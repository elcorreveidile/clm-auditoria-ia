#!/usr/bin/env python3
"""
📊 Análisis de Resultados - Auditoría IA CLM

Script principal para analizar las respuestas del formulario.

Uso:
    python analizar_resultados.py [--archivo ARCHIVO]

Ejemplos:
    python analizar_resultados.py --archivo data/formspree_export.json
    python analizar_resultados.py  # Usa datos de ejemplo
"""

import pandas as pd
import json
import argparse
from collections import Counter
import sys

def cargar_datos(archivo):
    """Carga datos desde archivo JSON de Formspree."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return pd.json_normalize(data)
    except FileNotFoundError:
        print(f"❌ Error: No se encuentra el archivo {archivo}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: El archivo {archivo} no es un JSON válido")
        sys.exit(1)

def resumen_general(df):
    """Muestra un resumen general de los datos."""
    print("\n" + "="*60)
    print("📊 RESUMEN GENERAL - AUDITORÍA IA CLM")
    print("="*60)

    total_respuestas = len(df)
    print(f"\n📈 Total de respuestas: {total_respuestas}")

    if '_camino' in df.columns:
        print(f"\n🎯 Respuestas por camino:")
        camino_counts = df['_camino'].value_counts().sort_index()
        for camino, count in camino_counts.items():
            pct = (count / total_respuestas) * 100
            print(f"  • {camino}: {count} ({pct:.1f}%)")

    if 'date' in df.columns or 'timestamp' in df.columns:
        fecha_col = 'date' if 'date' in df.columns else 'timestamp'
        df[fecha_col] = pd.to_datetime(df[fecha_col])
        fecha_min = df[fecha_col].min()
        fecha_max = df[fecha_col].max()
        print(f"\n📅 Período: {fecha_min.strftime('%d/%m/%Y')} - {fecha_max.strftime('%d/%m/%Y')}")

def analizar_por_camino(df):
    """Analiza métricas por cada camino."""
    print("\n" + "="*60)
    print("🎯 ANÁLISIS POR CAMINO")
    print("="*60)

    if '_camino' not in df.columns:
        print("⚠️  No se encuentra el campo '_camino'")
        return

    for camino in df['_camino'].unique():
        df_camino = df[df['_camino'] == camino]

        print(f"\n{'─'*60}")
        print(f"📌 {camino.upper()}")
        print(f"{'─'*60}")

        print(f"Total respuestas: {len(df_camino)}")

        # Uso de IA (si existe el campo específico del camino)
        uso_col = None
        for col in df_camino.columns:
            if 'uso' in col.lower() and 'ia' in col.lower() and col != 'bib_uso_concreto':
                uso_col = col
                break

        if uso_col and uso_col in df_camino.columns:
            print(f"\n📊 Uso de IA:")
            uso_counts = df_camino[uso_col].value_counts()
            for valor, count in uso_counts.items():
                pct = (count / len(df_camino)) * 100
                print(f"  • {valor}: {count} ({pct:.1f}%)")

        # Privacidad (si existe)
        privacidad_col = None
        for col in df_camino.columns:
            if 'datos_privados' in col.lower() or 'privacidad' in col.lower():
                privacidad_col = col
                break

        if privacidad_col and privacidad_col in df_camino.columns:
            print(f"\n⚠️  Riesgos de privacidad:")
            riesgo_count = df_camino[df_camino[privacidad_col].isin(['Posiblemente', 'Sí'])]
            riesgo_pct = (len(riesgo_count) / len(df_camino)) * 100
            print(f"  • Con riesgos: {len(riesgo_count)} ({riesgo_pct:.1f}%)")

def analizar_preguntas_abiertas(df):
    """Analiza campos de texto abierto para detectar temas recurrentes."""
    print("\n" + "="*60)
    print("💬 ANÁLISIS DE PREGUNTAS ABIERTAS")
    print("="*60)

    # Buscar campos de texto abierto
    campos_texto = [
        col for col in df.columns
        if df[col].dtype == 'object' and
           any(keyword in col.lower() for keyword in ['uso_concreto', 'tarea_automatizar', 'observaciones', 'oportunidades'])
    ]

    if not campos_texto:
        print("No se encontraron campos de texto abierto")
        return

    for campo in campos_texto:
        print(f"\n📝 Campo: {campo}")

        # Contar palabras más frecuentes
        todas_palabras = []
        for texto in df[campo].dropna():
            if texto and texto.lower() not in ['nunca', 'no sé', '']:
                palabras = str(texto).lower().split()
                todas_palabras.extend(palabras)

        if todas_palabras:
            # Filtrar palabras comunes
            stopwords = ['de', 'la', 'el', 'en', 'que', 'y', 'a', 'los', 'se', 'del', 'las', 'un', 'por', 'con', 'una', 'para', 'al', 'lo', 'como', 'más']
            palabras_filtradas = [p for p in todas_palabras if p not in stopwords and len(p) > 3]

            word_freq = Counter(palabras_filtradas)
            top_10 = word_freq.most_common(10)

            print("Temas más mencionados:")
            for palabra, freq in top_10:
                print(f"  • {palabra}: {freq} veces")

def exportar_reporte(df, archivo_salida='data/reporte_analisis.txt'):
    """Exporta el análisis a un archivo de texto."""
    original_stdout = sys.stdout

    with open(archivo_salida, 'w', encoding='utf-8') as f:
        sys.stdout = f

        resumen_general(df)
        analizar_por_camino(df)
        analizar_preguntas_abiertas(df)

        sys.stdout = original_stdout

    print(f"\n✅ Reporte exportado a: {archivo_salida}")

def main():
    parser = argparse.ArgumentParser(description='Analizar resultados de la auditoría IA CLM')
    parser.add_argument('--archivo', type=str, default='data/formspree_export.json',
                        help='Archivo JSON exportado desde Formspree (default: data/formspree_export.json)')
    parser.add_argument('--exportar', action='store_true',
                        help='Exportar reporte a archivo')

    args = parser.parse_args()

    # Cargar datos
    df = cargar_datos(args.archivo)

    # Ejecutar análisis
    resumen_general(df)
    analizar_por_camino(df)
    analizar_preguntas_abiertas(df)

    # Exportar si se solicita
    if args.exportar:
        exportar_reporte(df)

    print("\n" + "="*60)
    print("✅ Análisis completado")
    print("="*60)

if __name__ == '__main__':
    main()
