#!/usr/bin/env python3
"""
🔓 Extraer Datos Manualmente desde Web - Auditoría IA CLM

Script para extraer datos de Formspree copiando desde la interfaz web.

Instrucciones:
1. Ir a https://formspree.io/dashboard
2. Abrir las submissions una por una
3. Copiar el JSON de cada una
4. Pegar en un archivo de texto
5. Ejecutar este script

Uso:
    # Paso 1: Copiar datos de las submissions (ver EXPORTAR_DESDE_WEB.md)
    # Paso 2:
    python3 extraer_desde_web.py --archivo data/copiado_web.txt
"""

import json
import argparse
import pandas as pd
from datetime import datetime

def parse_copied_text(archivo):
    """
    Parsea texto copiado desde la interfaz web de Formspree.

    Formato esperado (cada submission entre ---):
    ---
    {"reply": {"_camino": "biblioteca", "bib_tareas": ["Atención presencial"]}}
    ---
    {"reply": {"_camino": "admin", "admin_herramientas": ["Email"]}}
    ---
    """
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()

    submissions = []

    # Buscar bloques JSON entre ---
    bloques = contenido.split('---')

    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque:
            continue

        try:
            # Intentar parsear como JSON
            data = json.loads(bloque)
            submissions.append(data)
        except json.JSONDecodeError:
            # Si falla, intentar extraer JSON del bloque
            if 'reply' in bloque or '{' in bloque:
                # Buscar primer JSON válido
                inicio = bloque.find('{')
                if inicio != -1:
                    # Encontrar cierre
                    nivel = 0
                    fin = inicio
                    for i in range(inicio, len(bloque)):
                        if bloque[i] == '{':
                            nivel += 1
                        elif bloque[i] == '}':
                            nivel -= 1
                            if nivel == 0:
                                fin = i + 1
                                break

                    json_str = bloque[inicio:fin]
                    try:
                        data = json.loads(json_str)
                        submissions.append(data)
                    except:
                        pass

    return submissions

def exportar_json(submissions, archivo_salida='data/formspree_extraido.json'):
    """Exporta submissions a JSON."""
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(submissions, f, indent=2, ensure_ascii=False)

    print(f"✅ Exportadas {len(submissions)} submissions a: {archivo_salida}")

def main():
    parser = argparse.ArgumentParser(description='Extraer datos copiados desde web Formspree')
    parser.add_argument('--archivo', type=str, default='data/copiado_web.txt',
                        help='Archivo de texto con datos copiados desde web')
    parser.add_argument('--output', type=str, default='data/formspree_extraido.json',
                        help='Archivo JSON de salida')

    args = parser.parse_args()

    submissions = parse_copied_text(args.archivo)

    if submissions:
        print(f"✅ Se encontraron {len(submissions)} submissions")

        # Exportar a JSON
        exportar_json(submissions, args.output)

        # Crear DataFrame para análisis
        df = pd.json_normalize(submissions)

        print(f"\n📊 Datos listos para análisis:")
        print(f"   Total de respuestas: {len(df)}")

        if '_camino' in df.columns:
            print(f"\n   Respuestas por camino:")
            camino_counts = df['_camino'].value_counts()
            for camino, count in camino_counts.items():
                print(f"      • {camino}: {count}")

        print(f"\n💡 Ahora puedes usar los scripts de análisis:")
        print(f"   python3 scripts/analizar_resultados.py --archivo {args.output}")
        print(f"   python3 scripts/metricas_por_camino.py --archivo {args.output}")

    else:
        print("❌ No se encontraron submissions válidas en el archivo")
        print("\n💡 Asegúrate de:")
        print("   1. Copiar el contenido de cada submission")
        print("   2. Pegar en un archivo de texto")
        print("   3. Separar cada submission con '---'")

if __name__ == '__main__':
    main()
