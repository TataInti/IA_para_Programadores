# Directrices para agentes de IA: armado de notebooks

Este archivo define cómo crear, editar y revisar los notebooks educativos del
repositorio. Complementa las instrucciones del entorno y del usuario. Si existe
un conflicto, prevalecen la solicitud explícita del usuario, las políticas del
entorno y las instrucciones más específicas del directorio.

## 1. Contexto del curso

Los alumnos son programadores con poca experiencia en Python, inteligencia
artificial y, según el track, audio, NLP, visión o datos geoespaciales. Algunos
trabajan principalmente en frontend y otros en backend.

El objetivo no es formar investigadores, sino que puedan:

- reconocer los componentes de una solución de IA;
- ejecutar y modificar un pipeline sencillo;
- interpretar resultados y limitaciones;
- diseñar cómo integrar el componente en una aplicación existente;
- formular buenas preguntas antes de llevar una demo a producción.

El temario puede ser técnicamente avanzado, pero la explicación debe ser
intuitiva, progresiva y orientada a decisiones de software. El notebook es
material de clase y laboratorio, no solamente un archivo de código.

## 2. Prioridades al trabajar

Antes de editar, distinguir tres cosas:

1. La solicitud actual del usuario: define el resultado buscado.
2. Las instrucciones del repositorio y el contexto de la clase: definen el
   estilo y las restricciones del curso.
3. El contenido existente del notebook: es material del usuario que debe
   preservarse salvo que la solicitud pida cambiarlo.

Leer el notebook objetivo y, cuando sea útil, la clase anterior y la siguiente.
No reescribir un notebook completo para resolver un cambio localizado. Revisar
el estado del repositorio antes de editar y conservar cambios previos, outputs,
attachments y assets que no formen parte de la solicitud.

Trabajar en español, con tono cercano y directo. Usar el voseo que ya aparece
en los notebooks: “ejecutá”, “observá”, “cambiá”, “pensá”.

## 3. Estructura pedagógica estándar

Mantener, salvo que el usuario indique otra cosa, este recorrido:

1. Título de la clase y pregunta central.
2. Idea principal en lenguaje simple.
3. Objetivos observables, idealmente entre cuatro y seis.
4. Recorrido de la clase en una tabla breve.
5. Sección “Cómo trabajar con este notebook”.
6. Glosario mínimo.
7. Bloques teóricos cortos, cada uno conectado con un ejemplo.
8. Experimento guiado con una salida visible.
9. Preguntas de interpretación: describir, comparar y explicar lo observado.
10. Actividad aplicada de veinte a treinta minutos.
11. Límites, riesgos, privacidad y diferencia entre demo y producción.
12. Síntesis, comprobación conceptual y puente hacia la próxima clase.

La secuencia didáctica de cada concepto debería ser:

    problema o situación real
        → idea intuitiva
        → código mínimo
        → resultado visible
        → interpretación
        → decisión de integración

Evitar una introducción académica extensa antes de que los alumnos puedan
observar algo. Las fórmulas, detalles internos y nombres técnicos se incluyen
cuando ayudan a interpretar una salida o a tomar una decisión.

## 4. Cómo diseñar el código

- Ejecutar las celdas en orden, sin depender de variables creadas mucho después.
- Mantener una celda con imports y otra con configuración reutilizable.
- Usar nombres descriptivos y comentarios breves; no esconder el flujo detrás
  de demasiadas funciones.
- Marcar las partes editables con “✏️” y un comentario TODO concreto.
- Hacer que una modificación produzca una diferencia observable.
- Exponer los parámetros importantes cerca del experimento: umbral, duración,
  ventana, temperatura, cantidad de tokens, resolución, etc.
- Explicar qué se espera que cambie antes de pedir que se ejecute.
- Preferir un experimento pequeño que el alumno pueda repetir y comparar antes
  que una búsqueda automática de muchas combinaciones.
- Mostrar errores con mensajes accionables: qué falta y cómo continuar.
- Evitar estado oculto, ejecuciones mágicas o código que sólo funciona después
  de ejecutar celdas en un orden accidental.
- No borrar outputs existentes sin una razón pedagógica o una solicitud
  explícita: muchas veces documentan un resultado importante de la clase.

Cada bloque de código debe tener un propósito reconocible. Si una celda mezcla
descarga, configuración, inferencia, visualización y guardado, evaluar si puede
separarse para que los alumnos comprendan el flujo.

## 5. Archivos, rutas, assets y dependencias

- Usar rutas relativas al notebook y construirlas con os.path.join.
- No incluir rutas absolutas de la computadora del autor.
- Guardar assets de clase en assets/ y documentar qué representa cada uno.
- Verificar que el asset exista y ofrecer un mensaje claro si falta.
- Preferir datos pequeños, reproducibles y sin información personal.
- Si se incorpora un asset externo, registrar su procedencia y las condiciones
  de uso cuando corresponda.
- No depender de una API, una clave o un servicio pago salvo pedido explícito.
- Preferir modelos locales pequeños, CPU-friendly y con descarga cacheada.
- Si aparece una dependencia nueva, agregarla a requirements.txt sólo cuando
  realmente sea necesaria y actualizar README.md si cambia la preparación.
- Mantener los notebooks ejecutables con el entorno documentado en README.md.
- No guardar modelos descargados, caches ni outputs temporales en Git si están
  cubiertos por .gitignore.

Las celdas de preparación deben indicar si la primera ejecución descarga un
modelo, cuánto puede tardar de forma aproximada y qué queda cacheado después.

## 6. Reglas específicas por modalidad

### Audio

- Reproducir el audio de entrada junto con sus metadatos: duración, sample
  rate, canales y formato cuando estén disponibles.
- Reproducir también los audios generados, no limitar la clase a gráficos.
- Mostrar waveform, espectrograma o features sólo cuando ayuden a responder una
  pregunta concreta.
- Usar un flujo explícito: cargar → inspeccionar → transformar → escuchar o
  visualizar → guardar.
- Hacer que los alumnos puedan alterar pocos parámetros relevantes y comparar
  antes y después.
- Para ASR, mostrar la transcripción completa y advertir que ruido, música,
  acentos, nombres propios y silencio pueden producir errores o alucinaciones.
- Para TTS, permitir escuchar el resultado y señalar que una voz sintética no
  implica que el contenido sea correcto.

### NLP y LLM

- Separar modelo, prompt, parámetros y casos de prueba en celdas identificables.
- Tratar el prompt como parte del diseño del software, no como texto decorativo.
- Definir un contrato de salida legible por una aplicación: campos, etiquetas o
  JSON según la madurez de la clase.
- Mostrar primero la salida cruda antes de parsearla o transformarla.
- Probar como mínimo un caso normal, uno incompleto o ambiguo y uno riesgoso o
  fuera de dominio.
- Exponer temperatura y longitud de salida sólo si sirven para discutir el
  comportamiento.
- No afirmar que un modelo pequeño es confiable sólo porque produjo una
  respuesta fluida.
- Si se usa salida estructurada, contemplar validación y una ruta de error.

### Visión

- Mostrar la imagen original antes de la predicción.
- Explicar qué representa cada caja, etiqueta, máscara o score.
- Mantener visibles los umbrales que los alumnos puedan modificar.
- Comparar al menos dos resultados y discutir falsos positivos y negativos.
- Separar el tamaño de visualización del tamaño de entrada al modelo.

### Datos geoespaciales

- Mostrar CRS, resolución, extensión y bandas antes de operar.
- Visualizar la escena, la geometría y el resultado con una leyenda clara.
- Explicar qué parte es dato, qué parte es transformación y qué parte es una
  decisión de negocio.

## 7. Actividades prácticas

Una actividad no debe ser sólo una pregunta conceptual ni una lista abierta de
pasos. Debe combinar:

- una decisión de producto o flujo de trabajo;
- un laboratorio corto sobre el resultado visible;
- una entrega concreta;
- una reflexión sobre errores y producción.

Para una actividad grupal de treinta minutos, usar una organización similar:

- 5 minutos: entender el escenario y definir el contrato de entrada/salida;
- 10 minutos: modificar el prompt, la lógica o los parámetros;
- 10 minutos: ejecutar casos contrastantes y registrar qué cambió;
- 5 minutos: compartir un acierto y un fallo o decisión pendiente.

Proponer grupos de tres o cuatro con roles rotativos, por ejemplo:

- flujo de producto e integración;
- prompt o lógica;
- pruebas y casos límite;
- documentación y presentación.

La consigna debe indicar:

- quién usa el sistema;
- qué problema resuelve;
- qué entra y qué sale;
- qué no está permitido inventar o prometer;
- qué deben modificar;
- cómo sabrán si el resultado mejoró;
- qué deben entregar o explicar al cierre.

Incluir casos de prueba contrastantes: caso feliz, información faltante,
entrada ruidosa o ambigua y caso fuera de alcance. Para temas de salud, incluir
siempre una decisión de derivación o escalamiento humano.

## 8. Salud, privacidad y producción

En ejemplos de salud, el asistente debe:

- no diagnosticar ni indicar tratamientos;
- no inventar turnos, horarios, disponibilidad o acciones ejecutadas;
- pedir datos faltantes de forma explícita;
- escalar consultas clínicas, urgencias, ambigüedades y baja confianza;
- distinguir una respuesta informativa de una acción realmente realizada;
- contemplar consentimiento, minimización de datos, retención y acceso;
- evitar exponer datos personales en outputs o casos de prueba.

Cerrar cada pipeline con preguntas de integración: contrato de una API,
latencia, errores, reintentos, logging, observabilidad, privacidad y qué parte
queda bajo control humano. Explicar siempre qué es una demostración didáctica y
qué faltaría para usarla en producción.

## 9. Flujo de trabajo para el agente

1. Leer la solicitud y resumir mentalmente el resultado esperado.
2. Revisar el notebook objetivo, los assets involucrados y el contexto de las
   clases vecinas.
3. Revisar el estado del repositorio para no pisar cambios del usuario.
4. Elegir la modificación mínima que resuelva la necesidad.
5. Editar con apply_patch, conservando el formato JSON del notebook, los IDs de
   las celdas y el contenido no relacionado.
6. Validar que el notebook sea JSON válido.
7. Analizar sintácticamente las celdas de código.
8. Ejecutar una prueba proporcional al cambio: celdas afectadas, notebook
   completo o una copia si ejecutar modifica muchos outputs o descarga modelos.
9. Revisar visualmente que haya outputs comprensibles: plots, tablas, audio o
   imágenes según corresponda.
10. Ejecutar git diff --check y revisar el diff final.
11. Informar qué archivos cambiaron, qué se validó y qué no se ejecutó por
    depender de descargas, hardware o credenciales.

No regenerar notebooks completos de forma mecánica: suele producir ruido en
outputs, attachments e IDs y dificulta revisar el cambio pedagógico.

## 10. Lista de control antes de entregar

- [ ] La pregunta central y los objetivos coinciden con el laboratorio.
- [ ] El contenido se entiende sin conocimientos previos no declarados.
- [ ] Hay una salida visible antes de pedir interpretación.
- [ ] Las celdas se pueden ejecutar en orden desde un kernel limpio.
- [ ] Las rutas son relativas y los assets están documentados.
- [ ] Las variables editables están claramente marcadas.
- [ ] La actividad tiene tiempo, roles, casos de prueba y entrega.
- [ ] Se distinguen errores del dato, del modelo, del prompt y de la aplicación.
- [ ] Se incluyeron límites, privacidad y escalamiento cuando corresponde.
- [ ] README.md y requirements.txt reflejan cambios de dependencias o modelos.
- [ ] El diff no incluye cambios accidentales ni archivos generados innecesarios.
