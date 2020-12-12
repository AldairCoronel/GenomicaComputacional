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

**Respuesta 4:**

# Parte IV.

**Respuesta 1:**

**Respuesta 2:**

**Respuesta 3:**

**Respuesta 4:**

**Respuesta 5:**

**Respuesta 6:**

## Referencias
- Pareek, C.S., Smoczynski, R. & Tretyn, A. Sequencing technologies and genome sequencing. J Appl Genetics 52, 413–435 (2011). https://doi.org/10.1007/s13353-011-0057-x
- Kchouk, M; Gibrat, J y  Elloumi, M. (2017).Generations of Sequencing Technologies: From First to Next Generation. Biol Med. DOI: 10.4172/0974-8369.1000395
