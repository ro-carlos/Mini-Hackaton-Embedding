[Saltar al contingut](es/infoAca/estudis/assignatures/EC2.html.md)
[Menu](es/infoAca/estudis/assignatures/EC2.html.md)

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

# Estructura de Computadores 2 (EC2)

Créditos | Dept. | Tipo | Requisitos  
---|---|---|---  
7.5 (6.0 ECTS) | AC | 

  * Obligatoria para la EI
  * Obligatoria para la ETIS
  * Optativa para la ETIG

|  _ [EC1](es/infoAca/estudis/assignatures/EC1.html.md) \- _Prerequisito para
la_ EI , ETIG , ETIS  
[IC](es/infoAca/estudis/assignatures/IC.html.md) \- _Prerequisito para la_ EI
, ETIG , ETIS  
[P1](es/infoAca/estudis/assignatures/P1.html.md) \- _Prerequisito para la_ EI
, ETIG , ETIS  
_  
  
## Profesores

Responsable: | **(-)**  
---|---  
Otros:| (-)  
  
## Objectivos Generales

En las asignaturas previas (IC y EC1) el estudiante ha adquirido los
conocimientos básicos de cómo funciona un computador. Todas las prácticas, los
ejercicios y los problemas han sido realizados sobre computadores pedagógicos
y simuladores. El objetivo principal de EC2 es que el estudiante profundice en
los conocimientos ya adquiridos y que los aplique sobre un computador real: un
PC compatible basado en un procesador IA32.

## Objectivos Específicos

### Conocimientos

  1. El alumno ha de conocer el Lenguaje Máquina de un procesador comercial (IA32).
  2. El alumno ha de conocer los dispositivos básicos de entrada/salida en una máquina real (PC compatible).
  3. El alumno ha de comprender las implicaciones que tiene en el rendimiento del computador la velocidad, el ancho de banda y la jerarquía de buses.
  4. Dada una configuración del subsistema de entrada/salida, el alumno debería ser capaz de escoger la que obtenga mejor rendimiento.

### Habilidades

  1. El alumno ha de ser capaz de realizar programas de 15-25 líneas en ensamblador de una máquina real (IA32).
  2. El alumno ha de ser capaz de enlazar programas escritos en ensamblador con programas escritos en C, llamando desde alto nivel a una rutina escrita en ensamblador y viceversa. Incluye el paso de parámetros y la gestión de las variables locales. El alumno ha de ser capaz de traducir código escrito en C a ensamblador. El código generado ha de ser razonablemente eficiente.
  3. El alumno ha de aprender a desarrollar programas en C y ensamblador en un entorno de trabajo Linux. El alumno ha de ser capaz de utilizar un depurador (debugger) para eliminar errores en un programa en ensamblador y C.
  4. El alumno ha de ser capaz de programar operaciones básicas de entrada/salida, utilizando sincronización por encuesta y por interrupciones.
  5. El alumno ha de comprender y saber evaluar los esquemas básicos de memorias cache que incluyen: algoritmos de emplazamiento, diferentes tamaños de cache y de línea, políticas de escritura, algoritmos de reemplazo, y varios niveles de cache.
  6. El alumno ha de saber evaluar el impacto de realizar transformaciones simples en un programa escrito en C cuando éste se ejecuta en procesador con una configuración dada de Memoria Cache.

### Competencias

  1. Capacidad de abstracción. Capacidad para enfrentarse a problemas nuevos recurriendo conscientemente a estrategias que han resultado útiles en problemas resueltos anteriormente.
  2. Capacidad de análisis y de síntesis.
  3. Capacidad para trabajar efectivamente en grupos pequeños de personas para la resolución de un problema de dificultad media.

## Contenidos

Horas estimadas de:

T  |  P  |  L  |  Alt  |  L Ext.  |  Est  |  O. Ext.   
---|---|---|---|---|---|---  
Teoria | Problemas | Laboratorio | Otras actividades | Laboratorio externo | Estudio | Otras horas fuera del horario fijado  
  
|  1\.  | Ensamblador del IA32   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
12,0 | 8,0 | 6,0 | 0 | 12,0 | 20,0 | 0 | 58,0  
En este tema se pretende que los alumnos practiquen con un ensamblador real en
una máquina real. El procesador escogido es el utilizado en los PCs
compatibles (Intel Pentium y AMD). El ensamblador escogido es el IA32. El
entorno de trabajo será el SO Linux.

  
  
|  2\.  | Subsistema de Memoria   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
13,0 | 7,0 | 4,0 | 0 | 8,0 | 20,0 | 0 | 52,0  
En este tema se repasan los conceptos ya conocidos de jerarquía de memoria y
localidad. Se estudia un sistema de memoria principal real, la memoria cache
en profundidad y la memoria virtual.

  
  
|  3\.  | Entrada/Salida   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
10,0 | 2,0 | 1,0 | 0 | 2,0 | 12,0 | 0 | 27,0  
En este tema se repasarán los conceptos ya conocidos de Entrada / Salida
(encuesta, interrupciones, DMA, periféricos, etc). Se estudiarán los
dispositivos reales de un PC compatible.En este tema también se estudiarán los
elementos de interconexión de un computador: los buses, haciendo énfasis en
los buses estándar y en la jerarquía de buses.  

  
  
  
Total por tipo | T  | P  | L  | Alt  | L Ext. | Est  | O. Ext. | Total   
---|---|---|---|---|---|---|---|---  
35,0 | 17,0 | 11,0 | 0 | 22,0 | 52,0 | 0 | 137,0  
Horas adicionales dedicadas a la evaluación | 3,0  
Total horas de trabajo para el estudiante | 140,0   
  

## Metodología docente

La asignatura tiene 5 horas de clase por semana: 4 de teoría y problemas y 1
de laboratorio.  
  
Las clases de laboratorio servirán de soporte a la teoría. Los alumnos
dispondrán de la información de prácticas antes de cada sesión. Es
recomendable que los alumnos preparen la práctica antes de realizarla (leer la
documentación, estudiar los conceptos utilizados, etc). Igualmente es
recomendable, una vez acabada la sesión, repasar los conceptos vistos. Las
sesiones de laboratorio son presenciales y evaluables, y se realizan de forma
exclusiva en el grupo que el alumno esta matriculado, por tanto es
imprescindible que no haya solapamientos del laboratorio en el momento de
realizar la matricula.  
  
No se hará una distinción explícita entre las clases de teoría y problemas,
sino que se irán distribuyendo en función de las necesidades de cada tema.  
  
En esta asignatura se pretende realizar una evaluación continuada. Durante el
curso se realizarán 3 controles. Si el alumno supera satisfactoriamente la
evaluación continuada no será necesario que realice el examen final.

## Método de evaluación

La nota de la asignatura se calculará a partir de 2 notas:  
\- Nota de contenidos teóricos (peso 80%).  
\- Nota de laboratorio o contenidos prácticos (peso 20%).  
  
La nota de laboratorio se obtendrá a partir de las notas de seguimiento de las
sesiones de prácticas que elabora cada profesor.  
  
La nota de contenidos teóricos se puede obtener por controles a lo largo del
cuso o bien en el examen final. Durante el curso se realizarán 3 controles
teóricos (C1 Lenguaje Máquina, peso 33%; C2 Jerarquía, peso 33%; C3 Memoria
Virtual y Entrada/Salida, peso 33%). El alumno que supere la parte de
contenidos teóricos por medio de los controles quedará liberado, si quiere,
del examen final. Los alumnos que se presenten al examen final perderán la
nota de los controles de clase.

## Bibliografía básica

  * Randal E. Bryant, David R. O'Hallaron **Computer systems : a programmer's perspective** , Pearson Education, 2002.
  * David A. Patterson, John L. Hennessy **Estructura y diseño de computadores : interficie circuitería-programación** , Reverté, 1999.

## Bibliografía complementaria

_(Información no introducida)_

## Enlaces web

_(Información no introducida)_

## Capacidades previas

\- El alumno ha de ser capaz de programar rutinas sencillas en un ensamblador
cualquiera.  
\- El alumno ha de ser capaz de programar rutinas de complejidad media en un
Lenguaje de Alto Nivel Cualquiera.  
\- El alumno ha de tener conocimientos básicos de circuitos digitales.  
\- El alumno ha de tener conocimientos básicos de aritmética binaria.

  

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
clássica](es/infoAca/estudis/assignatures/EC2.html.md) [Versión
móvil](es/infoAca/estudis/assignatures/EC2.html.md)

