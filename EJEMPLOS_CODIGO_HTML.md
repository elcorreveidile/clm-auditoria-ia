# 💻 EJEMPLOS DE CÓDIGO HTML
## Nuevas secciones para implementar

---

## 📣 EJEMPLO 1: MARKETING - Sección M2

```html
<!-- ══════════════════════════════════════════
     CAMINO MARKETING: M2 - CONTENIDO Y REDES
══════════════════════════════════════════ -->
<div class="q-section camino-marketing" id="section-M2">
  <div class="q-section__header">
    <div class="q-section__letter q-section__letter--C">3</div>
    <div class="q-section__info">
      <p class="q-section__name">Contenido y Redes Sociales</p>
      <p class="q-section__desc">Cómo la IA puede transformar tu trabajo de marketing</p>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 8 · Clave</p>
    <p class="q-block__text">¿Para qué tareas usas o usarías IA en marketing?</p>
    <p class="q-block__note">Marca todas las que apliquen</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Redacción">
        <span class="q-option__box"></span>
        <span class="q-option__label">Redacción de posts y copy</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Imágenes">
        <span class="q-option__box"></span>
        <span class="q-option__label">Generación de imágenes y gráficos</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Vídeo">
        <span class="q-option__box"></span>
        <span class="q-option__label">Creación de vídeos y reels</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Métricas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Análisis de métricas y engagement</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Programación">
        <span class="q-option__box"></span>
        <span class="q-option__label">Programación automática de contenido</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Respuestas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Respuesta a comentarios y mensajes</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Ideas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Generación de ideas para campañas</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Traducción">
        <span class="q-option__box"></span>
        <span class="q-option__label">Traducción de contenido</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="Newsletter">
        <span class="q-option__box"></span>
        <span class="q-option__label">Creación de newsletters</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="mkt_tareas" value="SEO">
        <span class="q-option__box"></span>
        <span class="q-option__label">Optimización SEO para web</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 9</p>
    <p class="q-block__text">¿Qué porcentaje de tu trabajo de contenido crees que podría automatizarse con IA?</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="mkt_automatizable" value="<20%">
        <span class="q-option__box"></span>
        <span class="q-option__label">Menos del 20% - Requiere mucha creatividad humana</span>
      </label>
      <label class="q-option">
        <input type="radio" name="mkt_automatizable" value="20-40%">
        <span class="q-option__box"></span>
        <span class="q-option__label">Entre 20-40% - Tareas de soporte</span>
      </label>
      <label class="q-option">
        <input type="radio" name="mkt_automatizable" value="40-60%">
        <span class="q-option__box"></span>
        <span class="q-option__label">Entre 40-60% - Bastantes tareas repetitivas</span>
      </label>
      <label class="q-option">
        <input type="radio" name="mkt_automatizable" value=">60%">
        <span class="q-option__box"></span>
        <span class="q-option__label">Más del 60% - Gran parte es producción estandarizada</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 10 · Agentes de IA</p>
    <p class="q-block__text">Imagina un agente de IA que responde automáticamente comentarios en redes sociales, analiza métricas y te genera reportes. ¿Cómo lo valorarías?</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="mkt_agente" value="Muy positivo">
        <span class="q-option__box"></span>
        <span class="q-option__label">Muy positivo: me liberaría de tareas repetitivas</span>
      </label>
      <label class="q-option">
        <input type="radio" name="mkt_agente" value="Positivo con reservas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Positivo, pero me preocupa que dé respuestas incorrectas</span>
      </label>
      <label class="q-option">
        <input type="radio" name="mkt_agente" value="Neutro">
        <span class="q-option__box"></span>
        <span class="q-option__label">Neutro: no veo claramente la ventaja</span>
      </label>
      <label class="q-option">
        <input type="radio" name="mkt_agente" value="Negativo">
        <span class="q-option__box"></span>
        <span class="q-option__label">Negativo: nuestros seguidores necesitan atención humana</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 11 · Abierta</p>
    <p class="q-block__text">¿Qué tarea concreta de tu trabajo diario te gustaría que se pudiera automatizar con IA?</p>
    <textarea class="q-open" name="mkt_tarea_automatizar" placeholder="Ej: Generar reportes semanales de engagement de todas las redes..." rows="3"></textarea>
  </div>

  <div class="q-nav">
    <button type="button" class="btn btn--outline" data-prev="section-M1">← Anterior</button>
    <span class="q-nav__info"></span>
    <button type="button" class="btn btn--primary" data-next="section-M3">Siguiente →</button>
  </div>
</div>
```

---

## 🔑 EJEMPLO 2: CONSERJERÍA - Sección C1

```html
<!-- ══════════════════════════════════════════
     CAMINO CONSERJERÍA: C1 - USO REAL DE IA
══════════════════════════════════════════ -->
<div class="q-section camino-conserjeria" id="section-C1">
  <div class="q-section__header">
    <div class="q-section__letter q-section__letter--B">2</div>
    <div class="q-section__info">
      <p class="q-section__name">Tu uso real de la IA</p>
      <p class="q-section__desc">Qué has probado ya, sin tecnicismos</p>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 3</p>
    <p class="q-block__text">¿Qué tareas realizas principalmente en tu trabajo en el CLM?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Atención">
        <span class="q-option__box"></span>
        <span class="q-option__label">Atención presencial en conserjería</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Eléctrico">
        <span class="q-option__box"></span>
        <span class="q-option__label">Mantenimiento eléctrico</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Climatización">
        <span class="q-option__box"></span>
        <span class="q-option__label">Mantenimiento de climatización</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Fontanería">
        <span class="q-option__box"></span>
        <span class="q-option__label">Mantenimiento de fontanería / agua</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Jardinería">
        <span class="q-option__box"></span>
        <span class="q-option__label">Jardinería</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Albañilería">
        <span class="q-option__box"></span>
        <span class="q-option__label">Albañilería, pintura y carpintería</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Coordinación">
        <span class="q-option__box"></span>
        <span class="q-option__label">Coordinación de equipos de mantenimiento</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="cons_tareas" value="Llaves">
        <span class="q-option__box"></span>
        <span class="q-option__label">Gestión de llaves y espacios</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 4</p>
    <p class="q-block__text">¿Has usado alguna vez herramientas de IA, aunque sea en el ámbito personal?</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="cons_uso_ia" value="No nunca">
        <span class="q-option__box"></span>
        <span class="q-option__label">No, nunca</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_uso_ia" value="Sí personal">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sí, pero solo en el ámbito personal</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_uso_ia" value="Sí trabajo ocasional">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sí, alguna vez en el trabajo para algo concreto</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_uso_ia" value="Sí trabajo habitual">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sí, la uso con regularidad en mi trabajo</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 5 · Clave</p>
    <p class="q-block__text">Si has usado IA en el trabajo, ¿para qué fue exactamente?</p>
    <p class="q-block__note">Si nunca la has usado, escribe "nunca"</p>
    <textarea class="q-open" name="cons_uso_concreto" placeholder="Ej: Usé ChatGPT para redactar un parte de incidencia..." rows="3"></textarea>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 6 · Discriminante</p>
    <p class="q-block__text">¿Qué nivel de competencia digital tienes?</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="cons_nivel_digital" value="Básico">
        <span class="q-option__box"></span>
        <span class="q-option__label">Básico: uso email y WhatsApp, poco más</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_nivel_digital" value="Intermedio">
        <span class="q-option__box"></span>
        <span class="q-option__label">Intermedio: uso oficimática, busco información en internet</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_nivel_digital" value="Avanzado">
        <span class="q-option__box"></span>
        <span class="q-option__label">Avanzado: uso aplicaciones específicas de mi área</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_nivel_digital" value="Experto">
        <span class="q-option__box"></span>
        <span class="q-option__label">Experto: manejo varios tipos de software y aplicaciones técnicas</span>
      </label>
    </div>
  </div>

  <div class="q-block" style="border:2px solid #D9534F;background:#FDF2F2">
    <p class="q-block__num" style="color:#D9534F">Pregunta 7 · Privacidad</p>
    <p class="q-block__text" style="font-weight:600">¿Has introducido datos de estudiantes o incidentes en herramientas de IA?</p>
    <p class="q-block__note">Anónima. Objetivo: detectar riesgos de privacidad.</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="cons_datos_privados" value="No">
        <span class="q-option__box"></span>
        <span class="q-option__label">No, nunca.</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_datos_privados" value="Posiblemente">
        <span class="q-option__box"></span>
        <span class="q-option__label">Posiblemente sí, sin ser consciente.</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_datos_privados" value="Sí">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sí, para agilizar algún gestor o reporte.</span>
      </label>
      <label class="q-option">
        <input type="radio" name="cons_datos_privados" value="No sé">
        <span class="q-option__box"></span>
        <span class="q-option__label">No sé qué se considera dato personal.</span>
      </label>
    </div>
  </div>

  <div class="q-nav">
    <button type="button" class="btn btn--outline" data-prev="section-0">← Anterior</button>
    <span class="q-nav__info"></span>
    <button type="button" class="btn btn--primary" data-next="section-C2">Siguiente →</button>
  </div>
</div>
```

---

## 💻 EJEMPLO 3: SISTEMAS - Sección SYS2 (Infraestructura y Seguridad)

```html
<!-- ══════════════════════════════════════════
     CAMINO SISTEMAS: SYS2 - INFRAESTRUCTURA
══════════════════════════════════════════ -->
<div class="q-section camino-sistemas" id="section-SYS2">
  <div class="q-section__header">
    <div class="q-section__letter q-section__letter--C">3</div>
    <div class="q-section__info">
      <p class="q-section__name">Infraestructura y Seguridad</p>
      <p class="q-section__desc">Lo que existe hoy y lo que falta para implantar IA</p>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 8</p>
    <p class="q-block__text">¿Qué infraestructura de sistemas existe en el CLM?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="On-premise">
        <span class="q-option__box"></span>
        <span class="q-option__label">Servidores on-premise</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="Cloud">
        <span class="q-option__box"></span>
        <span class="q-option__label">Servicios en la nube</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="Incidencias">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sistema de gestión de incidencias</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="Monitorización">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sistema de monitorización</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="Backups">
        <span class="q-option__box"></span>
        <span class="q-option__label">Backups y Disaster Recovery</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="VPN">
        <span class="q-option__box"></span>
        <span class="q-option__label">VPN y acceso remoto</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_infra" value="No lo sé">
        <span class="q-option__box"></span>
        <span class="q-option__label">No lo sé con certeza</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 9</p>
    <p class="q-block__text">¿Qué falta en el CLM para implantar soluciones con IA?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_falta" value="Servidores IA">
        <span class="q-option__box"></span>
        <span class="q-option__label">Infraestructura de servidores para IA</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_falta" value="Conectividad">
        <span class="q-option__box"></span>
        <span class="q-option__label">Conectividad y ancho de banda suficiente</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_falta" value="Política ENS">
        <span class="q-option__box"></span>
        <span class="q-option__label">Políticas de seguridad y privacidad (ENS)</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_falta" value="Personal">
        <span class="q-option__box"></span>
        <span class="q-option__label">Personal formado en IA aplicada a sistemas</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_falta" value="Presupuesto">
        <span class="q-option__box"></span>
        <span class="q-option__label">Presupuesto para herramientas y servicios</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_falta" value="Nada">
        <span class="q-option__box"></span>
        <span class="q-option__label">No falta nada, se podría implantar ya</span>
      </label>
    </div>
  </div>

  <div class="q-block" style="border:2px solid #D9534F;background:#FDF2F2">
    <p class="q-block__num" style="color:#D9534F">Pregunta 10 · Riesgos específicos</p>
    <p class="q-block__text" style="font-weight:600">¿Qué riesgos específicos de seguridad ves en el uso de IA en el CLM?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="Fuga datos">
        <span class="q-option__box"></span>
        <span class="q-option__label">Fuga de datos personales de estudiantes</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="ENS">
        <span class="q-option__box"></span>
        <span class="q-option__label">Incumplimiento del ENS</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="Ingeniería social">
        <span class="q-option__box"></span>
        <span class="q-option__label">Ataques mediante ingeniería social con IA</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="Proveedores">
        <span class="q-option__box"></span>
        <span class="q-option__label">Dependencia de proveedores externos</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="Pérdida control">
        <span class="q-option__box"></span>
        <span class="q-option__label">Pérdida de control sobre datos sensibles</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="Uso no autorizado">
        <span class="q-option__box"></span>
        <span class="q-option__label">Uso no autorizado por personal</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="sys_riesgos" value="Respuestas incorrectas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Respuestas incorrectas en decisiones críticas</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 11</p>
    <p class="q-block__text">¿Tiene el CLM actualmente algún sistema para atención al estudiante?</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="sys_crm" value="Sí consolidado">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sí, un sistema consolidado (CRM, helpdesk)</span>
      </label>
      <label class="q-option">
        <input type="radio" name="sys_crm" value="Sí parcial">
        <span class="q-option__box"></span>
        <span class="q-option__label">Sí, pero parcial o poco utilizado</span>
      </label>
      <label class="q-option">
        <input type="radio" name="sys_crm" value="No manual">
        <span class="q-option__box"></span>
        <span class="q-option__label">No, todo es manual (email, teléfono)</span>
      </label>
      <label class="q-option">
        <input type="radio" name="sys_crm" value="No lo sé">
        <span class="q-option__box"></span>
        <span class="q-option__label">No lo sé con certeza</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 12 · Abierta</p>
    <p class="q-block__text">¿Qué proceso técnico del CLM podría automatizarse con IA con más impacto y menos riesgo?</p>
    <textarea class="q-open" name="sys_proceso_automatizable" placeholder="Ej: Clasificación automática de tickets de incidencias..." rows="4"></textarea>
  </div>

  <div class="q-nav">
    <button type="button" class="btn btn--outline" data-prev="section-SYS1">← Anterior</button>
    <span class="q-nav__info"></span>
    <button type="button" class="btn btn--primary" data-next="section-SYS3">Siguiente →</button>
  </div>
</div>
```

---

## 🎯 EJEMPLO 4: DIRECCIÓN - Sección DIR2 (Gestión y Toma de Decisiones)

```html
<!-- ══════════════════════════════════════════
     CAMINO DIRECCIÓN: DIR2 - GESTIÓN Y DECISIONES
══════════════════════════════════════════ -->
<div class="q-section camino-direccion" id="section-DIR2">
  <div class="q-section__header">
    <div class="q-section__letter q-section__letter--C">3</div>
    <div class="q-section__info">
      <p class="q-section__name">Gestión y Toma de Decisiones</p>
      <p class="q-section__desc">Cómo la IA puede apoyar la dirección del CLM</p>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 7 · Clave</p>
    <p class="q-block__text">¿En qué decisiones del CLM crees que la IA podría aportar más valor?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Matrícula">
        <span class="q-option__box"></span>
        <span class="q-option__label">Previsión de matrícula y demanda</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Recursos">
        <span class="q-option__box"></span>
        <span class="q-option__label">Optimización de aulas y profesores</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Satisfacción">
        <span class="q-option__box"></span>
        <span class="q-option__label">Análisis de satisfacción</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Problemas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Detección temprana de problemas</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Informes">
        <span class="q-option__box"></span>
        <span class="q-option__label">Automatización de informes</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Comunicación">
        <span class="q-option__box"></span>
        <span class="q-option__label">Personalización de comunicación</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_decisiones" value="Todas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Todas podrían beneficiarse</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 8 · Diagnóstico</p>
    <p class="q-block__text">¿Qué datos tiene actualmente el CLM para análisis?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="Matrículas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Matrículas históricas</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="Calificaciones">
        <span class="q-option__box"></span>
        <span class="q-option__label">Calificaciones y resultados</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="Encuestas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Encuestas de satisfacción</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="Uso plataformas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Datos de uso (Moodle, web)</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="Atención">
        <span class="q-option__box"></span>
        <span class="q-option__label">Datos de atención al estudiante</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="No claro">
        <span class="q-option__box"></span>
        <span class="q-option__label">No tengo claro qué datos hay</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_datos" value="No estructurados">
        <span class="q-option__box"></span>
        <span class="q-option__label">No hay datos estructurados</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 9 · Barreras</p>
    <p class="q-block__text">¿Qué barreras ves para la toma de decisiones basada en datos en el CLM?</p>
    <div class="q-options q-options--grid">
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_barreras" value="Dispersos">
        <span class="q-option__box"></span>
        <span class="q-option__label">Datos dispersos en diferentes sistemas</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_barreras" value="Personal">
        <span class="q-option__box"></span>
        <span class="q-option__label">No hay personal para analizar</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_barreras" value="Cultura">
        <span class="q-option__box"></span>
        <span class="q-option__label">No hay cultura de datos</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_barreras" value="RGPD">
        <span class="q-option__box"></span>
        <span class="q-option__label">Preocupaciones de privacidad y RGPD</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_barreras" value="Herramientas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Falta de herramientas</span>
      </label>
      <label class="q-option q-option--check">
        <input type="checkbox" name="dir_barreras" value="Prioridad">
        <span class="q-option__box"></span>
        <span class="q-option__label">No lo veo como prioridad</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 10 · Agentes de IA</p>
    <p class="q-block__text">¿Cómo valorarías un agente de IA que analiza datos del CLM y genera recomendaciones?</p>
    <div class="q-options">
      <label class="q-option">
        <input type="radio" name="dir_agente" value="Muy positivo">
        <span class="q-option__box"></span>
        <span class="q-option__label">Muy positivo: mejoraría la toma de decisiones</span>
      </label>
      <label class="q-option">
        <input type="radio" name="dir_agente" value="Positivo con reservas">
        <span class="q-option__box"></span>
        <span class="q-option__label">Positivo, pero necesito entender el razonamiento</span>
      </label>
      <label class="q-option">
        <input type="radio" name="dir_agente" value="Neutro">
        <span class="q-option__box"></span>
        <span class="q-option__label">Neutro: no veo claro el valor añadido</span>
      </label>
      <label class="q-option">
        <input type="radio" name="dir_agente" value="Negativo">
        <span class="q-option__box"></span>
        <span class="q-option__label">Negativo: prefiero decisiones basadas en criterio humano</span>
      </label>
      <label class="q-option">
        <input type="radio" name="dir_agente" value="No aplicable">
        <span class="q-option__box"></span>
        <span class="q-option__label">No lo veo aplicable en nuestra realidad</span>
      </label>
    </div>
  </div>

  <div class="q-block">
    <p class="q-block__num">Pregunta 11 · Abierta</p>
    <p class="q-block__text">¿Qué proceso de gestión te gustaría que la IA pudiera asesorar?</p>
    <textarea class="q-open" name="dir_proceso_asesorar" placeholder="Ej: Asignación optimizada de aulas considerando preferencias..." rows="3"></textarea>
  </div>

  <div class="q-nav">
    <button type="button" class="btn btn--outline" data-prev="section-DIR1">← Anterior</button>
    <span class="q-nav__info"></span>
    <button type="button" class="btn btn--primary" data-next="section-DIR3">Siguiente →</button>
  </div>
</div>
```

---

## 🔄 EJEMPLO 5: Actualización de Sección 0 (Selección de área)

```html
<!-- ══════════════════════════════════════════
     SECCIÓN 0: SELECCIÓN DE PERFIL (ACTUALIZADA)
══════════════════════════════════════════ -->
<div class="q-section active" id="section-0">
  <div class="q-section__header">
    <div class="q-section__letter q-section__letter--A">1</div>
    <div class="q-section__info">
      <p class="q-section__name">Tu perfil en el CLM</p>
      <p class="q-section__desc">Esta selección adapta todo el cuestionario a tu área de trabajo</p>
    </div>
  </div>

  <div class="q-block" style="border:2px solid var(--clm-red);background:var(--clm-red-light)">
    <p class="q-block__num" style="color:var(--clm-red)">Pregunta 1 · Obligatoria</p>
    <p class="q-block__text" style="font-weight:600">¿En qué área trabajas en el CLM?</p>
    <p class="q-block__note">Tu respuesta determina las preguntas que verás a continuación.</p>
    <div class="area-grid" style="margin-top:.75rem">

      <!-- CAMINO DOCENTE -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="docente-ele" data-camino="docente" required>
        <span class="area-option__icon">🇪🇸</span>
        <span class="area-option__info">
          <span class="area-option__label">Profesorado de ELE</span>
          <span class="area-option__desc">Español como lengua extranjera</span>
        </span>
      </label>

      <label class="area-option">
        <input type="radio" name="area_trabajo" value="docente-lm" data-camino="docente">
        <span class="area-option__icon">🌍</span>
        <span class="area-option__info">
          <span class="area-option__label">Profesorado de Lenguas Modernas</span>
          <span class="area-option__desc">Inglés, francés, alemán, italiano y otras</span>
        </span>
      </label>

      <!-- CAMINO ADMINISTRACIÓN -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="administracion" data-camino="admin">
        <span class="area-option__icon">📋</span>
        <span class="area-option__info">
          <span class="area-option__label">Administración y Gestión</span>
          <span class="area-option__desc">Matrículas, Study Abroad, contabilidad</span>
        </span>
      </label>

      <!-- CAMINO MARKETING ✨ NUEVO -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="marketing" data-camino="marketing">
        <span class="area-option__icon">📣</span>
        <span class="area-option__info">
          <span class="area-option__label">Marketing y Comunicación</span>
          <span class="area-option__desc">Redes sociales, contenidos, promoción</span>
        </span>
      </label>

      <!-- CAMINO CONSERJERÍA ✨ NUEVO -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="conserjeria" data-camino="conserjeria">
        <span class="area-option__icon">🔑</span>
        <span class="area-option__info">
          <span class="area-option__label">Conserjería y Mantenimiento</span>
          <span class="area-option__desc">Atención presencial, mantenimiento</span>
        </span>
      </label>

      <!-- CAMINO DISEÑO ✨ NUEVO -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="diseno" data-camino="disenyo">
        <span class="area-option__icon">🎨</span>
        <span class="area-option__info">
          <span class="area-option__label">Diseño Gráfico y Audiovisual</span>
          <span class="area-option__desc">Diseño gráfico, producción web y audiovisual</span>
        </span>
      </label>

      <!-- CAMINO PROGRAMACIÓN ✨ NUEVO -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="programacion" data-camino="desarrollo">
        <span class="area-option__icon">⌨️</span>
        <span class="area-option__info">
          <span class="area-option__label">Programación y Desarrollo</span>
          <span class="area-option__desc">Desarrollo de software y plataformas</span>
        </span>
      </label>

      <!-- CAMINO SISTEMAS ✨ NUEVO -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="informatica" data-camino="sistemas">
        <span class="area-option__icon">💻</span>
        <span class="area-option__info">
          <span class="area-option__label">Sistemas y Seguridad Informática</span>
          <span class="area-option__desc">Sistemas, infraestructura, seguridad, ENS</span>
        </span>
      </label>

      <!-- BIBLIOTECA -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="biblioteca" data-camino="disenyo">
        <span class="area-option__icon">📚</span>
        <span class="area-option__info">
          <span class="area-option__label">Biblioteca</span>
          <span class="area-option__desc">Gestión de fondos y servicios</span>
        </span>
      </label>

      <!-- CAMINO DIRECCIÓN ✨ NUEVO -->
      <label class="area-option">
        <input type="radio" name="area_trabajo" value="direccion" data-camino="direccion">
        <span class="area-option__icon">🎯</span>
        <span class="area-option__info">
          <span class="area-option__label">Dirección y Subdirecciones</span>
          <span class="area-option__desc">Dirección, gerencia y estrategia</span>
        </span>
      </label>

    </div>
  </div>

  <!-- ... resto de la sección ... -->
</div>
```

---

## 📋 EJEMPLO 6: Actualización de JavaScript (CAMINOS)

```javascript
// Configuración de caminos actualizada
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
  marketing: { // ✨ NUEVO
    label: 'Marketing y Comunicación',
    tipo: 'auditoria-marketing-clm',
    secciones: ['section-0', 'section-M1', 'section-M2', 'section-M3'],
    tabs: ['Perfil', 'Uso IA en Marketing', 'Contenido y Redes', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  conserjeria: { // ✨ NUEVO
    label: 'Conserjería y Mantenimiento',
    tipo: 'auditoria-conserjeria-clm',
    secciones: ['section-0', 'section-C1', 'section-C2', 'section-C3'],
    tabs: ['Perfil', 'Uso IA', 'Automatización', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  disenyo: { // ✨ NUEVO
    label: 'Diseño Gráfico y Audiovisual',
    tipo: 'auditoria-disenyo-clm',
    secciones: ['section-0', 'section-DG1', 'section-DG2', 'section-DG3'],
    tabs: ['Perfil', 'Uso IA en Diseño', 'Proyectos Creativos', 'Actitudes'],
    badge: '📋 4 bloques'
  },
  desarrollo: { // ✨ NUEVO
    label: 'Programación y Desarrollo',
    tipo: 'auditoria-desarrollo-clm',
    secciones: ['section-0', 'section-DEV1', 'section-DEV2', 'section-DEV3'],
    tabs: ['Perfil', 'Uso IA en Desarrollo', 'Proyectos', 'Visión Estratégica'],
    badge: '📋 4 bloques'
  },
  sistemas: { // ✨ NUEVO
    label: 'Sistemas y Seguridad Informática',
    tipo: 'auditoria-sistemas-clm',
    secciones: ['section-0', 'section-SYS1', 'section-SYS2', 'section-SYS3'],
    tabs: ['Perfil', 'Uso IA en Sistemas', 'Infraestructura', 'Visión Estratégica'],
    badge: '📋 4 bloques'
  },
  direccion: { // ✨ NUEVO
    label: 'Dirección y Subdirecciones',
    tipo: 'auditoria-direccion-clm',
    secciones: ['section-0', 'section-DIR1', 'section-DIR2', 'section-DIR3'],
    tabs: ['Perfil', 'Visión Estratégica', 'Gestión', 'Política Institucional'],
    badge: '📋 4 bloques'
  }
};
```

---

## 🎨 EJEMPLO 7: Clases CSS adicionales necesarias

```css
/* Clases para nuevos caminos */
.camino-marketing,
.camino-conserjeria,
.camino-disenyo,
.camino-desarrollo,
.camino-sistemas,
.camino-direccion {
  display: none;
}

/* Mostrar sección activa */
.camino-marketing.active,
.camino-conserjeria.active,
.camino-disenyo.active,
.camino-desarrollo.active,
.camino-sistemas.active,
.camino-direccion.active {
  display: block;
}
```

---

**Estos ejemplos son listos para copiar y pegar en el archivo index.html**

**Versión:** 1.0
**Fecha:** 15 de abril de 2026
