# 🚀 Guía de Mejoras Futuras - Auditoría IA CLM

**Versión:** 1.0  
**Fecha:** 15 de abril de 2026  
**Formulario:** https://clm.laclasedigital.com  
**Repositorio:** https://github.com/elcorreveidile/clm-auditoria-ia

---

## 📋 Índice

1. [Análisis de Resultados del Formulario](#1-análisis-de-resultados-del-formulario)
2. [Ajuste de Preguntas según Feedback](#2-ajuste-de-preguntas-según-feedback)
3. [Creación de Informes Automáticos](#3-creación-de-informes-automáticos)
4. [Implementación de Mejoras Adicionales](#4-implementación-de-mejoras-adicionales)
5. [Checklist de Mantenimiento](#5-checklist-de-mantenimiento)

---

## 1. Análisis de Resultados del Formulario

### 1.1 Acceso a Datos de Formspree

**Opción A: Interface Web (Para análisis rápido)**

1. Ir a https://formspree.io/dashboard
2. Seleccionar el formulario `mjgalypd`
3. Ver/enviar respuestas a:
   - Excel/CSV
   - JSON
   - Integraciones (Google Sheets, Zapier)

**Opción B: API (Para automatización)**

```bash
# Endpoint de la API
curl -X GET \
  https://formspree.io/api/v0/forms/mjgalypd/submissions \
  -H "Authorization: Bearer TU_API_KEY"
```

### 1.2 Análisis por Camino

**Estructura de Datos:**
```json
{
  "_camino": "biblioteca",
  "_tipo": "auditoria-biblioteca-clm",
  "bib_tareas": ["Atención presencial", "Catalogación"],
  "bib_uso_concreto": "He usado ChatGPT para...",
  "bib_chatbot": "Muy positivo",
  // ... más campos
}
```

**Scripts de Análisis (Python):**

```python
# analizar_resultados.py
import pandas as pd
import json

# Cargar datos desde Formspree (exportado como JSON)
with open('formspree_export.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)

# Análisis por camino
for camino in df['_camino'].unique():
    df_camino = df[df['_camino'] == camino]
    print(f"\n=== {camino.toUpperCase()} ===")
    print(f"Respuestas: {len(df_camino)}")
    
    # Ejemplo: Usos de IA más comunes
    if 'bib_uso_concreto' in df_camino.columns:
        print(df_camino['bib_uso_concreto'].value_counts().head(10))
```

### 1.3 Métricas Clave por Camino

**KPIs Recomendados:**

| Métrica | Descripción | Cómo Calcular |
|---------|-------------|---------------|
| **Tasa de respuesta** | % de respuestas completas | (Completadas / Iniciadas) × 100 |
| **Uso de IA actual** | % que usa IA en trabajo | (Usa IA / Total respuestas) × 100 |
| **Nivel de prompting** | Nivel medio de prompting | Promedio de respuestas 1-5 |
| **Riesgos de privacidad** | % con riesgos detectados | (Posiblemente+Sí / Total) × 100 |
| **Necesidades de formación** | Áreas con más demanda | Top 5 necesidades (1-5) |

**Script de Métricas:**

```python
# metricas_por_camino.py
import pandas as pd

def calcular_metricas(df, camino):
    df_camino = df[df['_camino'] == camino]
    
    metricas = {
        'total_respuestas': len(df_camino),
        'usa_ia_pct': (df_camino['uso_ia_alguna_vez'].isin(['Sí trabajo ocasional', 'Sí trabajo habitual']).sum() / len(df_camino)) * 100,
        'privacidad_riesgo_pct': (df_camino['datos_privados'].isin(['Posiblemente', 'Sí']).sum() / len(df_camino)) * 100,
    }
    
    return metricas

# Aplicar a todos los caminos
for camino in df['_camino'].unique():
    print(f"{camino}: {calcular_metricas(df, camino)}")
```

### 1.4 Visualización de Datos

**Opción A: Google Data Studio (Gratis)**

1. Exportar datos de Formspree a Google Sheets
2. Crear dashboard en Data Studio
3. Gráficos recomendados:
   - Barras: Respuestas por camino
   - Pie: Uso de IA por área
   - Heatmap: Necesidades de formación
   - Línea temporal: Evolución mensual

**Opción B: Streamlit (Python)**

```python
# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Auditoría IA - CLM")

df = pd.read_json('formspree_export.json')

# Filtro por camino
camino = st.selectbox('Selecciona camino', df['_camino'].unique())
df_camino = df[df['_camino'] == camino]

# Gráfico de uso de IA
fig = px.pie(df_camino, names='uso_ia_alguna_vez', title='Uso de IA')
st.plotly_chart(fig)
```

**Ejecutar:**
```bash
streamlit run dashboard.py
```

---

## 2. Ajuste de Preguntas según Feedback

### 2.1 Metodología de Mejora Continua

**Ciclo de Vida de una Pregunta:**

```
1. DISEÑO → 2. PRODUCCIÓN → 3. ANÁLISIS → 4. AJUSTE → 1. DISEÑO
```

### 2.2 Identificación de Preguntas Problemáticas

**Señales de alerta:**

| Señal | Causa Probable | Acción |
|-------|----------------|--------|
| Alta tasa de "No sé qué es dato personal" | Falta de formación | Añadir explicación o ejemplo |
| Muchos campos vacíos en preguntas abiertas | Pregunta mal formulada | Simplificar o dar ejemplos |
| Preguntas omitidas sistemáticamente | No relevante | Revisar o eliminar |
| Comentarios en "Otras" | Opciones insuficientes | Añadir como opción principal |

**Script de Detección:**

```python
# detectar_preguntas_problematicas.py
import pandas as pd

df = pd.read_json('formspree_export.json')

# Campos vacíos > 30%
campos_vacios = df.isnull().sum() / len(df) * 100
problematicos = campos_vacios[campos_vacios > 30]
print("Campos con más del 30% vacíos:")
print(problematicos)

# Respuestas "No sé" en privacidad
no_se_count = df[df['datos_privados'] == 'No sé qué son'].shape[0]
print(f"\nConfusión sobre privacidad: {no_se_count} ({no_se_count/len(df)*100:.1f}%)")
```

### 2.3 Proceso de Ajuste de Preguntas

**Paso 1: Análisis Cualitativo**

```python
# analizar_comentarios.py
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_json('formspree_export.json')

# Extraer campos de texto abierto
campos_texto = [col for col in df.columns if df[col].dtype == 'object']

for campo in campos_texto:
    if campo.startswith(('uso_concreto', 'tarea_automatizar', 'observaciones')):
        texto = ' '.join(df[campo].dropna().astype(str))
        
        # Nube de palabras
        wordcloud = WordCloud(width=800, height=400).generate(texto)
        
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud)
        plt.title(f'Temas más mencionados: {campo}')
        plt.axis('off')
        plt.show()
```

**Paso 2: Decisión de Cambio**

Usar este flujo de decisión:

```
¿Más del 20% de respuestas son "No sé" o están vacías?
├─ SÍ → ¿Es la pregunta importante?
│   ├─ SÍ → Reformular con ejemplos concretos
│   └─ NO → Eliminar pregunta
└─ NO → ¿Más del 30% usa "Otras"?
    ├─ SÍ → Añadir opciones principales
    └─ NO → Mantener pregunta
```

**Paso 3: Implementación del Cambio**

```bash
# 1. Hacer backup del archivo actual
cp index.html index.html.backup

# 2. Editar la pregunta en index.html
# Buscar el campo correspondiente y modificar

# 3. Probar localmente
# Abrir index.html en navegador y verificar

# 4. Commit con mensaje descriptivo
git add index.html
git commit -m "fix: reformulada Pregunta X (20% estaban vacíos)

Antes: ¿Qué usas?
Ahora: ¿Qué usas? (Ej: ChatGPT para correos...)

Motivo: Análisis de respuestas mostró confusión"

# 5. Push a producción
git push origin main
```

### 2.4 Ejemplos de Reformulaciones

**Caso 1: Pregunta sobre "Prompt"**

*Antes (demasiado técnica):*
```html
<p class="q-block__text">¿Qué nivel de prompting tienes?</p>
```

*Después (más clara):*
```html
<p class="q-block__text">Un <strong>prompt</strong> es lo que le escribes a ChatGPT. ¿Cuál te describe mejor?</p>
<p class="q-block__note">Ejemplo de prompt: "Escribe un correo formal en inglés invitando a estudiantes..."</p>
```

**Caso 2: Pregunta abierta sin ejemplos**

*Antes:*
```html
<textarea placeholder="Escribe libremente…"></textarea>
```

*Después:*
```html
<textarea placeholder="Ej: Automatizar respuestas a preguntas frecuentes sobre fechas de exámenes DELE..."></textarea>
```

### 2.5 Testing de Cambios

**Antes de Producir:**

1. **Test Local:** Abrir `index.html` en navegador
2. **Test Caminos:** Probar cada uno de los 9 caminos
3. **Test Envío:** Enviar formulario de prueba
4. **Test Datos:** Verificar que llega a Formspree

**Script de Test Automatizado:**

```python
# test_formulario.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///ruta/a/index.html")

# Test camino Biblioteca
driver.find_element(By.VALUE, "biblioteca").click()
driver.find_element(By.ID, "btn0Next").click()

# Verificar navegación
assert "Biblioteca" in driver.page_source
assert "section-B1" in driver.page_source

# Test envío (descomentar para producción)
# driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.quit()
print("✅ Test pasado")
```

---

## 3. Creación de Informes Automáticos

### 3.1 Informe Mensual Automático

**Opción A: Script Python + Email**

```python
# informe_mensual.py
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generar_informe(mes, año):
    # Cargar datos
    df = pd.read_json('formspree_export.json')
    
    # Filtrar por mes
    df_mes = df[pd.to_datetime(df['date']).dt.month == mes]
    df_mes = df_mes[df_mes['date'].dt.year == año]
    
    # Métricas
    total_respuestas = len(df_mes)
    por_camino = df_mes['_camino'].value_counts()
    uso_ia = df_mes['uso_ia_alguna_vez'].value_counts(normalize=True) * 100
    
    # Generar HTML
    html = f"""
    <h1>📊 Informe Mensual - Auditoría IA CLM</h1>
    <p><strong>Período:</strong> {mes}/{año}</p>
    <p><strong>Total respuestas:</strong> {total_respuestas}</p>
    
    <h2>Respuestas por Camino</h2>
    {por_camino.to_html()}
    
    <h2>Uso de IA</h2>
    {uso_ia.to_html()}
    """
    
    return html

def enviar_email(html, destinatario):
    msg = MIMEMultipart()
    msg['From'] = 'noreply@clm.ugr.es'
    msg['To'] = destinatario
    msg['Subject'] = f'Informe Mensual - Auditoría IA {datetime.now().strftime("%m/%Y")}'
    
    msg.attach(MIMEText(html, 'html'))
    
    # Enviar (configurar SMTP)
    # smtp.send_message(msg)

if __name__ == '__main__':
    mes = datetime.now().month
    año = datetime.now().year
    
    html = generar_informe(mes, año)
    enviar_email(html, 'direccion@clm.ugr.es')
    
    with open(f'informe_{mes}_{año}.html', 'w') as f:
        f.write(html)
```

**Programar con Cron:**

```bash
# Ejecutar el 1 de cada mes a las 9:00 AM
0 9 1 * * /usr/bin/python3 /ruta/a/informe_mensual.py
```

### 3.2 Dashboard en Tiempo Real

**Opción: Google Looker Studio (Gratis)**

**Pasos:**

1. **Conectar Fuente de Datos:**
   - Crear Google Sheet nuevo
   - En Formspree: Settings → Integrations → Google Sheets
   - Seleccionar el sheet creado

2. **Crear Dashboard en Looker Studio:**
   - https://lookerstudio.google.com
   - Nuevo → Data Source → Google Sheets
   - Seleccionar el sheet

3. **Gráficos Recomendados:**

| Gráfico | Dimensión | Métrica |
|---------|-----------|---------|
| Barras | `_camino` | Count |
| Pie | `uso_ia_alguna_vez` | Count |
| Score Card | Total | Count |
| Heatmap | `_camino` × `nivel_prompt` | Count |

**Actualizar Automáticamente:**
- Looker Studio actualiza cada 15 minutos
- Configurar en Resource → Edit connection → Refresh

### 3.3 Alertas Automáticas

**Alerta cuando hay X respuestas en un camino:**

```python
# alertas.py
import requests

WEBHOOK_URL = "TU_WEBHOOK_SLACK"

def verificar_alertas():
    df = pd.read_json('formspree_export.json')
    
    # Alerta: Más de 10 respuestas en Biblioteca
    biblio_count = len(df[df['_camino'] == 'biblioteca'])
    
    if biblio_count >= 10:
        mensaje = {
            "text": f"📚 {biblio_count} respuestas en Biblioteca. "
                   f"Hora de analizar resultados."
        }
        requests.post(WEBHOOK_URL, json=mensaje)
    
    # Alerta: Más del 30% con riesgos de privacidad
    riesgo_count = df[df['datos_privados'].isin(['Posiblemente', 'Sí'])]
    if len(riesgo_count) / len(df) > 0.3:
        mensaje = {
            "text": f"⚠️ Alerta: {len(riesgo_count)} personas con "
                   f"riesgos de privacidad detectados."
        }
        requests.post(WEBHOOK_URL, json=mensaje)
```

---

## 4. Implementación de Mejoras Adicionales

### 4.1 Mejoras Futuras Sugeridas

**Prioridad ALTA:**

1. **Exportación de Informes PDF**
   - Generar PDF individual por camino
   - Incluir gráficos y recomendaciones
   
   ```python
   # generar_pdf.py
   from reportlab.lib.pagesizes import letter
   from reportlab.pdfgen import canvas
   
   def generar_pdf_camino(camino, datos):
       c = canvas.Canvas(f"informe_{camino}.pdf", pagesize=letter)
       c.drawString(100, 750, f"Informe: {camino}")
       c.drawString(100, 730, f"Total respuestas: {len(datos)}")
       c.save()
   ```

2. **Comparación Temporal**
   - Ver evolución trimestre a trimestre
   - Identificar tendencias de adopción de IA

3. **Benchmarking entre Caminos**
   - Comparar nivel de uso de IA por área
   - Identificar líderes en adopción

**Prioridad MEDIA:**

4. **Análisis de Sentimiento**
   - Detectar preocupaciones en comentarios
   - Clasificar por tipo (técnico, ético, práctico)

5. **Recomendaciones Automáticas**
   - Generar recomendaciones por camino
   - Basadas en gaps identificados

**Prioridad BAJA:**

6. **Integración con Sistemas del CLM**
   - Conectar con base de datos de personal
   - Enviar recordatorios de formación

### 4.2 Añadir Nuevos Caminos

**Si en el futuro hay nuevas áreas:**

```bash
# 1. Copiar estructura de un camino existente
# Por ejemplo, copiar A1-A3 para nuevo camino "Recursos Humanos"

# 2. Modificar secciones
<section-A1> → <section-RH1>
camino-admin → camino-rh
admin_tareas → rh_tareas

# 3. Añadir al objeto CAMINOS
rh: {
  label: 'Recursos Humanos',
  tipo: 'auditoria-rh-clm',
  secciones: ['section-0', 'section-RH1', 'section-RH2', 'section-RH3'],
  tabs: ['Perfil', 'Uso IA', 'Gestión', 'Formación'],
  badge: '📋 4 bloques'
}

# 4. Añadir opción en Sección 0
<label class="area-option">
  <input type="radio" name="area_trabajo" value="rrhh" data-camino="rh">
  ...
</label>

# 5. Añadir CSS
.camino-rh { display: none; }
.camino-rh.active { display: block; }

# 6. Commit y push
git add index.html
git commit -m "feat: añadido camino Recursos Humanos"
git push origin main
```

### 4.3 Integraciones Futuras

**Con Formspree:**

```javascript
// Añadir a index.html
<script>
// Webhook personalizado al enviar
document.getElementById('auditoriaForm').addEventListener('submit', (e) => {
  const camino = document.getElementById('hidden_camino').value;
  
  // Enviar a tu propia API también
  fetch('https://tu-api.com/auditoria', {
    method: 'POST',
    body: JSON.stringify({ camino, timestamp: new Date() })
  });
});
</script>
```

---

## 5. Checklist de Mantenimiento

### Mensual

- [ ] **Revisar métricas clave**
  - Tasa de respuesta por camino
  - Campos con más del 30% vacíos
  - Riesgos de privacidad detectados

- [ ] **Actualizar informes**
  - Generar informe mensual
  - Enviar a dirección
  - Archivar CSV de respuestas

- [ ] **Revisar feedback**
  - Comentarios en campo "observaciones"
  - Emails de consulta
  - Sugerencias del personal

### Trimestral

- [ ] **Análisis profundo por camino**
  - Evolución de uso de IA
  - Cambios en actitudes
  - Necesidades de formación emergentes

- [ ] **Ajustar preguntas**
  - Reformular las problemáticas
  - Añadir nuevas opciones
  - Eliminar las irrelevantes

- [ ] **Actualizar documentación**
  - Este documento
  - README del repositorio
  - Guía de usuario

### Anual

- [ ] **Revisión completa del formulario**
  - ¿Todos los caminos siguen siendo relevantes?
  - ¿Hay nuevas áreas en el CLM?
  - ¿Nuevas herramientas de IA a considerar?

- [ ] **Benchmarking**
  - Comparar con año anterior
  - Identificar tendencias
  - Planificar próximo año

---

## 📞 Soporte

**Repositorio:** https://github.com/elcorreveidile/clm-auditoria-ia  
**Formulario:** https://clm.laclasedigital.com  
**Formspree Dashboard:** https://formspree.io/dashboard

**Para ayuda o consultas:**
- Abrir issue en GitHub
- Revisar commits anteriores para referencia
- Usar este documento como guía

---

**Última actualización:** 15 de abril de 2026  
**Versión del documento:** 1.0
