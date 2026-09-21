# Guía rápida para la instructora

Este es el único documento de este repositorio escrito en español. Existe para orientarte: qué hay, en qué orden usarlo y qué decidir. **Todo el material que ve el alumnado y el cliente está en inglés**, porque el curso se imparte en inglés con interpretación al árabe.

---

## En una frase

El repositorio contiene un curso de cinco días completo y ejecutable. Lo que falta no es contenido: es ensayo, las decisiones que solo puede tomar el organizador, y las diapositivas finales.

## Lo primero que tienes que hacer

**Antes de estudiar nada, escribe al organizador.** Hay ocho preguntas cuya respuesta cambia el diseño del curso, y todas tardan menos en preguntarse que en corregirse después. Están al final de `CURRICULUM_REVIEW.md`. Las tres críticas:

1. **¿La interpretación es consecutiva o simultánea?** De esto depende todo el horario. El material asume consecutiva, que es lo conservador.
2. **¿22,5 horas lectivas más descansos, o 25 horas sin contar descansos?** Son 30 minutos más por día.
3. **¿Cuánta gente del grupo programa hoy?** El folleto invita explícitamente a perfiles directivos. Si más de un tercio no programa, hay que ajustar el enfoque y acordarlo por escrito antes de viajar.

## Cómo está organizado esto

```
PROGRAMME.md          ← el temario para presentar al cliente
CURRICULUM_REVIEW.md  ← qué promete el folleto, qué falta, qué añadir
COURSE_GUIDE.md       ← estado del material
SETUP.md              ← instalación del entorno

instructor/           ← para ti
  GUIA_RAPIDA_ES.md      este documento
  RUNBOOK.md             ★ el guion del día, para imprimir y tener en la mano
  QUESTION_BANK.md       ★ preguntas difíciles con respuestas preparadas
  PREPARATION_PLAN.md    plan de preparación de siete días
  CLASSROOM_AND_INTERPRETER.md  aula, parejas, interpretación
  INTERPRETER_GLOSSARY.md       glosario para la sesión con el intérprete
  first_model.ipynb      tu primer modelo, empieza por aquí

participant/          ← para el alumnado (se imprime o se envía)
  HANDBOOK.md            el cuaderno de trabajo
  CHEATSHEET_*.md        dos fichas de referencia
  GLOSSARY_EN_AR.md      glosario inglés-árabe (borrador, lo valida el intérprete)
  CAPSTONE.md            el proyecto que atraviesa la semana
  PRE_COURSE_PACK.md     correo de bienvenida e instalación
  POST_COURSE_PACK.md    qué hacer después del curso
  FEEDBACK_FORM.md       evaluación del curso
  EXIT_SELF_ASSESSMENT.md  autoevaluación final

day-01-eda/ … day-05-big-data/   ← un directorio por día
  TEACHING_GUIDE.md      ★ lo que explicas, con las palabras
  TASK_CARDS.md          las tareas de las parejas, cronometradas
  student.ipynb          lo que abre el alumnado
  worked.ipynb           la versión resuelta, para ti
  solutions.ipynb        soluciones de los ejercicios
  ANSWER_KEY.md          respuestas y preguntas de cierre
  worked_RESULTS.md      ★ resultados guardados: tu red de seguridad
  figures/               gráficos ya generados

assessments/          diagnóstico inicial y práctica final
presentations/        los cinco guiones de diapositivas
scripts/              generadores de cuaderno y diapositivas
dist/                 lo generado: cuaderno HTML y cinco .pptx
```

Los ★ son los cuatro archivos que de verdad vas a usar.

## Orden de trabajo recomendado

### Semana previa a la preparación

1. Manda las ocho preguntas al organizador.
2. Manda `participant/PRE_COURSE_PACK.md` al alumnado, con el diagnóstico adjunto. **Diez días antes como mínimo** — si alguien no puede instalar Python, quieres saberlo con tiempo.
3. Reúnete con el intérprete y repasad `participant/GLOSSARY_EN_AR.md`. La columna árabe es un borrador; manda lo que diga el intérprete. Presta atención al apartado final de ambigüedades: *precision* y *accuracy* se traducen las dos como الدقة y el día 2 las contrapone directamente.

### Los siete días de preparación

Sigue `instructor/PREPARATION_PLAN.md`. Un día por jornada del curso, más un día final de ensayo completo.

Para cada día, en este orden:

1. Lee el `TEACHING_GUIDE.md` entero.
2. Ejecuta `worked.ipynb` de principio a fin, **reiniciando el kernel antes**.
3. Haz las tareas de `TASK_CARDS.md` como si fueras alumna, sin mirar las soluciones.
4. Explica el día en voz alta, sin notas, a alguien o a la pared. Cronométralo.
5. Lee la sección correspondiente de `QUESTION_BANK.md` y contesta en voz alta.

**El criterio para dar un día por preparado:** puedes ejecutarlo desde cero, explicar cada decisión, responder a las preguntas del ejercicio, y continuar la clase usando solo `worked_RESULTS.md` si falla el portátil. Si un día no pasa ese filtro, no está listo — y es mejor decírselo al organizador que descubrirlo en el aula.

### La víspera

- Imprime `instructor/RUNBOOK.md`. Es lo que sostienes en la mano.
- Confirma que Spark arranca en tu portátil (día 5). Si no arranca, no pasa nada: existe `day-05-big-data/OFFLINE_ACTIVITY.md`.
- Descarga todo. No cuentes con internet en el aula.
- Genera e imprime el cuaderno: `python scripts/build_participant_handbook.py`, luego abre `dist/participant-handbook.html` e imprime a PDF. 20 copias más 5 de repuesto.

## Lo que tiene que quedarte claro sobre el diseño

El material tiene una disciplina deliberada y es lo mejor que tiene: **ningún método se enseña sin una línea base con la que compararlo, una estrategia de evaluación y una limitación declarada.** No la diluyas por ganar tiempo. Es lo que separa este curso de los demás, y es lo que el alumnado recordará dentro de un año.

La frase que repites toda la semana es: *"¿qué es lo que esto no demuestra?"*

## Lo que cambia respecto a la versión anterior del repositorio

He añadido tres capas que no existían:

1. **`CURRICULUM_REVIEW.md`** — el análisis de lo que promete el folleto de LPC frente a lo que hay. Hay una tabla de trazabilidad línea por línea: úsala con el organizador, es la forma más rápida de demostrar que el temario contratado está cubierto.
2. **`participant/`** — todo el material del alumnado, que antes no existía. El repositorio era íntegramente para la instructora.
3. **`PROGRAMME.md`** — el temario en versión presentable, para mandar al cliente.

Y tres cosas prácticas: `RUNBOOK.md`, `QUESTION_BANK.md` y los generadores de `scripts/`.

## Las dos carencias reales que no he cerrado

Las digo claras porque conviene que las decidas tú:

**1. No hay ningún dato real.** Todo es sintético. Es una decisión pedagógica defendible y está documentada con honestidad, pero el folleto promete *"ejercicios extraídos de la práctica y del mundo real"*. Lo cierra un único conjunto de datos abiertos, pequeño, con licencia comprobada, descargado y commiteado **antes de viajar**. No lo he elegido yo porque la licencia hay que verificarla y un dato sin licencia clara es peor que ningún dato.

**2. Faltan seis módulos que recomiendo añadir.** Están especificados con detalle y tiempo estimado en `CURRICULUM_REVIEW.md` — backtesting con origen móvil, explicabilidad, el puente texto-serie temporal, la decisión bayesiana, gobernanza de datos sintéticos y puesta en producción. Ninguno es imprescindible para cumplir el contrato; todos elevan bastante el resultado. Suman unos tres días de trabajo. Si solo haces uno, haz el backtesting del día 3.

Lo que sí he cerrado del todo: comunicación y visualización (estaba en la categoría del curso y no se enseñaba), el proyecto de la semana, y todo el material del alumnado.

## Si algo sale mal en el aula

Está todo en la última tabla de `RUNBOOK.md`. Lo esencial:

- **Falla una demostración:** no depures en directo más de un minuto. Pasa a `worked_RESULTS.md`, sigue, y lo arreglas en el descanso.
- **La interpretación va lenta:** quita las extensiones opcionales. Nunca quites un descanso ni el laboratorio principal.
- **No sabes una respuesta:** *"prefiero verificarlo a darte una respuesta inexacta; lo anoto y te contesto mañana"*. Apúntalo donde se vea. Y contesta. Hacer esto una vez bien vale más que responder diez preguntas con seguridad.
- **El grupo sabe mucho más de lo previsto:** pasa a las extensiones y avisa al organizador **el mismo día y por escrito**.

## Lo que no hay que prometer

- Que el curso capacita profesionalmente. Es formación de cinco días con evaluación formativa. El certificado lo dice explícitamente y esa frase se queda.
- Que lo construido en clase sirve para producción. No sirve, y el día 5 se explica por qué.
- Resultados sobre los datos del cliente. Nadie puede saberlo desde aquí.

Decir esto no resta autoridad: la suma. Es, literalmente, lo que el curso enseña.
