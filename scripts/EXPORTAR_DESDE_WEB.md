# 📖 Guía de Extracción Manual desde Web - GRATIS

## 🚨 Problema: Formspree Cobra por Exportación

Formspree ha limitado la exportación de datos a planes de pago.

## ✅ Soluciones Gratuitas

---

## 📋 Opción 1: Copiar Manualmente desde Interfaz Web

### Paso 1: Abrir las Submissions

1. Ir a https://formspree.io/dashboard
2. Click en formulario `mjgalypd`
3. Click en **"Submissions"**

### Paso 2: Abrir Cada Submission

Verás una lista como esta:
```
┌─────────────────────────────────────────────┐
│ From: alguien@ugr.es                        │
│ Subject: [Auditoría IA · CLM · UGR]         │
│ Date: April 16, 2026 at 10:30 AM          │
│                                                 │
│ [View Submission] ← Click aquí              │
└─────────────────────────────────────────────┘
```

### Paso 3: Copiar Datos de Cada Submission

1. Click en **"View Submission"** de cada respuesta
2. Verás los datos en formato JSON
3. **Copiar todo el contenido** (Ctrl+A, Ctrl+C)
4. Pegar en un archivo de texto

### Paso 4: Formatear el Archivo

Crea un archivo `data/copiado_web.txt` con formato:

```
---
{"_camino": "biblioteca", "bib_tareas": ["Atención presencial", "Catalogación"], "bib_uso_ia": "Sí trabajo habitual"}
---
{"_camino": "admin", "admin_herramientas": ["Email", "Excel"]}
---
{"_camino": "marketing", "mkt_herramientas": ["Instagram", "Canva"]}
---
```

**Separar cada submission con `---`**

### Paso 5: Extraer con Script

```bash
python3 scripts/extraer_desde_web.py --archivo data/copiado_web.txt
```

**Output:**
```
✅ Se encontraron 3 submissions
✅ Exportadas 3 submissions a: data/formspree_extraido.json

📊 Datos listos para análisis:
   Total de respuestas: 3

💡 Ahora puedes usar los scripts de análisis:
   python3 scripts/analizar_resultados.py --archivo data/formspree_extraido.json
```

---

## 🔧 Opción 2: Script Automatizado con Selenium

Si tienes muchas respuestas y quieres automatizar el proceso:

```python
# extraer_automatico_web.py (pendiente de implementación)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Configurar navegador
driver = webdriver.Chrome()
driver.get("https://formspree.io/dashboard")

# Login (implementar)
# ...

# Navegar a submissions
driver.find_element(By.LINK_TEXT, "Submissions").click()

# Extraer cada submission
submissions = []
elements = driver.find_elements(By.CLASS_NAME, "submission")

for elem in elements:
    elem.click()
    time.sleep(1)

    # Copiar JSON
    json_text = driver.find_element(By.TAG_NAME, "pre").text
    submissions.append(json.loads(json_text))

    # Volver atrás
    driver.back()

# Guardar
with open('data/formspree_extraido.json', 'w') as f:
    json.dump(submissions, f)

driver.quit()
```

---

## 💡 Opción 3: Migrar a Servicio Gratuito

Si necesitas exportación frecuente, considera migrar a:

### Google Forms (GRATIS)

**Ventajas:**
- ✅ 100% gratis
- ✅ Exportación ilimitada a Google Sheets
- ✅ Integración con Google Sheets
- ✅ Análisis con Google Data Studio

**Desventajas:**
- ❌ Requiere cambiar formulario en el HTML
- ❌ Los datos van a Google (no Formspree)

**Migración:**
1. Crear Google Forms con las mismas preguntas
2. Cambiar `action` del formulario en `index.html`
3. Configurar Google Sheets para recibir respuestas

### Typeform (Plan Free)

**Ventajas:**
- ✅ Interfaz muy bonita
- ✅ Plan gratuito con exportación básica
- ✅ Analytics integrados

**Desventajas:**
- ❌ Limitaciones en plan free
- ❌ Requiere recrear formulario

---

## 🎯 Recomendación

### Si tienes pocas respuestas (<20):
Usa **Opción 1** (copiar manualmente)

### Si tienes muchas respuestas (>50):
- **Corto plazo:** Usar **Opción 1** una vez
- **Largo plazo:** Considerar migrar a **Google Forms** (Opción 3)

### Para automatización completa:
Implementar **Opción 2** (Selenium)

---

## 📞 Ayuda Rápida

**¿Cuál opción usar?**

| Situación | Opción Recomendada |
|-----------|-------------------|
| < 10 respuestas | Opción 1 (manual) |
| 10-50 respuestas | Opción 1 (manual) |
| > 50 respuestas | Opción 3 (migrar a Google Forms) |
| Exportación frecuente | Opción 2 (Selenium) |

---

**Última actualización:** 16 de abril de 2026  
**Versión:** 1.0
