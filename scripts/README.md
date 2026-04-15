# 📊 Scripts de Análisis - Auditoría IA CLM

Esta carpeta contiene scripts Python para analizar los resultados del formulario de auditoría IA del CLM.

---

## 🚀 Instalación Rápida

### 1. Instalar Python 3

```bash
# Verificar versión de Python
python3 --version

# Si no está instalado:
# macOS: brew install python3
# Ubuntu: sudo apt-get install python3
# Windows: https://www.python.org/downloads/
```

### 2. Instalar Dependencias

```bash
cd scripts
pip3 install -r requirements.txt
```

### 3. Obtener Datos del Formulario

**🆓 OPCIÓN GRATIS (Recomendada):**

```bash
# 1. Exportar datos manualmente desde Formspree
#    (Ver: EXPORTAR_MANUAL_GRATIS.md)

# 2. Usar el analizador interactivo
python3 scripts/analizador_manual.py
```

**🔑 OPCIÓN CON API (Requiere suscripción):**

```bash
# 1. Obtener API Key de Formspree
#    https://formspree.io/dashboard → Settings → API Keys

# 2. Exportar automáticamente
python3 scripts/exportar_formspree.py --api-key TU_API_KEY
```

**💡 Ver EXPORTAR_MANUAL_GRATIS.md para instrucciones detalladas de exportación manual.**

---

## 📁 Scripts Disponibles

### 1. `exportar_formspree.py` 📥

**Propósito:** Exportar respuestas desde Formspree

**Uso básico:**
```bash
python3 exportar_formspree.py --api-key TU_API_KEY
```

**Opciones:**
```bash
# Exportar a JSON (default)
python3 exportar_formspree.py --api-key TU_API_KEY --formato json

# Exportar a CSV
python3 exportar_formspree.py --api-key TU_API_KEY --formato csv

# Especificar nombre de archivo
python3 exportar_formspree.py --api-key TU_API_KEY --archivo data/mis_datos.json

# Solo mostrar estadísticas (sin exportar)
python3 exportar_formspree.py --api-key TU_API_KEY --estadisticas
```

**Ejemplo de salida:**
```
✅ Exportadas 150 respuestas a: data/formspree_export_20260415_143022.json

💡 Ahora puedes analizar los datos con:
   python scripts/analizar_resultados.py --archivo data/formspree_export_20260415_143022.json
```

---

### 2. `analizar_resultados.py` 📊

**Propósito:** Análisis general de todas las respuestas

**Uso básico:**
```bash
python3 analizar_resultados.py --archivo data/formspree_export.json
```

**Opciones:**
```bash
# Usar archivo específico
python3 analizar_resultados.py --archivo data/mis_datos.json

# Exportar reporte a archivo
python3 analizar_resultados.py --archivo data/formspree_export.json --exportar
```

**Ejemplo de salida:**
```
============================================================
📊 RESUMEN GENERAL - AUDITORÍA IA CLM
============================================================

📈 Total de respuestas: 150

🎯 Respuestas por camino:
  • admin: 25 (16.7%)
  • biblioteca: 18 (12.0%)
  ...

💬 ANÁLISIS DE PREGUNTAS ABIERTAS
Temas más mencionados:
  • chatgpt: 45 veces
  • estudiantes: 38 veces
  • respuestas: 32 veces
```

---

### 3. `metricas_por_camino.py` 📈

**Propósito:** Calcular KPIs por cada camino

**Uso básico:**
```bash
# Analizar todos los caminos
python3 metricas_por_camino.py --archivo data/formspree_export.json

# Analizar un camino específico
python3 metricas_por_camino.py --camino biblioteca --archivo data/formspree_export.json
```

**Opciones:**
```bash
# Analizar todos los caminos
python3 metricas_por_camino.py --archivo data/formspree_export.json

# Analizar solo Biblioteca
python3 metricas_por_camino.py --camino biblioteca

# Exportar métricas a CSV
python3 metricas_por_camino.py --exportar
```

**Ejemplo de salida:**
```
================================================================================
📊 MÉTRICAS POR CAMINO - AUDITORÍA IA CLM
================================================================================

Camino                                Respuestas    Uso IA %    Riesgo %   Nivel Prom
────────────────────────────────────────────────────────────────────────────────
admin                                       25       45.2%      20.0%       2.85/5
biblioteca                                  18       52.3%      15.4%       3.12/5
...

================================================================================
📌 MÉTRICAS DETALLADAS: BIBLIOTECA
================================================================================

📊 Respuestas totales: 18

🤖 Uso de IA en trabajo: 52.3%
  📈 Uso medio: Potencial para mejora

⚠️  Riesgos de privacidad: 15.4%
  ✅ Riesgo bajo: Buen nivel de concienciación

📝 Nivel de prompting: 3.12/5
  📈 Nivel intermedio: Potencial para optimizar prompts
```

---

### 4. `detectar_preguntas_problematicas.py` 🔍

**Propósito:** Identificar preguntas que necesitan ajustes

**Uso básico:**
```bash
python3 detectar_preguntas_problematicas.py --archivo data/formspree_export.json
```

**Opciones:**
```bash
# Cambiar umbrales
python3 detectar_preguntas_problematicas.py \
    --umbral-vacios 40 \
    --umbral-otras 20 \
    --archivo data/formspree_export.json

# Exportar reporte a archivo
python3 detectar_preguntas_problematicas.py \
    --exportar \
    --archivo data/formspree_export.json
```

**Ejemplo de salida:**
```
================================================================================
⚠️  CAMPOS CON MÁS DEL 30% VACÍOS
================================================================================

Se encontraron 3 campos problemáticos:

📌 campo_observaciones
   Vacíos: 75/150 (50.0%)
   🚨 CRÍTICO: Más de la mitad vacío
   → ACCIÓN: Considerar eliminar o reformular significativamente

...

================================================================================
📋 RECOMENDACIONES DE MEJORA
================================================================================

🎯 PRIORIDAD ALTA (Revisar urgently):

   1. Campos con más del 50% vacíos:
      • campo_observaciones - Considerar eliminar o reformular
```

---

## 🔄 Flujo de Trabajo Recomendado

### Opción A: Manual (Más Fácil)

```bash
# 1. Exportar desde Formspree manualmente
# - Ir a https://formspree.io/dashboard
# - Seleccionar formulario
# - Export → JSON (descargar archivo)

# 2. Mover archivo a carpeta data/
mv ~/Downloads/formspree_export.json data/

# 3. Analizar resultados
python3 scripts/analizar_resultados.py --archivo data/formspree_export.json

# 4. Ver métricas por camino
python3 scripts/metricas_por_camino.py --archivo data/formspree_export.json

# 5. Detectar problemas
python3 scripts/detectar_preguntas_problematicas.py --archivo data/formspree_export.json
```

### Opción B: Automatizado (Con API)

```bash
# 1. Exportar datos automáticamente
python3 scripts/exportar_formspree.py --api-key TU_API_KEY

# 2. Analizar resultados (usa el archivo más reciente)
python3 scripts/analizar_resultados.py --archivo data/formspree_export_latest.json

# 3. Ver métricas
python3 scripts/metricas_por_camino.py --exportar

# 4. Detectar problemas
python3 scripts/detectar_preguntas_problematicas.py --exportar
```

---

## 📂 Carpeta `data/`

Esta carpeta almacenará:
- `formspree_export.json` - Última exportación (automática si usas API)
- `formspree_export_TIMESTAMP.json` - Exportaciones con timestamp
- `reporte_analisis.txt` - Reporte de análisis
- `metricas_por_camino.csv` - Métricas exportadas
- `reporte_problemas.txt` - Reporte de problemas detectados

---

## 📊 Ejemplos de Uso

### Ejemplo 1: Análisis Rápido Diario

```bash
# Ver estadísticas rápidas
python3 exportar_formspree.py --api-key TU_KEY --estadisticas
```

### Ejemplo 2: Análisis Semanal Completo

```bash
# 1. Exportar datos
python3 exportar_formspree.py --api-key TU_KEY --formato json

# 2. Análisis general
python3 analizar_resultados.py --exportar

# 3. Métricas por camino
python3 metricas_por_camino.py --exportar

# 4. Detectar problemas
python3 detectar_preguntas_problematicas.py --exportar

# 5. Revisar reportes generados
cat data/reporte_analisis.txt
cat data/reporte_problemas.txt
```

### Ejemplo 3: Análisis de un Camino Específico

```bash
# Ver métricas detalladas de Biblioteca
python3 metricas_por_camino.py --camino biblioteca
```

---

## 🔧 Solución de Problemas

### Error: "No module named 'pandas'"

**Solución:**
```bash
pip3 install -r requirements.txt
```

### Error: "API Key inválida"

**Solución:**
1. Verificar que la API Key es correcta
2. Asegurarse de que tiene permisos de lectura
3. Generar nueva API Key si es necesario

### Error: "Archivo no encontrado"

**Solución:**
```bash
# Crear carpeta data
mkdir -p data

# Exportar datos manualmente desde Formspree primero
```

---

## 📞 Soporte

**Para dudas o problemas:**

1. Revisar la guía principal: `../GUIA_MEJORAS_FUTURAS.md`
2. Verificar que tienes Python 3 instalado: `python3 --version`
3. Verificar dependencias: `pip3 list`
4. Abrir issue en GitHub

---

**Última actualización:** 15 de abril de 2026  
**Versión:** 1.0
