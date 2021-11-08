# Overview

The goal of this report is to locate pairs of RNA-Seq (similar to the format used in Prestige) and H3K27ac data from the Cistrome DB.

# Prestige RNA-Seq Background

Prestige paper: https://genome.cshlp.org/content/early/2013/11/06/gr.164079.113.full.pdf

<i>
"RNA-seq data processing Publicly available RNA-seq data were obtained for all 12 cell lines of the comparator set (Supplemental Fig. S2A). Reads were aligned to hg18 with TopHat (Trapnell et al. 2009) allowing for a maximum of 10 multiple alignments. Gene expression score FPKM (fragments per kilobase per million reads) was determined for all Refseq genes using Cufflinks (Trapnell et 16
al. 2010). An FPKM threshold of 0.3 was chosen to balance the false discovery and false negative rates as described by Ramsköld et al. (Ramskold et al. 2009). Genes with FPKMs below 0.3 were rounded to zero and then the results were tabled. The data obtained for Neural Precursor Cells (NPCs) was sequenced on the ABI SOLiD platform, and was aligned using TopHat modified for colorspace reads. Given the different platforms used in sequencing the 12 samples, FPKMs were quantile normalized. Shannon entropy scoring was then performed on the normalized FPKMs to score cell line specificity of gene expression."
</i>

# RNA-Seq Data

The IDs of the RNA-Seq data can be found on pg 36 of the supplemental material from the Prestige paper:

https://genome.cshlp.org/content/suppl/2013/11/11/gr.164079.113.DC1/Supplemental_Text_Figs_Tables.pdf


The same GSE used for all cell line data except for NPC (GSE16256): GSE26284

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE26284

The individual RNA-Seq cell samples are identified by a GSM ID: (total of 183.2 GB of compressed data)

```	
GSM646522	Gingeras_GM12878_cell_total
GSM646523	Gingeras_K562_cell_total
GSM646524	Gingeras_K562_cytosol_longPolyA
GSM758559	CSHL_RnaSeq_GM12878_cell_longPolyA (superseded by GSE86658)
GSM758560	CSHL_RnaSeq_GM12878_cytosol_longPolyA (superseded by GSE90222)
GSM758561	CSHL_RnaSeq_AG04450_cell_longPolyA (superseded by GSE78585)
GSM758562	CSHL_RnaSeq_BJ_cell_longPolyA (superseded by GSE90221)
GSM758563	CSHL_RnaSeq_HUVEC_cell_longPolyA (superseded by GSE78588)
GSM758564	CSHL_RnaSeq_A549_cell_longPolyA (superseded by GSE86657)
GSM758565	CSHL_RnaSeq_HUVEC_nucleus_longPolyA (superseded by GSE78590)
GSM758566	CSHL_RnaSeq_H1-hESC_cell_longPolyA (superseded by GSE90225)
GSM758567	CSHL_RnaSeq_HepG2_cell_longNonPolyA (superseded by GSE90229)
GSM758568	CSHL_RnaSeq_HepG2_nucleus_longPolyA (superseded by GSE90228)
GSM758569	CSHL_RnaSeq_HUVEC_cytosol_longPolyA (superseded by GSE78589)
GSM758570	CSHL_RnaSeq_H1-hESC_cytosol_longPolyA (superseded by GSE90226)
GSM758571	CSHL_RnaSeq_HMEC_cell_longPolyA (superseded by GSE78586)
GSM758572	CSHL_RnaSeq_GM12878_cell_longNonPolyA (superseded by GSE90223)
GSM758573	CSHL_RnaSeq_H1-hESC_cell_longNonPolyA (superseded by GSE90224)
GSM758574	CSHL_RnaSeq_H1-hESC_nucleus_longPolyA (superseded by GSE90227)
GSM758575	CSHL_RnaSeq_HepG2_cell_longPolyA (superseded by GSE86659)
GSM758576	CSHL_RnaSeq_HepG2_cytosol_longPolyA (superseded by GSE90230)
GSM758577	CSHL_RnaSeq_K562_cell_longNonPolyA (superseded by GSE90231)
GSM758578	CSHL_RnaSeq_HSMM_cell_longPolyA (superseded by GSE78587)
GSM765386	CSHL_RnaSeq_GM12878_nucleus_longPolyA (superseded by GSE90233)
GSM765387	CSHL_RnaSeq_K562_nucleus_longPolyA (superseded by GSE90236)
GSM765388	CSHL_RnaSeq_MCF-7_cell_longPolyA (superseded by GSE90237)
GSM765389	CSHL_RnaSeq_NHLF_cell_longNonPolyA (superseded by GSE78598)
GSM765390	CSHL_RnaSeq_K562_nucleoplasm_total (superseded by GSE90240)
GSM765391	CSHL_RnaSeq_HSMM_cell_longNonPolyA (superseded by GSE78597)
GSM765392	CSHL_RnaSeq_K562_chromatin_total (superseded by GSE90238)
GSM765393	CSHL_RnaSeq_K562_nucleolus_total (superseded by GSE90239)
GSM765394	CSHL_RnaSeq_NHLF_cell_longPolyA (superseded by GSE78595)
GSM765395	CSHL_RnaSeq_SK-N-SH_RA_cell_longPolyA (superseded by GSE90232)
GSM765396	CSHL_RnaSeq_AG04450_cell_longNonPolyA (superseded by GSE78599)
GSM765397	CSHL_RnaSeq_HMEC_cell_longNonPolyA (superseded by GSE78596)
GSM765398	CSHL_RnaSeq_NHEK_cell_longNonPolyA (superseded by GSE78591)
GSM765399	CSHL_RnaSeq_NHEK_nucleus_longPolyA (superseded by GSE78592)
GSM765400	CSHL_RnaSeq_NHEK_cytosol_longPolyA (superseded by GSE78593)
GSM765401	CSHL_RnaSeq_NHEK_cell_longPolyA (superseded by GSE78594)
GSM765402	CSHL_RnaSeq_HeLa-S3_cell_longPolyA (superseded by GSE86661)
GSM765403	CSHL_RnaSeq_HeLa-S3_nucleus_longPolyA (superseded by GSE90235)
GSM765404	CSHL_RnaSeq_HeLa-S3_cytosol_longPolyA (superseded by GSE90234)
GSM765405	CSHL_RnaSeq_K562_cell_longPolyA (superseded by GSE86660)
GSM767838	CSHL_RnaSeq_HeLa-S3_cytosol_longNonPolyA (superseded by GSE90255)
GSM767839	CSHL_RnaSeq_HUVEC_cytosol_longNonPolyA
GSM767840	CSHL_RnaSeq_HepG2_cytosol_longNonPolyA (superseded by GSE90256)
GSM767841	CSHL_RnaSeq_H1-hESC_nucleus_longNonPolyA (superseded by GSE90253)
GSM767842	CSHL_RnaSeq_H1-hESC_cytosol_longNonPolyA (superseded by GSE90252)
GSM767843	CSHL_RnaSeq_NHEK_cytosol_longNonPolyA (superseded by GSE78602)
GSM767844	CSHL_RnaSeq_K562_nucleus_longNonPolyA (superseded by GSE90250)
GSM767845	CSHL_RnaSeq_SK-N-SH_RA_cell_longNonPolyA (superseded by GSE90251)
GSM767846	CSHL_RnaSeq_NHEK_nucleus_longNonPolyA (superseded by GSE78603)
GSM767847	CSHL_RnaSeq_HeLa-S3_cell_longNonPolyA (superseded by GSE90247)
GSM767848	CSHL_RnaSeq_HeLa-S3_nucleus_longNonPolyA (superseded by GSE90246)
GSM767849	CSHL_RnaSeq_K562_cytosol_longNonPolyA (superseded by GSE90249)
GSM767850	CSHL_RnaSeq_HepG2_nucleus_longNonPolyA (superseded by GSE90248)
GSM767851	CSHL_RnaSeq_MCF-7_cell_longNonPolyA (superseded by GSE90241)
GSM767852	CSHL_RnaSeq_GM12878_cytosol_longNonPolyA (superseded by GSE90244)
GSM767853	CSHL_RnaSeq_GM12878_nucleus_longNonPolyA (superseded by GSE90245)
GSM767854	CSHL_RnaSeq_A549_cell_longNonPolyA (superseded by GSE90242)
GSM767855	CSHL_RnaSeq_BJ_cell_longNonPolyA (superseded by GSE90243)
GSM767856	CSHL_RnaSeq_HUVEC_cell_longNonPolyA (superseded by GSE78600)
GSM767857	CSHL_RnaSeq_HUVEC_nucleus_longNonPolyA (superseded by GSE78601)
GSM840136	CSHL_RnaSeq_K562_cell_total
GSM840137	CSHL_RnaSeq_K562_cytosol_longPolyA (superseded by GSE90220)
GSM840138	CSHL_RnaSeq_GM12878_cell_total
GSM981243	CSHL_RnaSeq_IMR90_cell_total (superseded by GSE90257)
GSM981244	CSHL_RnaSeq_IMR90_cytosol_longPolyA (superseded by GSE90260)
GSM981245	CSHL_RnaSeq_MCF-7_nucleus_longPolyA (superseded by GSE90261)
GSM981246	CSHL_RnaSeq_A549_cytosol_longPolyA (superseded by GSE90258)
GSM981247	CSHL_RnaSeq_A549_nucleus_longPolyA (superseded by GSE90259)
GSM981248	CSHL_RnaSeq_IMR90_nucleus_longPolyA (superseded by GSE90262)
GSM981249	CSHL_RnaSeq_IMR90_cell_longPolyA (superseded by GSE90263)
GSM981250	CSHL_RnaSeq_SK-N-SH_nucleus_longPolyA (superseded by GSE90265)
GSM981251	CSHL_RnaSeq_SK-N-SH_cytosol_longPolyA (superseded by GSE90264)
GSM981252	CSHL_RnaSeq_MCF-7_cytosol_longPolyA (superseded by GSE90267)
GSM981253	CSHL_RnaSeq_SK-N-SH_cell_longPolyA (superseded by GSE90266)
GSM981254	CSHL_RnaSeq_CD20+_cell_longNonPolyA (superseded by GSE90269)
GSM981255	CSHL_RnaSeq_HPC-PL_cell_total (superseded by GSE78604)
GSM981256	CSHL_RnaSeq_CD20+_cell_longPolyA (superseded by GSE90268)
GSM981257	CSHL_RnaSeq_CD34+_Mobilized_cell_total (superseded by GSE78605)
GSM981258	CSHL_RnaSeq_HFDPC_cell_total (superseded by GSE78606)
GSM981259	CSHL_RnaSeq_Monocytes-CD14+_cell_longNonPolyA (superseded by GSE90270)
GSM981260	CSHL_RnaSeq_hMSC-AT_cell_total (superseded by GSE90271)
```


# Analysis of RNA-Seq used by Prestige

Taking one of the cell RNA-Seq samples, we have:

```
GSM758559	CSHL_RnaSeq_GM12878_cell_longPolyA (superseded by GSE86658)
GSM758560	CSHL_RnaSeq_GM12878_cytosol_longPolyA (superseded by GSE90222)
```

GSE86658:

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE86658

```
Status	Public on Oct 14, 2016
Title	polyA mRNA RNA-seq from GM12878 (ENCSR000COQ)
Project	ENCODE
Organism	Homo sapiens
Experiment type	Expression profiling by high throughput sequencing
Summary	The libraries contained in this experiment come from the whole cell fraction of independent growths of cell line GM12878. They are stranded PE76 Illumina GAIIx RNA-Seq libraries from rRNA-depleted Poly-A+ RNA > 200 nucleotides in size.
```
Cytosol data: 

https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE90222

```
Title	polyA mRNA RNA-seq from GM12878 (ENCSR000COR)
Project	ENCODE
Organism	Homo sapiens
Experiment type	Expression profiling by high throughput sequencing
Summary	The libraries contained in this experiment come from the cytoplasmic fraction of independent growths of cell line GM12878. They are stranded PE76 Illumina GAIIx RNA-Seq libraries from rRNA-depleted Poly-A+ RNA > 200 nucleotides in size.
```


So the RNA-Seq data type we are looking to match from Prestige is: "polyA mRNA RNA-seq"

We can now run this with our web crawler to mine the entire NCBI database.

Now all we have to do is specify the "polyA mRNA" search keywords, and the NCBI web crawler will search all 400 unique cell lines by h3k27ac histones from the Cistrome DB. Although we are expecting far less than 400 cell lines, we have the ability to do an exhaustive search for all the 400 unique h3k27ac histones from the Cistrome DB and avoid human error.

# Final Ouput Data

Using the web crawler method there are a total of 14 polyA mRNA RNA-seq cell lines. Each of these cell lines has a corresponding histone h3k27ac pair in the Cistrome DB. In addition we have multiple replicates of each sample for normalization purposes, for a total of 186 samples.



```
Cell line,RNA-Seq link
MCF-7 - 1,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400231
MCF-7 - 2,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400230
MCF-7 - 3,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400219
MCF-7 - 4,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400218
MCF-7 - 5,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400175
MCF-7 - 6,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400174
MCF-7 - 7,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072528
MCF-7 - 8,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072527
K562 - 9,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2471355
K562 - 10,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2471354
K562 - 11,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400173
K562 - 12,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400172
K562 - 13,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400143
K562 - 14,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400142
K562 - 15,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343894
K562 - 16,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343893
K562 - 17,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343892
K562 - 18,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343891
K562 - 19,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343836
K562 - 20,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343835
K562 - 21,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343815
K562 - 22,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343814
K562 - 23,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343645
K562 - 24,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343644
K562 - 25,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308419
K562 - 26,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308418
K562 - 27,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072371
K562 - 28,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072370
K562 - 29,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072367
K562 - 30,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072366
K562 - 31,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072363
K562 - 32,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072362
A549 - 33,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453354
A549 - 34,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453353
A549 - 35,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453352
A549 - 36,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453351
A549 - 37,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453350
A549 - 38,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453349
A549 - 39,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453332
A549 - 40,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453331
A549 - 41,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421935
A549 - 42,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421934
A549 - 43,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421933
A549 - 44,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421932
A549 - 45,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421786
A549 - 46,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421785
A549 - 47,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421784
A549 - 48,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421783
A549 - 49,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421767
A549 - 50,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421766
A549 - 51,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421765
A549 - 52,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421764
A549 - 53,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421760
A549 - 54,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421759
A549 - 55,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421758
A549 - 56,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421757
A549 - 57,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421703
A549 - 58,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421702
A549 - 59,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421701
A549 - 60,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421700
A549 - 61,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421693
A549 - 62,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421692
A549 - 63,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421691
A549 - 64,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421617
A549 - 65,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421616
A549 - 66,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421615
A549 - 67,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421614
A549 - 68,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421579
A549 - 69,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421578
A549 - 70,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421577
A549 - 71,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421576
A549 - 72,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421536
A549 - 73,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421535
A549 - 74,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421534
A549 - 75,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421516
A549 - 76,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421515
A549 - 77,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421514
A549 - 78,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421513
A549 - 79,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421487
A549 - 80,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421486
A549 - 81,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421485
A549 - 82,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421484
A549 - 83,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421444
A549 - 84,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421443
A549 - 85,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421442
A549 - 86,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2421441
A549 - 87,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400215
A549 - 88,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400214
A549 - 89,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400213
A549 - 90,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400212
A549 - 91,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308413
A549 - 92,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308412
GM12878 - 93,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400167
GM12878 - 94,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400166
GM12878 - 95,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400147
GM12878 - 96,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400146
GM12878 - 97,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308415
GM12878 - 98,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308414
GM12878 - 99,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072359
GM12878 - 100,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072358
GM12878 - 101,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072355
GM12878 - 102,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072354
GM12878 - 103,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072351
GM12878 - 104,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072350
H1 - 105,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400155
H1 - 106,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400154
H1 - 107,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400153
H1 - 108,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400152
HeLa - 109,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400171
HeLa - 110,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400170
HeLa - 111,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400169
HeLa - 112,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400168
HeLa - 113,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308421
HeLa - 114,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308420
Jurkat - 115,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453330
Jurkat - 116,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453329
Ishikawa - 117,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453340
Ishikawa - 118,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453339
Ishikawa - 119,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453338
Ishikawa - 120,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453337
Ishikawa - 121,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453336
Ishikawa - 122,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453335
Ishikawa - 123,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453334
Ishikawa - 124,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453333
HepG2 - 125,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400320
HepG2 - 126,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400319
HepG2 - 127,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400161
HepG2 - 128,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400160
HepG2 - 129,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400157
HepG2 - 130,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400156
HepG2 - 131,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2344354
HepG2 - 132,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2344353
HepG2 - 133,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343856
HepG2 - 134,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343855
HepG2 - 135,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343830
HepG2 - 136,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343829
HepG2 - 137,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343162
HepG2 - 138,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343161
HepG2 - 139,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343098
HepG2 - 140,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2343097
HepG2 - 141,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308417
HepG2 - 142,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308416
HepG2 - 143,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072618
HepG2 - 144,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072617
SK-N-AS - 145,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453358
SK-N-AS - 146,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453357
SK-N-AS - 147,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400229
SK-N-AS - 148,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400228
SK-N-AS - 149,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400227
SK-N-AS - 150,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400226
SK-N-AS - 151,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400225
SK-N-AS - 152,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400224
SK-N-AS - 153,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400165
SK-N-AS - 154,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400164
SK-N-AS - 155,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072558
SK-N-AS - 156,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072557
SK-N-AS - 157,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072524
SK-N-AS - 158,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072523
SK-N-AS - 159,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072520
SK-N-AS - 160,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072519
SK-N-AS - 161,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072510
SK-N-AS - 162,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072509
SK-N-SH - 163,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453358
SK-N-SH - 164,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2453357
SK-N-SH - 165,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400229
SK-N-SH - 166,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400228
SK-N-SH - 167,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400227
SK-N-SH - 168,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400226
SK-N-SH - 169,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400225
SK-N-SH - 170,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400224
SK-N-SH - 171,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400165
SK-N-SH - 172,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400164
HT1080 - 173,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072504
HT1080 - 174,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072503
HT1080 - 175,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072494
HT1080 - 176,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072493
HeLa-S3 - 177,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400171
HeLa-S3 - 178,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400170
HeLa-S3 - 179,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400169
HeLa-S3 - 180,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2400168
HeLa-S3 - 181,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308421
HeLa-S3 - 182,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2308420
SK-N-DZ - 183,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072558
SK-N-DZ - 184,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072557
SK-N-DZ - 185,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072520
SK-N-DZ - 186,https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2072519
```

<h3>Cistrome DB Histone Data</h3>

Here is the available Cistrome DB Histone Data corresponding to the above RNA-Seq. The data is ordered in terms of frequency. 

When tasked with downloading the data, we can match the below histone BED ranges by name with the above RNA-Seq.

```
Cell_line,Count
MCF-7,68
K562,57
A549,53
HCT-116,53
GM12878,34
MCF-10A,31
LNCaP,27
IMR90,19
H1,19
HT29,18
Pfeiffer,17
HUES64,16
HeLa,15
CyT49,14
D-341,12
MDA-MB-231,11
BICR31,11
H9,11
MRC5,11
Toledo,10
NHEK,10
JHU-06,10
SUM159PT,10
MD-901,9
Raji,9
786-O,9
LCL,9
Jurkat,9
Ishikawa,8
HepG2,8
A673,7
WIBR3,7
CHL-1,7
CFPAC-1,7
VCaP,6
hMADS-3,6
PANC-1,6
SHEP-21N,6
SW480,5
MV4-11,5
HCC95,5
THP-1,5
T47D,5
L3.6,5
P493-6,5
GM19239,5
PC-9,5
ZR-75-30,5
CUTLL1,5
MS1,5
HCC1954,5
ZR-75-1,5
H1299,5
KATO III,5
SK-N-MC,5
D283 Med,5
MOLM-14,5
H2009,5
A375,5
BE2-C,5
GM18505,4
KB Cell,4
293T-Rex,4
GM19193,4
HEK293A,4
RWPE1,4
GM19099,4
TIME,4
SH-SY5Y,4
JMSU-1,4
C4-2B,4
GM19147,4
BJ,4
G-401,4
OCI-Ly1,4
TOV-21G,4
MKN7,4
GM19238,4
HL-60,4
MIA PaCa-2,4
GM19240,3
NHLF,3
SK-N-AS,3
GM18508,3
GM18502,3
LTED,3
KMS11,3
PC-3,3
iPS DF 19.11,3
KOPT-K1,3
NGP,3
GM18499,3
DL23,3
SKNO-1,3
GM12891,3
SK-N-SH,3
GM18516,3
TE-7,3
COLO 205,3
MOLT-4,3
GM12892,3
HEK293,3
TC-797,3
GM18522,3
Huh7,3
GM18486,3
A-498,3
GM18498,3
GM19114,3
DND-41,3
GM18507,3
HuCCT1,2
GM18517,2
HCT-15,2
DKO1,2
YCC-22,2
RT112,2
MG-63,2
OCUM-1,2
7250,2
GM19210,2
SF8628,2
GM19127,2
GM18504,2
COLO-741,2
MB468,2
CLB-Ga,2
SUM149,2
GM19116,2
GM19222,2
IM95,2
SUM159R,2
IOE11,2
HT1080,2
TTC-549,2
TTC1240,2
GM18520,2
GM19141,2
GM18870,2
GM19119,2
UACC812,2
GM18862,2
YCC3,2
GM18511,2
T.T,2
GM18853,2
BT-16,2
90-8TL,2
GM19093,2
FT246,2
AGS,2
GM19152,2
COLO-320,2
LNCaP-abl,2
LIS2,2
HEK,2
LREX',2
GM12890,2
HCC1937,2
GM19200,2
GM19144,2
GM19153,2
GM19160,2
Reh,2
N87,2
GM19159,2
SKMEL5,2
NB69,2
LP-1,2
GM18519,2
NCI-H2087,2
SNU-16,2
H358,2
GM18951,2
GM18913,2
GM10847,2
EEC16,2
GM18861,2
GM19137,2
MOLM-13,2
1015c,2
GM19130,2
IOE4,2
GM19101,2
U2OS,2
H3122,2
SKMEL2,2
GM17942,2
Rj2.2.5,2
iPS C1,2
GM2630,2
GM19131,2
HUES6,2
GM19209,2
GM19138,2
GM18501,2
GM18916,2
MB231,2
ID00016,2
PrEC,2
FU97,2
MutuI,2
GM18912,2
GM18852,2
GM19098,2
GM18855,2
SKBR-3,2
MM.1S,2
KELLY,2
GM18909,2
GM2255,2
GM2610,2
LHCN-M2,2
MB361,2
SUM149R,2
CHP-134,2
NCC-59,2
76NF2V,2
FT33,2
CAL51-MCF7,2
GM19204,2
GM2588,2
GM19140,2
EBC-1,2
SNU-1750,2
HS-ES-2M,2
SF268,2
RERF-GC-1B,2
GM18526,2
IMEC,2
GM19201,2
MO1043,2
GM19143,2
YCC-21,2
LOUCY,2
WIS2,2
MB436,2
YCC-7,2
ZNF532-NUT 24335,2
MV4;11,2
iPS cells,2
GM18856,2
RS4,2
LoVo,1
RMS209,1
SK-N-FI,1
GM18510,1
GM19207,1
Capan-1,1
MM1.S,1
V457,1
V410,1
HSC4,1
GM06990,1
GI-ME-N,1
NCI-0082,1
U87,1
OCI-Ly4,1
TL-Om1,1
V411,1
NCI-H69,1
RKO,1
COLO 679,1
NS129,1
ID00015,1
LAN-1,1
MV4-11R,1
CJM,1
501-Mel,1
SKMEL30,1
IMR-32,1
TE6,1
SJNB-1,1
143B,1
SW620,1
V703,1
RMS206,1
SU-DHL6,1
Calu-3,1
293T,1
V852,1
V968,1
ID00014,1
RPMI-8402,1
C6661,1
KYSE-510,1
LM7,1
OCI-Ly3,1
GI-CA-N,1
BICR6,1
V576,1
SJNB-6,1
SNU016,1
V1074,1
HFF,1
V206,1
GM19225,1
IMR-5/75,1
ALL-SIL,1
TCam-2,1
LY1,1
TT,1
Caco-2,1
Rh4,1
697,1
GM18859,1
H7,1
NCI-0075,1
RMS008,1
SF7761,1
P12-ICHIKAWA,1
SKmel239,1
V1051,1
GM19190,1
V940,1
HOS,1
HKC8,1
YD8,1
CLB-Pe,1
BHY,1
Hu09,1
Detroit562,1
SJNB-12,1
HEK293T,1
GLC-16,1
LS174T,1
NS134,1
PF382,1
LNAR',1
GM19206,1
V1106,1
V456,1
RPM-MC,1
NHDF-Ad,1
M112,1
GSU,1
GM18858,1
ATL-2,1
V481,1
D1 ORL UVA,1
GM18907,1
Colo-205,1
5637,1
MDA-MB-468,1
RH5,1
SH-EP,1
DLD-1,1
Rh18,1
SET2,1
CCRF-CEM,1
NB-1643,1
AG04450,1
GM19257,1
MKN45,1
TE10,1
HCC827,1
H128,1
MLL-AF9,1
SCMC,1
CTR,1
V429,1
CAL33,1
GM19203,1
GM19092,1
UACC-257,1
GRANTA-519,1
BG01,1
RMS237,1
V855,1
V866,1
V1024,1
V784,1
VACO 5,1
BICR16,1
SW48,1
SNU719,1
V1058,1
TR14,1
NCI-H82,1
SJNB-3,1
LS180,1
MSTO,1
DU-528,1
HUES48,1
SNU638,1
MNNG,1
HK1,1
CHP-212,1
MKN1,1
U266B1,1
BT-549,1
H2171,1
SKmel147,1
BJEL,1
SJNB-8,1
iPS DF 6.9,1
HT-3,1
HeLa-S3,1
T24,1
NCCIT,1
HBL1,1
V432,1
OVCAR3,1
MOLT-3,1
SK-OV-3,1
LOX-IMVI,1
KARPAS-422,1
Ramos,1
PEER,1
DU145,1
V9P,1
SEM,1
HNE1,1
RMS216,1
V1009,1
BJELM,1
GM19171,1
V389,1
RMS238,1
SK-N-DZ,1
GM19223,1
```

```

Cell Line	Data: https://genome.ucsc.edu/ENCODE/dataMatrix/encodeDataMatrixHuman.html
GM12878	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=GM12878&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
H1-hESC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=H1-hESC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
K562	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=K562&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
A549	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=A549&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
CD20+	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=CD20%2B&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HeLa-S3	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HeLa-S3&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HepG2	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HepG2&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HUVEC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HUVEC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
IMR90	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=IMR90&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
LHCN-M2	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=LHCN-M2&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
MCF-7	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=MCF-7&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
Monocytes CD14+	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=Monocytes-CD14%2B&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
SK-N-SH	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=SK-N-SH&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
AG04450	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=AG04450&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
BE2-C	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=BE2_C&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
BJ	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=BJ&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
CD23+ Mobilized 	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=CD34%2B_Mobilized&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
ECC-1	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=ECC-1&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
GM12891	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=GM12891&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
GM12892	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=GM12892&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HAoAF	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HAoAF&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HAoEC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HAoEC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HCH	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HCH&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HCT-116	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HCT-116&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HFDPC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HFDPC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HMEC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HMEC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HMEpC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HMEpC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
hMNC-CB	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=hMNC-CB&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
hMNC-PB	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=hMNC-PB&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
hMSC-AT	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=hMSC-AT&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
hMSC-BM	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=hMSC-BM&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
hMSC-UC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=hMSC-UC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HOB	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HOB&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HPC-PL	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HPC-PL&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HPIEpC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HPIEpC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HSaVEC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HSaVEC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HSMM	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HSMM&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HVMF	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HVMF&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
HWP	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=HWP&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
Jurkat	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=Jurkat&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
NHDF	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=NHDF&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
NHEK	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=NHEK&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
NHEM M2	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=NHEM_M2&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
NHEM.f M2	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=NHEM.f_M2&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
NHLF	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=NHLF&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
PANC-1	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=PANC-1&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
PFSK-1	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=PFSK-1&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
SK-N-SH	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=SK-N-SH_RA&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
SkMC	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=SkMC&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
T-47D	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=T-47D&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
U87	https://genome.ucsc.edu/cgi-bin/hgFileSearch?db=hg19&fsFileType=Any&hgfs_Search=search&tsCurTab=advancedTab&hgt_tsPage=&tsName=&tsDescr=&tsGroup=Any&hgt_mdbVar1=dataType&hgt_mdbVal1=RnaSeq&hgt_mdbVar2=cell&hgt_mdbVal2=U87&hgt_mdbVar3=rnaExtract&hgt_mdbVal3=total&hgt_mdbVal3=longPolyA&hgt_mdbVal3=longNonPolyA&hgt_mdbVal3=polyA&hgt_mdbVar4=view&hgt_mdbVal4=Any&hgt_mdbVar5=[]&hgt_mdbVar6=[]
```
