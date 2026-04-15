#!/usr/bin/env python3
"""
📥 Exportar Datos desde Formspree - Auditoría IA CLM

Exporta respuestas del formulario desde Formspree usando la API.

Requiere:
- API Key de Formspree
- pip install requests

Uso:
    python exportar_formspree.py --api-key TU_API_KEY

Obtener API Key:
    1. Ir a https://formspree.io/dashboard
    2. Click en el formulario
    3. Settings → API Keys
    4. Crear nueva API Key
"""

import requests
import json
import argparse
import sys
from datetime import datetime

class FormspreeExporter:
    """Exportador de datos desde Formspree."""

    BASE_URL = "https://formspree.io/api/v0"

    def __init__(self, api_key, form_id='mjgalypd'):
        """
        Inicializar exportador.

        Args:
            api_key: API Key de Formspree
            form_id: ID del formulario (default: mjgalypd)
        """
        self.api_key = api_key
        self.form_id = form_id
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def obtener_submissions(self, limit=100):
        """
        Obtiene las respuestas del formulario.

        Args:
            limit: Número máximo de respuestas a obtener

        Returns:
            Lista de diccionarios con las respuestas
        """
        url = f"{self.BASE_URL}/forms/{self.form_id}/submissions"

        try:
            response = requests.get(
                url,
                headers=self.headers,
                params={'limit': limit}
            )
            response.raise_for_status()

            data = response.json()
            return data.get('submissions', [])

        except requests.exceptions.RequestException as e:
            print(f"❌ Error al obtener datos: {e}")
            sys.exit(1)

    def exportar_json(self, archivo_salida=None):
        """
        Exporta respuestas a formato JSON.

        Args:
            archivo_salida: Nombre del archivo (default: data/formspree_EXPORT.json)

        Returns:
            Ruta del archivo exportado
        """
        if archivo_salida is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            archivo_salida = f'data/formspree_export_{timestamp}.json'

        submissions = self.obtener_submissions(limit=1000)

        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(submissions, f, indent=2, ensure_ascii=False)

        print(f"✅ Exportadas {len(submissions)} respuestas a: {archivo_salida}")

        return archivo_salida

    def exportar_csv(self, archivo_salida=None):
        """
        Exporta respuestas a formato CSV.

        Args:
            archivo_salida: Nombre del archivo (default: data/formspree_EXPORT.csv)

        Returns:
            Ruta del archivo exportado
        """
        import pandas as pd

        if archivo_salida is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            archivo_salida = f'data/formspree_export_{timestamp}.csv'

        submissions = self.obtener_submissions(limit=1000)

        # Normalizar datos JSON
        df = pd.json_normalize(submissions)

        # Guardar como CSV
        df.to_csv(archivo_salida, index=False, encoding='utf-8')

        print(f"✅ Exportadas {len(submissions)} respuestas a: {archivo_salida}")

        return archivo_salida

    def obtener_estadisticas(self):
        """
        Obtiene estadísticas básicas del formulario.

        Returns:
            Diccionario con estadísticas
        """
        submissions = self.obtener_submissions(limit=1000)

        if not submissions:
            return {}

        stats = {
            'total_respuestas': len(submissions),
            'camino': {},
        }

        # Contar por camino
        for submission in submissions:
            camino = submission.get('_camino', 'desconocido')
            stats['camino'][camino] = stats['camino'].get(camino, 0) + 1

        return stats

    def mostrar_estadisticas(self):
        """Muestra estadísticas por pantalla."""
        stats = self.obtener_estadisticas()

        if not stats:
            print("❌ No hay respuestas en el formulario")
            return

        print("\n" + "="*60)
        print("📊 ESTADÍSTICAS DEL FORMULARIO")
        print("="*60)

        print(f"\nTotal de respuestas: {stats['total_respuestas']}")

        if stats['camino']:
            print(f"\nRespuestas por camino:")
            for camino, count in sorted(stats['camino'].items()):
                pct = (count / stats['total_respuestas']) * 100
                print(f"  • {camino}: {count} ({pct:.1f}%)")

def main():
    parser = argparse.ArgumentParser(description='Exportar datos desde Formspree')
    parser.add_argument('--api-key', type=str, required=True,
                        help='API Key de Formspree')
    parser.add_argument('--form-id', type=str, default='mjgalypd',
                        help='ID del formulario (default: mjgalypd)')
    parser.add_argument('--formato', type=str, default='json', choices=['json', 'csv'],
                        help='Formato de exportación (default: json)')
    parser.add_argument('--archivo', type=str,
                        help='Nombre del archivo de salida')
    parser.add_argument('--estadisticas', action='store_true',
                        help='Mostrar estadísticas sin exportar')

    args = parser.parse_args()

    # Crear exportador
    exporter = FormspreeExporter(args.api_key, args.form_id)

    if args.estadisticas:
        exporter.mostrar_estadisticas()
    else:
        # Exportar en el formato solicitado
        if args.formato == 'json':
            archivo = exporter.exportar_json(args.archivo)
        else:
            archivo = exporter.exportar_csv(args.archivo)

        print(f"\n💡 Ahora puedes analizar los datos con:")
        print(f"   python scripts/analizar_resultados.py --archivo {archivo}")

if __name__ == '__main__':
    main()
