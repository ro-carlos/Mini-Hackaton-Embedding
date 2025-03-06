[Saltar al contingut](es/infoAca/estudis/assignatures/AC.html.md)
[Menu](es/infoAca/estudis/assignatures/AC.html.md)

[ Masters in Computer Science and Engineering](index.md)

[![web UPC](/docroot/fib/imatges/Logo_UPC.gif)](index.md) [![web
FIB](/docroot/fib/imatges/Logo_FIB.gif)](es.md) FACULTAT D'INFORMÀTICA  
DE BARCELONA

[![Mapa](/docroot/fib/imatges/mobilitat-reduida-fib.gif)](es/centre/on.html.md
"Mobilidad reducida")

  * [![Inicio](/docroot/fib/imatges/home.gif)](es.md "Inicio")
  * [![Información](/docroot/fib/imatges/informacio.gif)](es/condicions_us.html.md "Información")
  * [![Contacto](/docroot/fib/imatges/correu.gif)](es/mail.md "Contacto")
  * [![Mapa](/docroot/fib/imatges/mapa_web.gif)](es/mapa.md "Mapa")

  * [Català](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)
  * [English](en/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)

cercar

  * [Estudiantes](es/perf/estudiants.md)
  * [PDI / PAS](es/perf/pdipas.md)
  * [Empresas](es/perf/empreses.md)
  * [Futuros estudiantes](es/perf/nous.md)
  * [Antiguos alumnos](es/perf/ex.md)

  * [FIB](es.md)
  * [Grado en Ingeniería en informática](es/estudiar-enginyeria-informatica.html.md)
  * [Ingenierias plan 2003](es/estudiar-enginyeria-informatica/enginyeries-pla-2003.html.md)
  * [Asignaturas](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)

[Versió en Català](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md) | [English version](en/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)

# Arquitectura de Computadores (AC)

Créditos | Dept. | Tipo | Requisitos  
---|---|---|---  
9.0 (7.2 ECTS) | AC | 

  * Obligatoria para la EI
  * Optativa para la ETIG
  * Optativa para la ETIS

|  _ [EC2](es/infoAca/estudis/assignatures/EC2.html.md) \- _Prerequisito para
la_ EI , ETIG , ETIS  
[EST](es/infoAca/estudis/assignatures/EST.html.md) \- _Prerequisito para la_
EI , ETIG , ETIS  
[SO](es/infoAca/estudis/assignatures/SO.html.md) \- _Prerequisito para la_ EI
, ETIS  
_  
  
## Profesores

Responsable: | **(-)**  
---|---  
Otros:| (-)  
  
## Objectivos Generales

Capacitación para efectuar evaluaciones cuantitativas, utilizando figuras de
mérito, del rendimiento de un procesador al ejecutar un programa. Comprensión
de las técnicas de concurrencia, transparentes al programador de lenguaje
máquina, que se utilizan en los procesadores con el fin de reducir el tiempo
de ejecución. Aplicación de técnicas de reestructuración de código
(planificación de instrucciones) para soportar la latencia de las
instrucciones. Comprensión de algunas de las restricciones que impone la
tecnología disponible y su proyección futura.

## Objectivos Específicos

### Conocimientos

  1. Importancia de evaluar prestaciones para justificar alternativas.
  2. Conceptos de segmentación y paralelismo.
  3. Concepto de dependencia (precedencia)
  4. Concepto de riesgo.
  5. Conceptos de predicción y especulación.Mecanismos hardware para reducir la latencia efectiva de las instrucciones.   
  
Concepto de renombre.  
  
Compromisos hardware-software.

### Habilidades

  1. Evaluación cuantitativa de prestaciones.
  2. Análisis de caminos de datos y su modificación.
  3. Evaluación de retardos en un camino de datos y su relación con el tiempo de ciclo.
  4. Construcción de diagramas temporales del proceso de interpretación de instrucciones en un procesador que utiliza segmentación y paralelismo.
  5. Comprensión del código generado por un compilador y su posible modificación respetando el cálculo que efectúa.

### Competencias

  1. Compresión, a nivel básico, de la descripción de la microarquitectura de un procesador.
  2. Evaluación de las prestaciones que se pueden extraer de un procesador.
  3. Aprendizaje y comprensión de mecanismos o conceptos, relacionados con el contenido de la asignatura, aunque no hayan sido explicados explícitamente.
  4. Aprendizaje y comprensión de nuevos conceptos que se incluyan en el futuro en la microarquitectura de un procesador.

## Contenidos

Horas estimadas de:

T  |  P  |  L  |  Alt  |  L Ext.  |  Est  |  O. Ext.   
---|---|---|---|---|---|---  
Teoria | Problemas | Laboratorio | Otras actividades | Laboratorio externo | Estudio | Otras horas fuera del horario fijado  
  
|  1\.  | Arquitectura Von-Neumann y prestaciones   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
4,0 | 4,0 | 2,0 | 0 | 2,0 | 6,0 | 0 | 18,0  
  
  

  * **Laboratorio:**  
Aprendizaje de la herramienta de simulación.  
  
Recordatorio del funcionamiento y características básicas de los elementos que
constituyen el camino de datos de un procesador uniciclo.  
  

  * **Actividades de laboratorio adicionales:**  
Lectura de los enunciados de las prácticas y contestación reflexiva a las
preguntas que se efectúan a partir de las mediciones realizadas en el
laboratorio.

  
  
|  2\.  | Técnicas para incrementar el número de operaciones por unidad de tiempo   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
4,0 | 2,0 | 0 | 0 | 0 | 10,0 | 0 | 16,0  
  
|  3\.  | Procesador escalar segmentado lineal   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
6,0 | 5,0 | 8,0 | 0 | 8,0 | 20,0 | 0 | 47,0  
  
  

  * **Laboratorio:**  
Camino de datos de un procesador segmentado lineal y adecuación de la
semántica del procesador segmentado a la semántica del lenguaje máquina.
Mejoras en el procesador segmentado para incrementar las prestaciones.  
  
  
  

  * **Actividades de laboratorio adicionales:**  
Lectura de los enunciados de las prácticas y contestación reflexiva a las
preguntas que se efectúan a partir de las mediciones realizadas en el
laboratorio.

  
  
|  4\.  | Procesador escalar con operaciones multiciclo   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
4,0 | 3,0 | 0 | 0 | 0 | 12,0 | 0 | 19,0  
  
|  5\.  | Técnicas software para disminuir los riesgos de datos y de secuenciamiento   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
3,0 | 2,0 | 0 | 0 | 0 | 8,0 | 0 | 13,0  
  
|  6\.  | Procesador superescalar   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
4,0 | 3,0 | 0 | 0 | 0 | 10,0 | 0 | 17,0  
  
|  7\.  | Predicción en instrucciones de secuenciamiento   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
3,0 | 2,0 | 0 | 0 | 0 | 8,0 | 0 | 13,0  
  
|  8\.  | Procesador con anticipación   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
6,0 | 4,0 | 0 | 0 | 0 | 12,0 | 0 | 22,0  
  
|  9\.  | Ejecución especulativa, perspectivas y tendencias   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
2,0 | 1,0 | 0 | 0 | 0 | 3,0 | 0 | 6,0  
  
|  10\.  | Herramienta de simulación   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
0 | 0 | 3,0 | 0 | 0 | 0 | 0 | 3,0  
  
  

  * **Laboratorio:**  
Aprendizaje de la herramienta de simulación.  
  
Recordatorio del funcionamiento y características básicas de los elementos que
constituyen el camino de datos de un procesador uniciclo.

  
  
  
Total por tipo | T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
---|---|---|---|---|---|---|---|---  
36,0 | 26,0 | 13,0 | 0 | 10,0 | 89,0 | 0 | 174,0  
Horas adicionales dedicadas a la evaluación | 5,0  
Total horas de trabajo para el estudiante | 179,0   
  

## Metodología docente

Clases presenciales de exposición estructurada y constructiva de conceptos y
de los compromisos que aparecen en su aplicación práctica.  
  
Clases presenciales centradas en el trabajo personal para consolidar los
conceptos, destrezas y competencias.  
  
  
  
Clases presenciales centradas en el trabajo cooperativo para consolidar los
conceptos, destrezas y competencias, a realizar en aulas de laboratorio.

## Método de evaluación

A) Examen final escrito individual sobre los conceptos, destrezas y
competencias.B) Prueba escrita individual, de seguimiento, sobre los
conceptos, destrezas y competencias.  
  
C) Evaluación de trabajo cooperativo de algunos conceptos, destrezas y
competencias básicas.  
  
  
  
Nota Final = max(0.70 x A + 0.15 x B, 0.85 x A) + 0.15 x C

## Bibliografía básica

  * John L. Hennessy, David A. Patterson **Computer architecture : a quantitative approach** , Elsevier, Morgan Kaufmann, 2007.
  * David A. Patterson, John L. Hennessy **Organización y diseño de computadores : la interfaz hardware/software** , McGraw-Hill, 1994.

## Bibliografía complementaria

  * Capilano Computing Systems, Ltd **LogicWorks 4 : interactive circuit design software** , Addison-Wesley, 1999.

## Enlaces web

_(Información no introducida)_

## Capacidades previas

Circuitos lógicos: combinacionales y secuenciales.Programación, representación
de datos elementales y estructurados.  
  
Funcionamiento de un computador: componentes y su interconexionado.  
  
Comprensión de lenguaje máquina.  
  
Funcionamiento de la jerarquía de memoria y mecanismos que la soportan.  
  
Comunicación del procesador con el exterior y mecanismos que lo soportan.  
  
Cálculo estadístico básico.  
  
Prerrequisitos sugeridos: EC2, Estadística, Sistemas Operativos.

  

Compartir

[ ![Share](http://s7.addthis.com/static/btn/sm-plus.gif) ](bookmark.php.md
"Compartir")

  * [La Facultad ](es/centre.html.md)
  * [Ingeniería informática ](es/estudiar-enginyeria-informatica.html.md)
    * [Acceso a los estudios ](es/estudiar-enginyeria-informatica/acces.html.md)
    * [Plan de estudios Grado ](es/estudiar-enginyeria-informatica/grau.html.md)
    * [Especialidades del Grado ](es/estudiar-enginyeria-informatica/especialitats-grau.html.md)
    * [Asignaturas del grado ](es/estudiar-enginyeria-informatica/assignatures.html.md)
    * [Trabajo de Fin de Grado ](es/estudiar-enginyeria-informatica/treball-final-grau.html.md)
    * [Doble titulación ](es/estudiar-enginyeria-informatica/doble-titulacio.html.md)
    * [Premios ](es/estudiar-enginyeria-informatica/premis.html.md)
    * [Normativas Académicas ](es/estudiar-enginyeria-informatica/normatives.html.md)
    * [Horarios grado ](es/estudiar-enginyeria-informatica/horaris.html.md)
    * [Exámenes finales ](es/estudiar-enginyeria-informatica/examens-finals.html.md)
    * [Exámenes parciales ](es/estudiar-enginyeria-informatica/examens-parcials.html.md)
    * [Ingenierias plan 2003 ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003.html.md)
      * [Ingeniería en Informática ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/EI.html.md)
      * [Ingeniería Técnica en Informática de Gestión ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/ETIG.html.md)
      * [Ingeniería Técnica en Informática de Sistemas ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/ETIS.html.md)
      * [Proyecto final de carrera ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/PFC.html.md)
      * **[Asignaturas ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)**
      * [Normativas ](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/normatives.html.md)
    * [Matrícula ](es/estudiar-enginyeria-informatica/matricula.html.md)
    * [Calendarios ](es/estudiar-enginyeria-informatica/calendari-lectiu.html.md)
  * [Bioinformática ](es/bioinformatica.html.md)
  * [Másters ](es/masters.html.md)
  * [Trámites secretaría ](es/tramits.html.md)
  * [Servicios y equipamientos ](es/serveis.html.md)
  * [Movilidad ](es/erasmus.html.md)
  * [Universidad-Empresa ](es/empresa.html.md)
  * [Vida universitaria ](es/vida.html.md)

Username Password

[ ![Entra amb el carnet
UPC](/docroot/fib/imatges/carnet_upc_es.gif)](cas/login-cert.md)

  * [Noticias](es/noticies.md)
  * [Agenda](es/agenda.md)

  

![logo FIB](/docroot/fib/imatges/Logo_FIB_inferior.gif) © Facultad de
Informática de Barcelona \- [ Contacto](es/mail.md) \-
[![](/docroot/fib/imatges/feed-icon-16x16.gif) RSS](es/rss.rss.md) Esta web
utiliza cookies propias para ofrecerle una mejor experiencia y servicio. Si
continúa la navegación, entendemos que acepta nuestra [ política de
cookies](aviso-legal/politica-de-cookies.md). [Versión
clássica](es/infoAca/estudis/assignatures/AC.html.md) [Versión
móvil](es/infoAca/estudis/assignatures/AC.html.md)

