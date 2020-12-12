# Comandos de la Práctica 03
## Equipo 04
### Integrante 1: Adrián García Pérez
### Integrante 2: Aldair Coronel Ruiz
### Integrante 3: Jorge Adrián Cid Chávez Cid
### Integrante 4: Liliana Bénitez Salazar
### Integrante 5: Gutierrez Cruz Abel Isaías
...

# Parte I.

**Respuesta 1:**
Plataforma/compañia | Longitud de reads | #reads x run | Tiempo | Costo x 10^6 bases | Error (%) | Química
--- | --- | --- | --- | --- | --- | ---
Primera generación |     
Sanger/Life technologies | 800 | 1 | 2 h | 2400 | 0.3 | Dideoxy terminator
Método de Maxam y Gilbert | 400 - 900 pb | 96 | 2 h | 500 $(0.5 $ x 1 kb) | 0.3 | Secuenciación por degradación química
Segunda generación |
454 GS FLX+/Roche | 700 | 1x10^6 | 24/48 h | 10 | 1 | Pyrosequencing
GS Junior/Roche | 500 | 1x10^5 | 18 h | 9 |  | Pyrosequencing
HiSeq/Illumina/1500 Gb | 2x150 | 5x10^9| 27/240 h | 0.1 | 0.8 | Reversible terminators
MiSeq/Illumina/15 Gb | 2x300 | 3x10^8 | 27 h | 0.13 | 0.8 | Reversible terminator
SOLiD/Life Technologies | 50 | 1x10^9 | 14 días | 0.13 | 0.1 | Ligation
Retrovolocity/BGI | 50 | 1x10^9 | 14 días | 0.01 | 0.01 | Nanoball/ligation
Ion Proton/Life Technologies | 200 | 6x10^7 | 2-5 h | 1 | 1.7 | Proton detection
Ion PGM/Life Technologies | 200 | 5x10^6 | 2-5 h | 1 | 1.7 | Proton detection
Tercera generación |  |  |  |  |  |
SMRT/Pac Bio/1 Gb | >10,000 | 1×106 | 1–2 h | 2 | 12.9 | Real-time SMS
Heliscope/Helicos/25 Gb | 35 | 7×109 | 8 days | 0.01 | 0.2 | Real-time SMS
Nanopore/Oxford Nanopore Technologies/1 Gb | >5000 | 6×104 | 48/72 h | <1 | 34 | Real-time SMS
Electron microscopy/ZS | 7200 | | 14 h | <0.01 | | Real-time SMS
# Parte II.

**Respuesta 1:**

Repositorio de secuencias: https://www.ebi.ac.uk/ena/browser/view/PRJEB5172

Convertir el archivo de `fastq` a `fasta`

gunzip -c ERR486827_1.fastq.gz | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > salida_1.fa
gunzip -c ERR486827_2.fastq.gz | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > salida_2.fa

**Respuesta 2:**

grep -c "^>" ena_files/ERR486827/salida_1.fa
>398824

grep -c "^>" ena_files/ERR486827/salida_2.fa
>398824

**Respuesta 3:**

El promedio de la longitud de las secuencias para ERR486827/salida_1.fa es igual a 150

# Parte III.

**Respuesta 1:**

>chmod +x fastqc

**Respuesta 2:**

Comando para poder ejecutar fastqc desde cualquier lado:
> export PATH=$PATH:/home/adrian/Downloads/FastQC/

Creando el script:
>nano fastqc_run.sh

>chmod +x fastqc_run.sh

>./fastqc_run.sh

**Respuesta 3:**

Visualizando los HTML:
>firefox ERR486827_1_fastqc.html

>firefox ERR486827_2_fastqc.html

Después de revisar los archivos con formato html, se obtiene la siguiente información:

El gráfico de "Per base sequence quality" se distingue que:

<ul>
<li> En el eje X, se representa las bases de las lecturas y cada lectura tiene 150 bases. </li>
<li> En el Y, se representan las calidades 0-40, distinguiéndose tres zonas: </li>
<ul>
  <li> Zona verde: 28-40. Corresponden a una muy buena calidad. </li>
  <li> Zona naranja: 20-28. Corresponden a una zona de calidad intermedia. </li>
  <li> Zona roja: 0-20. Corresponden a una zona de mala calidad. </li>
</ul>
</ul>

Se concluye que las calidades asignadas a todas las bases (150) que son muy buenas,
ya que se encuentran en la región verde y los cuartiles que aparecen son
significativamente pequeños.


El gráfico de *Per sequence quality scores* nos indica que existen más de 300K lecturas
con una calidad entorno a 37 y 38 y ninguna lectura con calidad < a 27 (ninguna lectura
con mala calidad). Por tanto, todas las lecturas caen en la región verde de buena
calidad y además existe un porcentaje significativamente pequeño de lecturas con
calidades entre 30 a 37.

El gráfico de *Per base sequence content* nos indica la proporción de cada una de
las bases que hay en la secuencia, notándose que la cantidad de A y T es igual
(líneas paralelas) y corresponde entre el 30 y 40 porciento, mientras que C y G
es proporcional y corresponde del 10 al 20 porciento.

**Respuesta 4:**

> cobertura = (398824 * 150)/580,000 = 103.14

M. genitalium G37T was selected as the type strain and in 1995, was the first
Mycoplasma to be whole genome sequenced [5] showing that it had, at the time,
the smallest known genome (0.58 Mb)

# Parte IV.

**Respuesta 1:**
#### Saccharomyces Cerevisiae
S.cerevisiae es un organismo eucariota, particularmente  una levadura  unicelular. Su genoma es de aproximadamente 12 Mb, organizado en 16 cromosomas.Como organismo modelo, S. cerevisiae, tienen las siguientes características:  Es fácil de obtener en  grandes cantidades,  y por otro lado,  posee un ciclo de vida que al incluir una fase sexual,  permite la realización de estudios que proveen información en el campo de la genética. Además, es muy importante en la industria alimenticia ya que posee la capacidad de llevar a cabo la fermentación alcohólica.

**Respuesta 2:**

La tecnología de secuenciación empleada para la obtención del genoma completo fue el método de Sanger, perteneciente a la primera generación. Básicamente, consiste en obtener 
muchas copias de un fragmento blanco de DNA. Los elementos base para llevar a cabo este método son: DNA polimerasa, un cebador, trinucleótidos, la muestra de DNA que se quiere secuenciar y otros elementos especiales que reciben el nombre de “terminadores de la cadena”, lo cuales están marcados con un fluorocromo de diferente color para cada base. Este método es muy parecido a la técnica de PCR con un cebador, en la cual se van a incorporar los ya mencionados dideoxinucleótidostrifosfato (ddNTPs) marcados con fluorescencia en el extremo 3’ de manera aleatoria. En la reacción, cada fluorocromo se encuentra asociado a un nucleótido en particular , el cual va a emitir una luz con una longitud de onda en específico, de esta manera se van a generar fragmentos de diferentes tamaños los cuales reciben el nombre de amplicones, los cuales van a ser separados en una columna de electroforesis capilar. Cabe destacar que esta emisión de fluorescencia es detectada por la excitación promovida de la luz de un láser, conectado a un software de secuenciación. (Instituto de Biotecnología, s.f)

**Respuesta 3:**

Después de revisar los archivos con formato html, se obtiene la siguiente información:

El gráfico de *Per base sequence quality* se distingue que:
En el eje X, se representa las bases de las lecturas y cada lectura tiene 151 bases.

En el Y, se representan las calidades 0-40, distinguiéndose tres zonas:
<ul>
<li> Zona verde: 28-40. Corresponden a una muy buena calidad. </li>
<li> Zona naranja: 20-28. Corresponden a una zona de calidad intermedia.  </li>
<li> Zona roja: 0-20. Corresponden a una zona de mala calidad. </li>
</ul>

Se concluye que las calidades asignadas a todas las bases (151) son muy buenas,
ya que se encuentran en la región verde y los cuartiles que aparecen son
significativamente pequeños.

El gráfico de *Per sequence quality scores* nos indica que existen aproxidamente
1.2M lecturas con una calidad entorno a 38 y 39 y ninguna lectura con calidad < a 28
(ninguna lectura con mala calidad) y por tanto, todas las lecturas caen en la región
verde de buena calidad. Además, existe un porcentaje significativamente pequeño de
lecturas con calidades entre 29 a 36.

El gráfico de *Per base sequence content* se observa un comportamiento irregular
hasta la base 19, de la base 20 en adelante se observa que la cantidad de A y T
es muy similar (líneas paralelas) y corresponde al 30 por ciento, mientras que C
y G es proporcional y corresponde del 20 por ciento.

**Respuesta 4:**

**Respuesta 5:**

**Respuesta 6:**

## Referencias
- Pareek, C.S., Smoczynski, R. & Tretyn, A. Sequencing technologies and genome sequencing. J Appl Genetics 52, 413–435 (2011). https://doi.org/10.1007/s13353-011-0057-x
- Kchouk, M; Gibrat, J y  Elloumi, M. (2017).Generations of Sequencing Technologies: From First to Next Generation. Biol Med. DOI: 10.4172/0974-8369.1000395
- Instituto de Biotecnología, UNAM. (s.f) Secuenciación de Ácidos Nucleicos.  Consultado el 11 de Diciembre 2020. Recuperado de: http://oldwww.ibt.unam.mx/computo/pdfs/met/secuenciacion_acidos_nucleicos.pdf
- Bioinfologics.(2019) W2rap: the WGS (Wheat) Robust Assembly Pipeline. Consultado el 11 de Diciembre 2020. Recuperado de: https://github.com/bioinfologics/w2rap/blob/master/README.md

