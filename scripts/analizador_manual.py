#!/usr/bin/env python3
"""
📊 Analizador Manual - Auditoría IA CLM

Versión simplificada que NO requiere API Key de Formspree.

Uso:
    1. Exportar datos manualmente desde Formspree (CSV o JSON)
    2. Copiar archivo a carpeta data/
    3. Ejecutar este script

Instrucciones detalladas en README_MANUAL.md
"""

import pandas as pd
import json
import argparse
import sys
import os
from pathlib import Path

def encontrar_archivo_reciente(directorio='data'):
    """Encuentra el archivo más reciente en el directorio."""
    if not os.path.exists(directorio):
        print(f"❌ Error: No existe el directorio '{directorio}'")
        print(f"   Crea el directorio: mkdir {directorio}")
        return None

    # Buscar archivos JSON o CSV
    archivos = []
    for extension in ['*.json', '*.csv']:
        archivos.extend(Path(directorio).glob(extension))

    if not archivos:
        print(f"❌ No se encontraron archivos JSON o CSV en '{directorio}'")
        print(f"\n📝 Pasos a seguir:")
        print(f"   1. Ir a https://formspree.io/dashboard")
        print(f"   2. Seleccionar el formulario")
        print(f"   3. Click en 'Submissions'")
        print(f"   4. Click en 'Export'")
        print(f"   5. Descargar como JSON o CSV")
        print(f"   6. Copiar archivo a carpeta data/")
        print(f"\n   Ejemplo:")
        print(f"   mv ~/Downloads/formspree_export.json {directorio}/")
        return None

    # Devolver el más reciente
    archivo_reciente = max(archivos, key=lambda p: p.stat().st_mtime)
    return str(archivo_reciente)

def cargar_archivo(archivo):
    """Carga datos desde archivo JSON o CSV."""
    if not os.path.exists(archivo):
        print(f"❌ Error: No existe el archivo {archivo}")
        return None

    try:
        if archivo.endswith('.json'):
            with open(archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return pd.json_normalize(data)
        elif archivo.endswith('.csv'):
            return pd.read_csv(archivo, encoding='utf-8')
        else:
            print(f"❌ Formato no soportado: {archivo}")
            print(f"   Usa JSON o CSV")
            return None
    except Exception as e:
        print(f"❌ Error al leer archivo: {e}")
        return None

def menu_principal():
    """Muestra menú principal."""
    print("\n" + "="*60)
    print("📊 ANÁLISIS DE RESULTADOS - AUDITORÍA IA CLM")
    print("="*60)

    print("\n¿Qué deseas hacer?")
    print("\n  1. 📈 Análisis general de todas las respuestas")
    print("  2. 🎯 Métricas por camino (KPIs)")
    print("  3. 🔍 Detectar preguntas problemáticas")
    print("  4. 📋 Análisis completo (todos los anteriores)")
    print("  5. ❓ Ayuda")

    eleccion = input("\nSelecciona una opción (1-5): ").strip()

    return eleccion

def ejecutar_analisis(archivo):
    """Ejecuta el análisis seleccionado."""
    df = cargar_archivo(archivo)

    if df is None:
        return False

    print(f"\n✅ Archivo cargado: {archivo}")
    print(f"   Total de respuestas: {len(df)}")

    # Importar funciones de análisis
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    try:
        from analizar_resultados import resumen_general, analizar_por_camino, analizar_preguntas_abiertas
        from metricas_por_camino import mostrar_metricas_todas, mostrar_detalle_camino
        from detectar_preguntas_problematicas import detectar_campos_vacios, detectar_respuestas_no_se, generar_recomendaciones

        # Ejecutar análisis según selección
        if opcion == '1':
            resumen_general(df)
            analizar_por_camino(df)

        elif opcion == '2':
            camino = input("\nIntroduce el nombre del camino (o presiona Enter para todos): ").strip()
            if camino:
                mostrar_detalle_camino(df, camino)
            else:
                mostrar_metricas_todas(df)

        elif opcion == '3':
            detectar_campos_vacios(df)
            detectar_respuestas_no_se(df)

        elif opcion == '4':
            resumen_general(df)
            analizar_por_camino(df)
            analizar_preguntas_abiertas(df)

            print("\n" + "="*60)
            print("📈 MÉTRICAS POR CAMINO")
            print("="*60)
            mostrar_metricas_todas(df)

            print("\n" + "="*60)
            print("🔍 DETECCIÓN DE PROBLEMAS")
            print("="*60)
            campos_vacios = detectar_campos_vacios(df)
            preguntas_confusas = detectar_respuestas_no_se(df)
            generar_recomendaciones(campos_vacios, preguntas_confusas, [])

        elif opcion == '5':
            mostrar_ayuda()

        return True

    except ImportError as e:
        print(f"❌ Error al importar módulos: {e}")
        return False

def mostrar_ayuda():
    """Muestra ayuda detallada."""
    print("\n" + "="*60)
    print("📖 AYUDA - ANÁLISIS MANUAL")
    print("="*60)

    print("\n📝 CÓMO OBTENER DATOS DESDE FORMSPREE:")
    print("\n   1. Ir a https://formspree.io/dashboard")
    print("   2. Seleccionar formulario 'mjgalypd'")
    print("   3. Click en 'Submissions' (respuestas)")
    print("   4. Click en 'Export' (arriba a la derecha)")
    print("   5. Seleccionar formato: JSON o CSV")
    print("   6. Click en 'Download'")
    print("   7. Mover archivo descargado a carpeta data/")
    print("\n   Ejemplo:")
    print("   mv ~/Downloads/formspree_export.json data/")

    print("\n📁 ESTRUCTURA DE ARCHIVOS:")
    print("\n   data/")
    print("   ├── formspree_export.json")
    print("   ├── formspree_export.csv")
    print("   └── formspree_export_TIMESTAMP.json")

    print("\n🔧 SCRIPTS DISPONIBLES:")
    print("\n   • analizar_resultados.py - Análisis general")
    print("   • metricas_por_camino.py - KPIs por camino")
    print("   • detectar_preguntas_problematicas.py - Detectar mejoras")

def main():
    """Función principal."""
    print("\n🔍 Buscando archivo de datos más reciente...")

    archivo = encontrar_archivo_reciente()

    if not archivo:
        return

    print(f"\n✅ Archivo encontrado: {archivo}")

    # Verificar si hay múltiples archivos
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    try:
        from detectar_preguntas_problematicas import cargar_datos as cargar_datos_v2
        df = cargar_datos_v2(archivo)

        print(f"\n📊 Datos cargados: {len(df)} respuestas")

        # Mostrar menú
        global opcion
        opcion = menu_principal()

        if opcion in ['1', '2', '3', '4']:
            # Importar scripts necesarios
            if opcion == '1':
                from analizar_resultados import resumen_general, analizar_por_camino, analizar_preguntas_abiertas
                resumen_general(df)
                analizar_por_camino(df)
                analizar_preguntas_abiertas(df)

            elif opcion == '2':
                from metricas_por_camino import mostrar_metricas_todas
                mostrar_metricas_todas(df)

            elif opcion == '3':
                from detectar_preguntas_problematicas import detectar_campos_vacios, detectar_respuestas_no_se
                detectar_campos_vacios(df)
                detectar_respuestas_no_se(df)

            elif opcion == '4':
                from analizar_resultados import resumen_general, analizar_por_camino, analizar_preguntas_abiertas
                from metricas_por_camino import mostrar_metricas_todas
                from detectar_preguntas_problematicas import detectar_campos_vacios, detectar_respuestas_no_se, generar_recomendaciones

                print("\n" + "="*60)
                print("📊 ANÁLISIS GENERAL")
                print("="*60)
                resumen_general(df)
                analizar_por_camino(df)
                analizar_preguntas_abiertas(df)

                print("\n" + "="*60)
                print("📈 MÉTRICAS POR CAMINO")
                print("="*60)
                mostrar_metricas_todas(df)

                print("\n" + "="*60)
                print("🔍 DETECCIÓN DE PROBLEMAS")
                print("="*60)
                campos_vacios = detectar_campos_vacios(df)
                preguntas_confusas = detectar_respuestas_no_se(df)
                generar_recomendaciones(campos_vacios, preguntas_confusas, [])

        elif opcion == '5':
            mostrar_ayuda()
        else:
            print("❌ Opción no válida")
            return

        print("\n" + "="*60)
        print("✅ ANÁLISIS COMPLETADO")
        print("="*60)

    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Asegúrate de que los scripts de análisis estén en la misma carpeta")
        return

if __name__ == '__main__':
    main()
