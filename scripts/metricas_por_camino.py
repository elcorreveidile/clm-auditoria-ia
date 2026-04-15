#!/usr/bin/env python3
"""
📊 Métricas por Camino - Auditoría IA CLM

Calcula KPIs clave para cada camino del formulario.

Uso:
    python metricas_por_camino.py [--archivo ARCHIVO] [--camino CAMINO]

Ejemplos:
    python metricas_por_camino.py --archivo data/formspree_export.json
    python metricas_por_camino.py --camino biblioteca
"""

import pandas as pd
import json
import argparse
import sys

def cargar_datos(archivo):
    """Carga datos desde archivo JSON."""
    with open(archivo, 'r', encoding='utf-8') as f:
        return pd.json_normalize(json.load(f))

def calcular_metricas_camino(df, camino):
    """Calcula métricas para un camino específico."""
    df_camino = df[df['_camino'] == camino]

    if len(df_camino) == 0:
        return None

    metricas = {
        'camino': camino,
        'total_respuestas': len(df_camino),
    }

    # Buscar campo de uso de IA
    uso_col = encontrar_campo_similar(df_camino, ['uso', 'ia'])

    if uso_col:
        # Calcular % que usa IA en trabajo
        usa_trabajo = df_camino[uso_col].isin([
            'Sí trabajo ocasional',
            'Sí trabajo habitual',
            'Varias veces semana',
            'A diario'
        ])
        metricas['usa_ia_trabajo_pct'] = (usa_trabajo.sum() / len(df_camino)) * 100

    # Buscar campo de privacidad
    privacidad_col = encontrar_campo_similar(df_camino, ['datos_privados', 'privacidad'])

    if privacidad_col:
        riesgo_count = df_camino[df_camino[privacidad_col].isin(['Posiblemente', 'Sí'])]
        metricas['privacidad_riesgo_pct'] = (len(riesgo_count) / len(df_camino)) * 100

    # Buscar campo de nivel de prompting
    prompt_col = encontrar_campo_similar(df_camino, ['prompt', 'nivel'])

    if prompt_col:
        # Convertir respuestas a valores numéricos
        nivel_map = {
            'No lo conocía': 1,
            'Lo conozco no uso': 1,
            'No uso': 1,
            'Preguntas simples': 2,
            'Refino y corrijo': 3,
            'Refino resultados': 3,
            'Contexto y rol': 4,
            'Sistemático': 5,
            'Prompts elaborados': 5
        }

        df_camino['nivel_num'] = df_camino[prompt_col].map(nivel_map)
        metricas['nivel_prompting_promedio'] = df_camino['nivel_num'].mean()

    return metricas

def encontrar_campo_similar(df, palabras_clave):
    """Busca un campo que contenga alguna de las palabras clave."""
    for col in df.columns:
        col_lower = col.lower()
        if any(palabra in col_lower for palabra in palabras_clave):
            return col
    return None

def mostrar_metricas_todas(df):
    """Muestra métricas para todos los caminos."""
    print("\n" + "="*80)
    print("📊 MÉTRICAS POR CAMINO - AUDITORÍA IA CLM")
    print("="*80)

    print(f"\n{'Camino':<30} {'Respuestas':>12} {'Uso IA %':>10} {'Riesgo %':>10} {'Nivel Prom':>11}")
    print("─"*80)

    metricas_todas = []

    for camino in sorted(df['_camino'].unique()):
        metricas = calcular_metricas_camino(df, camino)

        if metricas:
            metricas_todas.append(metricas)

            uso_ia = metricas.get('usa_ia_trabajo_pct', 0)
            riesgo = metricas.get('privacidad_riesgo_pct', 0)
            nivel = metricas.get('nivel_prompting_promedio', 0)

            print(f"{metricas['camino']:<30} {metricas['total_respuestas']:>12} "
                  f"{uso_ia:>9.1f}% {riesgo:>9.1f}% {nivel:>10.2f}/5")

    # Resumen global
    print("─"*80)
    total_respuestas = sum(m['total_respuestas'] for m in metricas_todas)
    uso_ia_promedio = sum(m.get('usa_ia_trabajo_pct', 0) * m['total_respuestas'] for m in metricas_todas) / total_respuestas
    riesgo_promedio = sum(m.get('privacidad_riesgo_pct', 0) * m['total_respuestas'] for m in metricas_todas) / total_respuestas

    print(f"{'GLOBAL':<30} {total_respuestas:>12} {uso_ia_promedio:>9.1f}% {riesgo_promedio:>9.1f}%")

def mostrar_detalle_camino(df, camino):
    """Muestra métricas detalladas de un camino específico."""
    metricas = calcular_metricas_camino(df, camino)

    if not metricas:
        print(f"❌ No hay datos para el camino: {camino}")
        return

    print(f"\n{'='*80}")
    print(f"📌 MÉTRICAS DETALLADAS: {camino.upper()}")
    print(f"{'='*80}")

    print(f"\n📊 Respuestas totales: {metricas['total_respuestas']}")

    if 'usa_ia_trabajo_pct' in metricas:
        uso = metricas['usa_ia_trabajo_pct']
        print(f"\n🤖 Uso de IA en trabajo: {uso:.1f}%")

        if uso < 30:
            print("  ⚠️  Bajo uso: Considerar formación en IA")
        elif uso < 60:
            print("  📈 Uso medio: Potencial para mejora")
        else:
            print("  ✅ Alto uso: Buen nivel de adopción")

    if 'privacidad_riesgo_pct' in metricas:
        riesgo = metricas['privacidad_riesgo_pct']
        print(f"\n⚠️  Riesgos de privacidad: {riesgo:.1f}%")

        if riesgo > 30:
            print("  🚨 Riesgo ALTO: Formación en privacidad URGENTE")
        elif riesgo > 15:
            print("  ⚠️  Riesgo medio: Considerar formación en RGPD")
        else:
            print("  ✅ Riesgo bajo: Buen nivel de concienciación")

    if 'nivel_prompting_promedio' in metricas:
        nivel = metricas['nivel_prompting_promedio']
        print(f"\n📝 Nivel de prompting: {nivel:.2f}/5")

        if nivel < 2:
            print("  📚 Nivel básico: Formación en prompting recomendada")
        elif nivel < 3.5:
            print("  📈 Nivel intermedio: Potencial para optimizar prompts")
        else:
            print("  ✅ Nivel avanzado: Buen uso de técnicas de prompting")

def exportar_csv(df, archivo='data/metricas_por_camino.csv'):
    """Exporta métricas a CSV."""
    metricas_todas = []

    for camino in sorted(df['_camino'].unique()):
        metricas = calcular_metricas_camino(df, camino)
        if metricas:
            metricas_todas.append(metricas)

    df_metricas = pd.DataFrame(metricas_todas)
    df_metricas.to_csv(archivo, index=False, encoding='utf-8')
    print(f"\n✅ Métricas exportadas a: {archivo}")

def main():
    parser = argparse.ArgumentParser(description='Calcular métricas por camino')
    parser.add_argument('--archivo', type=str, default='data/formspree_export.json',
                        help='Archivo JSON exportado desde Formspree')
    parser.add_argument('--camino', type=str,
                        help='Analizar solo un camino específico')
    parser.add_argument('--exportar', action='store_true',
                        help='Exportar métricas a CSV')

    args = parser.parse_args()

    df = cargar_datos(args.archivo)

    if args.camino:
        mostrar_detalle_camino(df, args.camino)
    else:
        mostrar_metricas_todas(df)

    if args.exportar:
        exportar_csv(df)

if __name__ == '__main__':
    main()
