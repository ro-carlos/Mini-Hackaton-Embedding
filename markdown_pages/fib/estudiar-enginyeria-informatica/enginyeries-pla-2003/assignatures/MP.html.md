[Saltar al contingut](fib/estudiar-enginyeria-informatica/enginyeries-
pla-2003/assignatures/MP.html.md) [Menu](fib/estudiar-enginyeria-
informatica/enginyeries-pla-2003/assignatures/MP.html.md)

[ Masters in Computer Science and Engineering](index.md)

[![web UPC](/docroot/fib/imatges/Logo_UPC.gif)](index.md) [![web
FIB](/docroot/fib/imatges/Logo_FIB.gif)](fib.md) FACULTAT D'INFORMÀTICA  
DE BARCELONA

[![Mapa](/docroot/fib/imatges/mobilitat-reduida-
fib.gif)](fib/centre/on.html.md "Mobilitat reduïda")

  * [![Inici](/docroot/fib/imatges/home.gif)](fib.md "Inici")
  * [![Informació](/docroot/fib/imatges/informacio.gif)](fib/condicions_us.html.md "Informació")
  * [![Contacte](/docroot/fib/imatges/correu.gif)](fib/mail.md "Contacte")
  * [![Mapa](/docroot/fib/imatges/mapa_web.gif)](fib/mapa.md "Mapa")

  * [Castellano](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)
  * [English](en/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)

cercar

  * [Estudiants](fib/perf/estudiants.md)
  * [PDI / PAS](fib/perf/pdipas.md)
  * [Empreses](fib/perf/empreses.md)
  * [Futurs estudiants](fib/perf/nous.md)
  * [Antics alumnes](fib/perf/ex.md)
  * [Incoming students](en/erasmus/vols_venir.html.md)

  * [FIB](fib.md)
  * [Grau en Enginyeria Informàtica](fib/estudiar-enginyeria-informatica.html.md)
  * [Enginyeries pla 2003](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003.html.md)
  * [Assignatures obertes](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)

[Versión en Castellano](es/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md) | [English version](en/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)

# Multiprocessadors (MP)

Crèdits | Dept. | Tipus | Requisits  
---|---|---|---  
7.5 (6.0 ECTS) | AC | 

  * Optativa per a l'EI
  * Optativa per a l'ETIS

|  _ [AC](fib/estudiar-enginyeria-informatica/enginyeries-
pla-2003/assignatures/AC.html.md) \- _Pre-requisit per la_ EI , ETIS  
_  
  
## Professors

Responsable: | **(-)**  
---|---  
Altres:| (-)  
  
## Objectius Generals

Coneixement de conceptes bàsics sobre multiprocessadors: terminologia,
estructura, les seves problemàtiques principals i solucions més freqüents.  
  
L'objectiu és conèixer els tipus de sistemes actualment en ús per a saber com
fer-los servir adequadament.  
  
Desenvolupar una actitud crítica a l'anàlisi del funcionament real d'aquests
sistemes que permeti millorar el rendiment que s'obté d'ells.

## Objectius Específics

### Coneixements

  1. Paral·lelisme i estructures de sistemes multiprocessadors
  2. Models de programació: memòria compartida (OpenMP) i pas de missatges (MPI)
  3. Coherència i consistència: Sistemes basats en bus i en directori
  4. Sincronització i implementació dels models de programación
  5. Xarxes d"interconnexió
  6. Sistemes Operatius per a multiprocessadors: Planificació.
  7. Exemples d"alguns sistemes reals.

### Habilitats

  1. Escriure programes paral·lels senzills tant en OpenMP com en MPI o conjuntament.
  2. Analitzar el rendiment dels mateixos i justificar/explicar els efectes observats.
  3. Identificar a priori potencials limitacions (colls d'ampolla) d'un sistema i estimar la importància dels mateixos per a un determinat ús de la màquina.

### Competències

  1. Honestedat amb sí mateixos: tenir clar el que se sap amb certesa i el que és especulació o hipòtesi encara no demostrada. Saber treure el millor partit possible d"un coneixement que sempre serà parcial.
  2. Capacitat d"especular amb possibles causes d"un comportament observat. Dissenyar experiments o fer mesures que puguin recolzar o desmentir les hipòtesis.
  3. Treball en grups petits.

## Continguts

Hores estimades de:

T  |  P  |  L  |  Alt  |  L Ext.  |  Est  |  A Ext.   
---|---|---|---|---|---|---  
Teoria | Problemes | Laboratori | Altres activitats | Laboratori extern | Estudi | Altres hores fora d'horari fixat  
  
|  1\.  | Paral·lelisme i multiprocessadors   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
2,0 | 2,0 | 0 | 0 | 0 | 2,0 | 0 | 6,0  
Paral·lelisme: Concepte, sobrecàrrega generació de treball, sincronització,
balanceig, llei d'amdahl.  
Multiprocessadors: Estructures bàsiques, top500.  
Models de programació: estructures de l'espai de direccions i que impliquen en
quant a la forma de paral·lelitzar un codi.

  
  
|  2\.  | OpenMP   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
4,0 | 4,0 | 0 | 0 | 0 | 4,0 | 0 | 12,0  
Descripció del llenguatge.Exemple de l'efecte de cada directiva en l'activitat
de cada thread.  
Implementació: Compilador i run time.

  
  
|  3\.  | MPI   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
4,0 | 4,0 | 0 | 0 | 0 | 4,0 | 0 | 12,0  
Descripció de les primitives: Punt a punt i col·lectives.Exemple de l'efecte
de les primitives a l'activitat de cada procés.  
Implementació del run time.

  
  
|  4\.  | Coherència i consistència en multiprocessadors de memòria compartida   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
6,0 | 6,0 | 0 | 0 | 0 | 6,0 | 0 | 18,0  
Problemàtica: el concepte de temps.  
Solucions bàsiques per a garantir coherència a sistemes basats en bus i
sistemes basats en directori.  
Solucions avançades: buffering de les peticions, caches multinivell, busos de
cicle partit.

  
  
|  5\.  | Sincronització   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
2,0 | 2,0 | 0 | 0 | 0 | 2,0 | 0 | 6,0  
Algoritmes de sincronització (exclusió mútua, punt a punt i barreres) i la
seva interacció amb el mecanisme de coherència.

  
  
|  6\.  | Xarxes d'interconnexió   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
4,0 | 4,0 | 0 | 0 | 0 | 4,0 | 0 | 12,0  
Components.  
Topologies.  
Algoritmes d'encaminament.  
Estratègies de commutació.  
Control de flux.  
Interfície de xarxa.

  
  
|  7\.  | Sistemes Operatius per a multiprocessadors   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
2,0 | 2,0 | 0 | 0 | 0 | 2,0 | 0 | 6,0  
Mal·leabilitat.  
Polítiques de planificació de treballs a llarg termini.  
Polítiques de planificació de processadors a curt/mig termini.  
Coordinació entre nivells.  
Gestió de memòria: col·locació de pàgines.

  
  
|  8\.  | Alguns sistemes reals   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
4,0 | 0 | 0 | 0 | 8,0 | 0 | 0 | 12,0  
Selecció d'un parell de multiprocessadors actuals i descripció de la seva
estructura i funcionament en relació amb els conceptes descrits durant el
curso  

  * **Activitats de laboratori addicionals:**  
Selecció d'un altre multiprocessador no descrit a classe i realització d'un
treball descrivint les seves opcions de disseny relacionant-les amb les
estructures vistes a classe.

  
  
|  9\.  | Anàlisi del rendiment   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
0 | 0 | 6,0 | 0 | 0 | 6,0 | 0 | 12,0  
  

  * **Laboratori:**  
Visualització i anàlisi amb Paraver: Navegació, fitxers de configuració
(mètriques: estat, funcions de usuari i run time, derivades de contadors
hardware,...). Aplicació a programa seqüencial, OpenMP i MPI. Obtenció de
traces.

  
  
|  10\.  | Paral·lelització amb OpenMP   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
0 | 0 | 6,0 | 0 | 0 | 6,0 | 0 | 12,0  
  

  * **Laboratori:**  
Paral·lelització d'una font seqüencial donada amb OpenMP. Optimització del
rendiment. Ajust dels resultats mitjançant la llei d'Amdahl.

  
  
|  11\.  | Paral·lelització amb MPI   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
0 | 0 | 6,0 | 0 | 0 | 6,0 | 0 | 12,0  
  

  * **Laboratori:**  
Paral·lelització d'una font seqüencial donat amb MPI. Optimización del
rendiment. Ajust dels resultats mitjançant la llei d'Amdahl.

  
  
|  12\.  | Programació de primitives bàsiques de comunicació/sincronització   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
0 | 0 | 6,0 | 0 | 6,0 | 0 | 0 | 12,0  
  
|  13\.  | Conceptes avançats   
---|---  
T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
6,0 | 4,0 | 0 | 0 | 0 | 6,0 | 0 | 16,0  
Descripció d'aspectes avançats en tots els temes anteriors: Paral·lelisme
multinivell a OpenMP, Comunicacions One-sided a MPI, MPI+OpenMP, Sistemes de
consistència relaxada, SDSM.

  
  
  
Total per tipus | T  | P  | L  | Alt  | L Ext. | Est  | A Ext. | Total   
---|---|---|---|---|---|---|---|---  
34,0 | 28,0 | 24,0 | 0 | 14,0 | 48,0 | 0 | 148,0  
Hores addicionals dedicades a l'avaluació | 4,0  
Total hores de treball per l'estudiant | 152,0   
  

## Metodologia docent

(-)

## Mètode d'avaluació

Es realitzarà un examen de l'assignatura, amb una part d'una hora sense apunts
i la resta amb apunts. Es puntua de 0 a 10.  
  
Per a les tres pràctiques obligatòries és necessari entregar una petita
memòria. A partir d'ella i el seguiment a classe de laboratori es valorarà
cada pràctica entre 0 i 3 (enter). La nota de Pràctiques és la nota promig de
les tres.  
  
La nota final s'obté de la següent manera:  
\- Si s'han entregat les tres pràctiques i la mitja de les tres és superior a
0, aleshores: Final = min(10, Examen + Pràctiques/2)  
\- En cas contrari (si no s'han entregat les tres, o es té un 0 de les tres):
Final = Examen / 2

## Bibliografía bàsica

  * David E. Culler, Jaswinder Pal Singh **Parallel computer architecture : a hardware/software approach** , Morgan Kaufmann Publishers, 1999.

## Bibliografía complementària

_(Informació no introduïda)_

## Enllaços web

  1. **http://www.openmp.org**  
Pagina de OpenMP y Manuales

  
  

  2. **http://www-unix.mcs.anl.gov/mpi/**  
Pagina de MPI y manuales

  
  

  3. **http://www.netlib.org/utk/papers/mpi-book/mpi-book.html**  
Referencia MPI

  
  

  4. **http://people.ac.upc.es/jesus/multiprocesadores**  
Transparencias de clase

  
  

## Capacitats prèvies

(-)

  

Compartir

[ ![Share](http://s7.addthis.com/static/btn/sm-plus.gif) ](bookmark.php.md
"Compartir")

  * [La Facultat ](fib/centre.html.md)
  * [Enginyeria informàtica ](fib/estudiar-enginyeria-informatica.html.md)
    * [Accés als estudis ](fib/estudiar-enginyeria-informatica/acces.html.md)
    * [Pla d'estudis Grau ](fib/estudiar-enginyeria-informatica/grau.html.md)
    * [Especialitats del Grau ](fib/estudiar-enginyeria-informatica/especialitats-grau.html.md)
    * [Assignatures del Grau ](fib/estudiar-enginyeria-informatica/assignatures.html.md)
    * [Treball Final de Grau ](fib/estudiar-enginyeria-informatica/treball-final-grau.html.md)
    * [Doble titulació ](fib/estudiar-enginyeria-informatica/doble-titulacio.html.md)
    * [Premis ](fib/estudiar-enginyeria-informatica/premis.html.md)
    * [Normatives Acadèmiques ](fib/estudiar-enginyeria-informatica/normatives.html.md)
    * [Exàmens finals Grau ](fib/estudiar-enginyeria-informatica/examens-finals.html.md)
    * [Exàmens parcials Grau ](fib/estudiar-enginyeria-informatica/examens-parcials.html.md)
    * [Horaris Grau ](fib/estudiar-enginyeria-informatica/horaris.html.md)
    * [Enginyeries pla 2003 ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003.html.md)
      * [Enginyeria en Informàtica ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/EI.html.md)
      * [Enginyeria Tècnica en Informàtica de Gestió ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/ETIG.html.md)
      * [Enginyeria Tècnica en Informàtica de Sistemes ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/ETIS.html.md)
      * **[Assignatures ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/assignatures.html.md)**
      * [Projecte final de carrera ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/PFC.html.md)
      * [Extinció titulació Pla 2003 ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/extinci--titulacions-primer-i-segon-cicle.html.md)
      * [Crèdits de lliure elecció ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/ALE.html.md)
      * [Normatives ](fib/estudiar-enginyeria-informatica/enginyeries-pla-2003/normatives.html.md)
    * [Matrícula ](fib/estudiar-enginyeria-informatica/matricula.html.md)
    * [Calendari lectiu ](fib/estudiar-enginyeria-informatica/calendari-lectiu.html.md)
  * [Ciència i Enginyeria de Dades ](fib/Ciencia-i-enginyeria-de-dades.html.md)
  * [Bioinformàtica ](fib/bioinformatica.html.md)
  * [Màsters ](fib/masters.html.md)
  * [Tràmits secretaria ](fib/tramits.html.md)
  * [Serveis i equipaments ](fib/serveis.html.md)
  * [Mobilitat ](fib/erasmus.html.md)
  * [Universitat-Empresa ](fib/empresa.html.md)
  * [Vida universitària ](fib/vida.html.md)
  * [Projectes finals ](fib/projectes-finals.html.md)

Username Password

[ ![Entra amb el carnet
UPC](/docroot/fib/imatges/carnet_upc_ca.gif)](cas/login-cert.md)

  * [Notícies](fib/noticies.md)
  * [Agenda](fib/agenda.md)

  

![logo FIB](/docroot/fib/imatges/Logo_FIB_inferior.gif) © Facultat
d'Informàtica de Barcelona \- [ Contacte](fib/mail.md) \-
[![](/docroot/fib/imatges/feed-icon-16x16.gif) RSS](fib/rss.rss.md) Aquest web
utilitza cookies pròpies per oferir una millor experiència i servei. En
continuar amb la navegació entenem que acceptes la nostra [política de
cookies](avis-legal/politica-de-cookies.md).  
[Versió clàssica](fib/estudiar-enginyeria-informatica/enginyeries-
pla-2003/assignatures/MP.html.md) [Versió mòbil](fib/estudiar-enginyeria-
informatica/enginyeries-pla-2003/assignatures/MP.html.md)

