# 📖 Guía de Exportación Manual - GRATIS

## 🆓 Opción Gratuita: Exportación Manual desde Formspree

No necesitas API Key ni suscripción de pago. Puedes exportar los datos manualmente de forma gratuita.

---

## 📝 Pasos Detallados

### Paso 1: Acceder a Formspree

1. Ir a https://formspree.io/dashboard
2. Iniciar sesión con tu cuenta

### Paso 2: Seleccionar el Formulario

1. Buscar el formulario: **`mjgalypd`** (Auditoría IA · CLM · UGR)
2. Click en el formulario

### Paso 3: Ver Respuestas

1. Click en **"Submissions"** (en el menú lateral)
2. Verás todas las respuestas recibidas

### Paso 4: Exportar Datos

1. Click en el botón **"Export"** (arriba a la derecha)
2. Seleccionar formato:
   - **JSON** (recomendado) - Para scripts Python
   - **CSV** - Para Excel/Google Sheets
3. Click en **"Download"**
4. Guardar archivo en tu carpeta de Descargas

### Paso 5: Mover a Carpeta data/

```bash
# macOS/Linux
mv ~/Downloads/formspree_export.json data/

# Windows
move Downloads\formspree_export.json data\
```

---

## 🚀 Usar los Scripts con Datos Exportados

Una vez tengas el archivo en `data/`:

```bash
# Opción 1: Usar el analizador interactivo (más fácil)
python3 scripts/analizador_manual.py

# Opción 2: Usar scripts individuales
python3 scripts/analizar_resultados.py --archivo data/formspree_export.json
python3 scripts/metricas_por_camino.py --archivo data/formspree_export.json
python3 scripts/detectar_preguntas_problematicas.py --archivo data/formspree_export.json
```

---

## 💡 Recomendación

**Para análisis mensual:**
1. Exportar datos manualmente (5 minutos)
2. Ejecutar `analizador_manual.py`
3. Seleccionar opción 4 (análisis completo)

**Para análisis continuo:**
1. Exportar datos 1 vez por semana
2. Guardar con timestamp: `data/export_2026_04_16.json`
3. Usar scripts individuales según necesites

---

## ⚡ Ventajas de la Exportación Manual

✅ **GRATIS** - Sin coste  
✅ **SIN API KEY** - Sin configuración  
✅ **SIMPLE** - Solo 3 clicks  
✅ **FLEXIBLE** - Exportas cuando quieras  
✅ **SEGURO** - Tienes control total de los datos  

---

## 📊 Plan Gratuito Formspree

Si el CLM tiene **≤50 respuestas/mes**, el plan FREE es suficiente:

| Característica | Plan FREE |
|----------------|-----------|
| Formularios | 1 |
| Respuestas/mes | 50 |
| Exportación | ✅ Sí (CSV/JSON) |
| Integraciones | Básicas |
| **Precio** | **$0** |

**¿Más de 50 respuestas/mes?**
- La exportación manual sigue funcionando
- Solo exporta las últimas 50 respuestas
- Puedes exportar periódicamente para no perder datos

---

## 🔄 Flujo de Trabajo Recomendado (GRATIS)

### Semanal

```bash
# 1. Exportar desde Formspree (manual)
# https://formspree.io/dashboard → Export → Download

# 2. Mover a carpeta data/
mv ~/Downloads/formspree_export.json data/

# 3. Ejecutar análisis completo
python3 scripts/analizador_manual.py
# Seleccionar opción 4 (análisis completo)
```

### Mensual

```bash
# 1. Exportar desde Formspree
# 2. Renombrar con mes
mv data/formspree_export.json data/export_2026_04.json

# 3. Ejecutar análisis
python3 scripts/analizar_resultados.py --archivo data/export_2026_04.json
python3 scripts/metricas_por_camino.py --exportar
python3 scripts/detectar_preguntas_problematicas.py --exportar
```

---

## 📞 ¿Necesitas Ayuda?

Si tienes problemas con la exportación manual:

1. **No aparece el botón "Export"**
   - Verifica que tienes permisos de administrador en el formulario
   - Contacta con el equipo del CLM

2. **Error al leer el archivo**
   - Verifica que el archivo esté en formato JSON o CSV
   - Verifica que esté en la carpeta `data/`

3. **Scripts no funcionan**
   - Asegúrate de tener Python 3 instalado
   - Ejecuta: `pip3 install -r scripts/requirements.txt`

---

**Última actualización:** 16 de abril de 2026  
**Versión:** 1.0
