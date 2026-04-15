#!/usr/bin/env python3
"""
🔍 Detectar Preguntas Problemáticas - Auditoría IA CLM

Identifica preguntas que necesitan ajustes:
- Campos con muchos valores vacíos
- Preguntas con muchas respuestas "No sé"
- Opciones "Otras" muy usadas

Uso:
    python detectar_preguntas_problematicas.py --archivo ARCHIVO

Ejemplos:
    python detectar_preguntas_problematicas.py --archivo data/formspree_export.json
"""

import pandas as pd
import json
import argparse
import sys

def cargar_datos(archivo):
    """Carga datos desde archivo JSON."""
    with open(archivo, 'r', encoding='utf-8') as f:
        return pd.json_normalize(json.load(f))

def detectar_campos_vacios(df, umbral=30):
    """Detecta campos con más del umbral% de valores vacíos."""
    print("\n" + "="*80)
    print(f"⚠️  CAMPOS CON MÁS DEL {umbral}% VACÍOS")
    print("="*80)

    total_registros = len(df)
    campos_vacios = {}

    for col in df.columns:
        # Ignorar campos de metadatos
        if col.startswith('_'):
            continue

        vacios = df[col].isnull().sum() + (df[col] == '').sum()
        pct_vacios = (vacios / total_registros) * 100

        if pct_vacios >= umbral:
            campos_vacios[col] = {
                'vacios': vacios,
                'porcentaje': pct_vacios,
                'total': total_registros
            }

    if campos_vacios:
        print(f"\nSe encontraron {len(campos_vacios)} campos problemáticos:\n")

        # Ordenar por porcentaje
        campos_ordenados = sorted(campos_vacios.items(), key=lambda x: x[1]['porcentaje'], reverse=True)

        for campo, datos in campos_ordenados:
            print(f"📌 {campo}")
            print(f"   Vacíos: {datos['vacios']}/{datos['total']} ({datos['porcentaje']:.1f}%)")

            if datos['porcentaje'] > 50:
                print("   🚨 CRÍTICO: Más de la mitad vacío")
                print("   → ACCIÓN: Considerar eliminar o reformular significativamente")
            elif datos['porcentaje'] > 40:
                print("   ⚠️  MUY ALTO: Requiere revisión urgente")
                print("   → ACCIÓN: Revisar si la pregunta es comprensible")
            else:
                print("   ⚠️  ALTO: Mejora posible")
                print("   → ACCIÓN: Añadir ejemplos o aclarar")
            print()

        return campos_ordenados
    else:
        print("✅ ¡Bien! No hay campos con muchos vacíos")
        return []

def detectar_respuestas_no_se(df):
    """Detecta preguntas con muchas respuestas 'No sé'."""
    print("\n" + "="*80)
    print("❓ PREGUNTAS CONFUSAS (MUCHAS RESPUESTAS 'NO SÉ')")
    print("="*80)

    preguntas_confusas = []

    for col in df.columns:
        if col.startswith('_'):
            continue

        # Buscar respuestas "No sé" o similares
        respuestas_no_se = df[col].astype(str).str.contains('no sé|No sé|no lo sé|No lo sé', case=False, na=False)

        if respuestas_no_se.any():
            conteo = respuestas_no_se.sum()
            pct = (conteo / len(df)) * 100

            if pct >= 20:  # Umbral del 20%
                preguntas_confusas.append({
                    'campo': col,
                    'conteo': conteo,
                    'porcentaje': pct
                })

    if preguntas_confusas:
        print(f"\nSe encontraron {len(preguntas_confusas)} preguntas confusas:\n")

        for pregunta in sorted(preguntas_confusas, key=lambda x: x['porcentaje'], reverse=True):
            print(f"📌 {pregunta['campo']}")
            print(f"   'No sé': {pregunta['conteo']} ({pregunta['porcentaje']:.1f}%)")

            if pregunta['porcentaje'] > 30:
                print("   🚨 CRÍTICO: Requiere explicación o ejemplos")
            else:
                print("   ⚠️  MEJORAR: Aclarar la pregunta")
            print()

        return preguntas_confusas
    else:
        print("✅ ¡Bien! No hay preguntas confusas significativas")
        return []

def detectar_otras_frecuentes(df, umbral=15):
    """Detecta opciones 'Otras' muy usadas (indica que faltan opciones)."""
    print("\n" + "="*80)
    print(f"🔮 OPCIONES 'OTRAS' MUY USADAS (>{umbral}%)")
    print("="*80)

    opciones_faltantes = []

    for col in df.columns:
        if col.startswith('_'):
            continue

        # Buscar valores "Otras" o similares
        otras_respuestas = df[col].astype(str).str.contains('otra|Otra|otros|Otros|Other|other', case=False, na=False)

        if otras_respuestas.any():
            conteo = otras_respuestas.sum()
            pct = (conteo / len(df)) * 100

            if pct >= umbral:
                opciones_faltantes.append({
                    'campo': col,
                    'conteo': conteo,
                    'porcentaje': pct
                })

    if opciones_faltantes:
        print(f"\nSe encontraron {len(opciones_faltantes)} opciones 'Otras' frecuentes:\n")

        for opcion in sorted(opciones_faltantes, key=lambda x: x['porcentaje'], reverse=True):
            print(f"📌 {opcion['campo']}")
            print(f"   'Otras': {opcion['conteo']} ({opcion['porcentaje']:.1f}%)")
            print("   → ACCIÓN: Revisar campo y añadir opciones más comunes como respuestas principales")
            print()

        return opciones_faltantes
    else:
        print("✅ ¡Bien! Las opciones parecen suficientes")
        return []

def generar_recomendaciones(campos_vacios, preguntas_confusas, opciones_faltantes):
    """Genera recomendaciones de mejora."""
    print("\n" + "="*80)
    print("📋 RECOMENDACIONES DE MEJORA")
    print("="*80)

    total_errores = len(campos_vacios) + len(preguntas_confusas) + len(opciones_faltantes)

    if total_errores == 0:
        print("\n✅ ¡Excelente! No se detectaron problemas significativos.")
        print("   El formulario está bien optimizado.")
        return

    print(f"\nSe detectaron {total_errores} áreas de mejora:\n")

    print("🎯 PRIORIDAD ALTA (Revisar urgently):")

    # Campos críticos (>50% vacíos)
    criticos = [c for c in campos_vacios if c[1]['porcentaje'] > 50]
    if criticos:
        print("\n   1. Campos con más del 50% vacíos:")
        for campo, datos in criticos:
            print(f"      • {campo} - Considerar eliminar o reformular")

    # Preguntas muy confusas (>30% "No sé")
    muy_confusas = [p for p in preguntas_confusas if p['porcentaje'] > 30]
    if muy_confusas:
        print("\n   2. Preguntas muy confusas:")
        for pregunta in muy_confusas:
            print(f"      • {pregunta['campo']} - Añadir explicación y ejemplos")

    print("\n🎯 PRIORIDAD MEDIA (Mejorar pronto):")

    # Campos con 30-50% vacíos
    medios_vacios = [c for c in campos_vacios if 30 < c[1]['porcentaje'] <= 50]
    if medios_vacios:
        print("\n   1. Campos con 30-50% vacíos:")
        for campo, datos in medios_vacios:
            print(f"      • {campo} - Añadir ejemplos concretos")

    # Opciones "Otras" frecuentes
    if opciones_faltantes:
        print("\n   2. Opciones insuficientes:")
        for opcion in opciones_faltantes:
            print(f"      • {opcion['campo']} - Añadir opciones principales")

    print("\n📝 CÓLO RESUMEN:")
    print(f"   • Campos muy vacíos: {len(criticos)}")
    print(f"   • Preguntas confusas: {len(muy_confusas)}")
    print(f"   • Opciones insuficientes: {len(opciones_faltantes)}")
    print(f"   • Total mejoras recomendadas: {total_errores}")

def exportar_reporte(campos_vacios, preguntas_confusas, opciones_faltantes, archivo='data/reporte_problemas.txt'):
    """Exporta reporte de problemas a archivo."""
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write("🔍 REPORTE DE PREGUNTAS PROBLEMÁTICAS\n")
        f.write("="*80 + "\n\n")

        f.write("CAMPOS CON MUCHOS VACÍOS:\n")
        for campo, datos in campos_vacios:
            f.write(f"• {campo}: {datos['porcentaje']:.1f}% vacíos\n")

        f.write("\nPREGUNTAS CONFUSAS:\n")
        for pregunta in preguntas_confusas:
            f.write(f"• {pregunta['campo']}: {pregunta['porcentaje']:.1f}% 'No sé'\n")

        f.write("\nOPCIONES INSUFICIENTES:\n")
        for opcion in opciones_faltantes:
            f.write(f"• {opcion['campo']}: {opcion['porcentaje']:.1f}% 'Otras'\n")

    print(f"\n✅ Reporte exportado a: {archivo}")

def main():
    parser = argparse.ArgumentParser(description='Detectar preguntas problemáticas')
    parser.add_argument('--archivo', type=str, default='data/formspree_export.json',
                        help='Archivo JSON exportado desde Formspree')
    parser.add_argument('--umbral-vacios', type=float, default=30,
                        help='Umbral %% de vacíos para alertar (default: 30)')
    parser.add_argument('--umbral-otras', type=float, default=15,
                        help='Umbral %% de "Otras" para alertar (default: 15)')
    parser.add_argument('--exportar', action='store_true',
                        help='Exportar reporte a archivo')

    args = parser.parse_args()

    df = cargar_datos(args.archivo)

    # Ejecutar detecciones
    campos_vacios = detectar_campos_vacios(df, args.umbral_vacios)
    preguntas_confusas = detectar_respuestas_no_se(df)
    opciones_faltantes = detectar_otras_frecuentes(df, args.umbral_otras)

    # Generar recomendaciones
    generar_recomendaciones(campos_vacios, preguntas_confusas, opciones_faltantes)

    # Exportar si se solicita
    if args.exportar:
        exportar_reporte(campos_vacios, preguntas_confusas, opciones_faltantes)

if __name__ == '__main__':
    main()
