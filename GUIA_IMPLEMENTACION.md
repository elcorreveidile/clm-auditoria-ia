# 🚀 GUÍA DE IMPLEMENTACIÓN PASO A PASO
## Reestructuración del Formulario de Auditoría IA

---

## 📋 ÍNDICE
1. [Preparación](#1-preparación)
2. [Implementación HTML](#2-implementación-html)
3. [Implementación JavaScript](#3-implementación-javascript)
4. [Testing](#4-testing)
5. [Lanzamiento](#5-lanzamiento)

---

## 1. PREPARACIÓN

### 1.1. Backup del sistema
```bash
# Copia de seguridad del repositorio
cd clm-auditoria-ia
git checkout -b backup-antes-de-cambios
git add .
git commit -m "Backup antes de reestructuración"
git push origin backup-antes-de-cambios
```

### 1.2. Crear rama de trabajo
```bash
# Crear rama para la reestructuración
git checkout -b feature/reestructuracion-7-caminos
```

### 1.3. Requisitos previos
- [ ] Revisar propuesta completa con stakeholders
- [ ] Aprobar estructura de 7 caminos
- [ ] Validar preguntas específicas por área
- [ ] Asignar recursos para implementación
- [ ] Definir timeline del proyecto

---

## 2. IMPLEMENTACIÓN HTML

### 2.1. Actualizar Sección 0 (Selección de área)

**Archivo:** `index.html`
**Ubicación:** Líneas 75-117 (aprox)

**Acción:** Reemplazar el bloque `<div class="area-grid">` con la nueva estructura:

```html
<div class="area-grid" style="margin-top:.75rem">
  <!-- DOCENTE (sin cambios) -->
  <label class="area-option">
    <input type="radio" name="area_trabajo" value="docente-ele" data-camino="docente" required>
    <span class="area-option__icon">🇪🇸</span>
    <span class="area-option__info">
      <span class="area-option__label">Profesorado de ELE</span>
      <span class="area-option__desc">Español como lengua extranjera</span>
    </span>
  </label>

  <!-- ... resto de opciones (ver EJEMPLOS_CODIGO_HTML.md) -->
</div>
```

**Checklist:**
- [ ] Actualizar `data-camino` para cada área
- [ ] Añadir nuevas áreas (marketing, conserjeria, etc.)
- [ ] Mantener consistencia en iconos y descripciones

### 2.2. Crear nuevas secciones por camino

**Orden recomendado de implementación:**

#### Fase 1: Marketing (M1-M3)
```html
<!-- Insertar después de sección A3 (línea 582) -->

<!-- M1: Uso de IA en Marketing -->
<div class="q-section camino-marketing" id="section-M1">
  <!-- (ver EJEMPLOS_CODIGO_HTML.md para código completo) -->
</div>

<!-- M2: Contenido y Redes Sociales -->
<div class="q-section camino-marketing" id="section-M2">
  <!-- ... -->
</div>

<!-- M3: Actitudes y Formación -->
<div class="q-section camino-marketing" id="section-M3">
  <!-- ... -->
</div>
```

**Checklist Marketing:**
- [ ] Crear sección M1 (10 preguntas)
- [ ] Crear sección M2 (4 preguntas)
- [ ] Crear sección M3 (10 preguntas)
- [ ] Validar navegación (prev/next)
- [ ] Probar flujo completo

#### Fase 2: Conserjería (C1-C3)
```html
<!-- Insertar después de sección M3 -->

<!-- C1: Uso real de IA -->
<div class="q-section camino-conserjeria" id="section-C1">
  <!-- ... -->
</div>

<!-- C2: Automatización y Gestión -->
<div class="q-section camino-conserjeria" id="section-C2">
  <!-- ... -->
</div>

<!-- C3: Actitudes y Formación -->
<div class="q-section camino-conserjeria" id="section-C3">
  <!-- ... -->
</div>
```

**Checklist Conserjería:**
- [ ] Crear sección C1 (7 preguntas)
- [ ] Crear sección C2 (4 preguntas)
- [ ] Crear sección C3 (10 preguntas)
- [ ] Validar navegación

#### Fase 3: Diseño (DG1-DG3)
**Checklist Diseño:**
- [ ] Crear sección DG1 (7 preguntas)
- [ ] Crear sección DG2 (4 preguntas)
- [ ] Crear sección DG3 (10 preguntas)

#### Fase 4: Desarrollo (DEV1-DEV3)
**Checklist Desarrollo:**
- [ ] Crear sección DEV1 (7 preguntas)
- [ ] Crear sección DEV2 (4 preguntas)
- [ ] Crear sección DEV3 (10 preguntas)

#### Fase 5: Sistemas (SYS1-SYS3)
**Checklist Sistemas:**
- [ ] Crear sección SYS1 (7 preguntas)
- [ ] Crear sección SYS2 (5 preguntas)
- [ ] Crear sección SYS3 (10 preguntas)

#### Fase 6: Dirección (DIR1-DIR3)
**Checklist Dirección:**
- [ ] Crear sección DIR1 (6 preguntas)
- [ ] Crear sección DIR2 (5 preguntas)
- [ ] Crear sección DIR3 (10 preguntas)

### 2.3. Actualizar referencias a caminos técnicos existentes

**Buscar y reemplazar en todo el archivo:**

**ANTES:**
```html
<div class="q-section camino-tecnico" id="section-T1">
```

**DESPUÉS:**
```html
<!-- Para diseño -->
<div class="q-section camino-disenyo" id="section-DG1">

<!-- Para desarrollo -->
<div class="q-section camino-desarrollo" id="section-DEV1">

<!-- Para sistemas -->
<div class="q-section camino-sistemas" id="section-SYS1">
```

**Acción:**
```bash
# Buscar secciones técnicas antiguas
grep -n "camino-tecnico" index.html

# Reemplazar según corresponda
# Mantener T1-T3 solo como referencia temporal
```

---

## 3. IMPLEMENTACIÓN JAVASCRIPT

### 3.1. Actualizar objeto CAMINOS

**Archivo:** `index.html`
**Ubicación:** Líneas 797-819 (script al final del archivo)

**Reemplazar completamente:**

```javascript
const CAMINOS = {
  docente: {
    label: 'Profesorado',
    tipo: 'auditoria-docentes-clm',
    secciones: ['section-0', 'section-D1', 'section-D2', 'section-D3', 'section-D4'],
    tabs: ['Perfil', 'Uso IA', 'IA en el aula', 'Automatización', 'Actitudes'],
    badge: '📋 5 bloques'
  },
  admin: {
    label: 'Administración y Gestión',
    tipo: 'auditoria-admin-clm',
    secciones: ['section-0', 'section-A1', 'section-A2', 'section-A3'],
    tabs: ['Perfil', 'Uso IA', 'Atención al estudiante', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  marketing: {
    label: 'Marketing y Comunicación',
    tipo: 'auditoria-marketing-clm',
    secciones: ['section-0', 'section-M1', 'section-M2', 'section-M3'],
    tabs: ['Perfil', 'Uso IA en Marketing', 'Contenido y Redes', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  conserjeria: {
    label: 'Conserjería y Mantenimiento',
    tipo: 'auditoria-conserjeria-clm',
    secciones: ['section-0', 'section-C1', 'section-C2', 'section-C3'],
    tabs: ['Perfil', 'Uso IA', 'Automatización', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  disenyo: {
    label: 'Diseño Gráfico y Audiovisual',
    tipo: 'auditoria-disenyo-clm',
    secciones: ['section-0', 'section-DG1', 'section-DG2', 'section-DG3'],
    tabs: ['Perfil', 'Uso IA en Diseño', 'Proyectos Creativos', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  desarrollo: {
    label: 'Programación y Desarrollo',
    tipo: 'auditoria-desarrollo-clm',
    secciones: ['section-0', 'section-DEV1', 'section-DEV2', 'section-DEV3'],
    tabs: ['Perfil', 'Uso IA en Desarrollo', 'Proyectos', 'Visión Estratégica'],
    badge: '📋 4 bloques'
  },
  sistemas: {
    label: 'Sistemas y Seguridad Informática',
    tipo: 'auditoria-sistemas-clm',
    secciones: ['section-0', 'section-SYS1', 'section-SYS2', 'section-SYS3'],
    tabs: ['Perfil', 'Uso IA en Sistemas', 'Infraestructura', 'Visión Estratégica'],
    badge: '📋 4 bloques'
  },
  direccion: {
    label: 'Dirección y Subdirecciones',
    tipo: 'auditoria-direccion-clm',
    secciones: ['section-0', 'section-DIR1', 'section-DIR2', 'section-DIR3'],
    tabs: ['Perfil', 'Visión Estratégica', 'Gestión', 'Política Institucional'],
    badge: '📋 4 bloques'
  }
};
```

### 3.2. Añadir clases CSS para nuevos caminos

**Archivo:** `css/style.css` (o `<style>` en HTML)

**Añadir al final:**

```css
/* Nuevos caminos */
.camino-marketing,
.camino-conserjeria,
.camino-disenyo,
.camino-desarrollo,
.camino-sistemas,
.camino-direccion {
  display: none;
}

/* Mostrar cuando está activo */
.camino-marketing.active,
.camino-conserjeria.active,
.camino-disenyo.active,
.camino-desarrollo.active,
.camino-sistemas.active,
.camino-direccion.active {
  display: block;
}
```

### 3.3. Validar lógica de navegación

**No requiere cambios** - la lógica existente funciona automáticamente con los nuevos caminos:

```javascript
// Este código ya existe y funciona con nuevos caminos
document.getElementById('btn0Next').addEventListener('click', () => {
  const radio = document.querySelector('input[name="area_trabajo"]:checked');
  const camino = radio.dataset.camino; // Obtiene el camino del data-camino
  // ... resto de la lógica
});
```

**Checklist JavaScript:**
- [ ] Actualizar objeto CAMINOS
- [ ] Añadir clases CSS
- [ ] Validar que data-camino coincide con claves del objeto
- [ ] Probar navegación para cada camino

---

## 4. TESTING

### 4.1. Testing manual por camino

**Crear spreadsheet de testing:**

| Camino | Secciones | Preguntas | Navegación | Envío | Observaciones |
|--------|-----------|-----------|------------|-------|---------------|
| docente | 5 | 25 | ✅ | ✅ | - |
| admin | 3 | 18 | ✅ | ✅ | - |
| marketing | 3 | 24 | ⏳ | ⏳ | Pendiente |
| conserjeria | 3 | 21 | ⏳ | ⏳ | Pendiente |
| disenyo | 3 | 21 | ⏳ | ⏳ | Pendiente |
| desarrollo | 3 | 21 | ⏳ | ⏳ | Pendiente |
| sistemas | 3 | 22 | ⏳ | ⏳ | Pendiente |
| direccion | 3 | 21 | ⏳ | ⏳ | Pendiente |

### 4.2. Casos de prueba

**Para cada camino, probar:**

1. **Selección de área**
   - [ ] Icono correcto
   - [ ] Descripción clara
   - [ ] data-camino válido

2. **Navegación**
   - [ ] Tabs se generan correctamente
   - [ ] Progreso se actualiza
   - [ ] Botón anterior funciona
   - [ ] Botón siguiente funciona
   - [ ] No se puede saltar secciones

3. **Preguntas**
   - [ ] Todas las preguntas se muestran
   - [ ] Opciones de respuesta son correctas
   - [ ] Campos de texto funcionan
   - [ ] Likert scales funcionan
   - [ ] Checkboxes funcionan

4. **Validación**
   - [ ] Preguntas obligatorias se validan
   - [ ] No se puede avanzar sin responder
   - [ ] Mensajes de error son claros

5. **Envío**
   - [ ] Botón de enviar aparece en última sección
   - [ ] Formulario se envía correctamente
   - [ ] Pantalla de gracias se muestra

### 4.3. Testing responsive

**Probar en:**
- [ ] Desktop (1920x1080)
- [ ] Tablet (768x1024)
- [ ] Móvil (375x667)
- [ ] Navegadores: Chrome, Firefox, Safari, Edge

### 4.4. Testing de integración

**Verificar:**
- [ ] Formspree recibe datos correctamente
- [ ] Email de confirmación se envía
- [ ] Datos se almacenan con el tipo correcto
- [ ] No hay errores en consola del navegador

---

## 5. LANZAMIENTO

### 5.1. Pre-lanzamiento

**Semana 1: Preparación**
- [ ] Completar todas las implementaciones
- [ ] Pasar todos los tests
- [ ] Hacer deployment a staging
- [ ] Testing final con usuarios piloto

**Semana 2: Comunicación**
- [ ] Preparar anuncio para toda la plantilla
- [ ] Crear guía rápida para usuarios
- [ ] Preparar email de lanzamiento
- [ ] Programar recordatorios

### 5.2. Deployment

**Opción A: GitHub Pages (recomendado para este proyecto)**
```bash
# Commit de todos los cambios
git add .
git commit -m "feat: reestructuración a 7 caminos específicos

- Añadidos caminos: marketing, conserjeria, disenyo, desarrollo, sistemas, direccion
- Actualizada Sección 0 con nuevas áreas
- Creadas 18 secciones nuevas (3 por camino)
- Actualizado objeto CAMINOS en JavaScript
- Añadidas clases CSS para nuevos caminos

Closes #[issue-number]"

# Push a main
git push origin feature/reestructuracion-7-caminos

# Crear Pull Request
gh pr create --title "Reestructuración a 7 caminos" --body "$(cat RESUMEN_EJECUTIVO.md)"
```

**Opción B: Deployment manual**
```bash
# Subir archivos por FTP/SFTP al servidor
# O usar panel de control del hosting
```

### 5.3. Post-lanzamiento

**Día 1: Monitorización**
- [ ] Verificar que el formulario funciona
- [ ] Comprobar que se reciben respuestas
- [ ] Revisar errores en logs (si disponibles)
- [ ] Estar atento a feedback de usuarios

**Semana 1: Seguimiento**
- [ ] Revisar tasa de respuesta
- [ ] Analizar primeras respuestas
- [ ] Recoger feedback informal
- [ ] Documentar problemas si los hay

**Semana 2-4: Evaluación**
- [ ] Análisis de datos por camino
- [ ] Comparación con datos anteriores (si existen)
- [ ] Informe preliminar de resultados
- [ ] Ajustes si son necesarios

### 5.4. Comunicación del lanzamiento

**Email plantilla:**

```
Asunto: 📋 Nueva Auditoría IA del CLM - Tu opinión es importante

Estimado/a compañeros/as,

Desde el Centro de Lenguas Modernas estamos llevando a cabo una
auditoría de necesidades de inteligencia artificial.

Hemos mejorado el formulario para que sea específico por área de trabajo.
Ahora hay 7 caminos diferentes adaptados a cada perfil:

✅ Profesorado (ELE y Lenguas Modernas)
✅ Administración y Gestión
✅ Marketing y Comunicación
✅ Conserjería y Mantenimiento
✅ Diseño Gráfico y Audiovisual
✅ Programación y Desarrollo
✅ Sistemas y Seguridad Informática
✅ Dirección y Subdirecciones

🔗 ENLACE: [URL del formulario]

Características:
• Anónimo y confidencial
• 15-20 minutos de duración
• Adaptado a tu área específica
• Disponible hasta el [FECHA]

Tu participación es fundamental para diseñar un plan de implantación
de IA ajustado a la realidad de nuestra institución.

Muchas gracias por tu colaboración.

El equipo de Dirección del CLM
```

---

## 📊 MÉTRICAS DE ÉXITO

### Objetivos del lanzamiento

| Métrica | Objetivo | Cómo medir |
|---------|----------|------------|
| Tasa de respuesta | >60% de plantilla | Formspree analytics |
| Tiempo de completado | <20 min media | Timestamp en respuestas |
| Satisfacción | >4/5 stars | Encuesta post-formulario |
| Datos accionables | >90% relevantes | Análisis de respuestas |

### KPIs a monitorizar

- **Respuestas por camino**: Objetivo mínimo 5 respuestas/camino
- **Tasa de abandono**: <20% en primera sección
- **Tiempo por sección**: <5 min media
- **Calidad de respuestas abiertas**: >80% con texto sustancial

---

## 🐥 SOLUCIÓN DE PROBLEMAS

### Problemas comunes y soluciones

**Problema 1: Sección no se muestra**
```javascript
// Verificar en consola
console.log(document.querySelector('input[name="area_trabajo"]:checked'));
console.log(document.querySelector('input[name="area_trabajo"]:checked").dataset.camino);

// Debe coincidir con clave en CAMINOS
```

**Problema 2: Navegación no avanza**
```javascript
// Verificar que data-next apunta a ID correcto
<button data-next="section-M2">Siguiente →</button>
<!-- Debe existir un elemento con id="section-M2" -->
```

**Problema 3: CSS no aplica**
```css
/* Verificar que clases están definidas */
.camino-marketing { display: none; }
.camino-marketing.active { display: block; }
```

**Problema 4: Form no envía**
```javascript
// Verificar que action URL es correcta
<form action="https://formspree.io/f/mjgalypd" method="POST">
```

---

## 📞 SOPORTE

**Durante el lanzamiento:**
- Email de soporte: [email protegido]
- Canal de Slack: #auditoria-ia
- Horario de respuesta: <24h laborables

**Recursos:**
- Guía rápida para usuarios: [ENLACE]
- Preguntas frecuentes: [ENLACE]
- Video tutorial: [ENLACE] (opcional)

---

## ✅ CHECKLIST FINAL

**Antes del lanzamiento:**
- [ ] Todos los caminos implementados
- [ ] Testing completado para todos los caminos
- [ ] Deployment a producción exitoso
- [ ] Email de lanzamiento preparado
- [ ] Canales de soporte configurados

**Después del lanzamiento:**
- [ ] Primer día sin incidentes críticos
- [ ] 10+ respuestas recibidas
- [ ] Feedback positivo de usuarios
- [ ] Métricas dentro de objetivos

---

**Versión:** 1.0
**Fecha:** 15 de abril de 2026
**Responsable:** [Tu nombre]
**Aprobado por:** [Dirección CLM]
