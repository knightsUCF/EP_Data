# Prestige Preprocessing Methodology

ChIP-seq and RNA-seq preprocessing is covered on page 15 of the Prestige paper:

https://genome.cshlp.org/content/early/2013/11/06/gr.164079.113.full.pdf


**ChIP-seq data processing** 

Publicly available H3K4me1 ChIP-seq and matched input data files were obtained for the 12
cells lines of the comparator set (see Supplemental Table S2A) and aligned to hg18 with BWA
(Li and Durbin 2009). Duplicate reads were removed with SAMtools (Li et al. 2009). Matched
inputs for each sample were trimmed to 10 million reads prior to alignment and used for peakcalling with MACS (Zhang et al. 2008). Called peaks were used to generate a list of potential
enhancer sites. All identified ChIP enriched peaks across the 12 cell lines were then compiled
and overlapping peaks were collapsed resulting in 309,713 regions. The maximum signal was
then retrieved in each region across all 12 cell lines and the results were tabled. To normalize for
read depth and varying enrichment across ChIP samples, maximum signals were quantile
normalized. Shannon entropy scoring was performed on normalized maximum signals to
quantify cell type-specificity for each region.

**RNA-seq data processing**

Publicly available RNA-seq data were obtained for all 12 cell lines of the comparator set
(Supplemental Fig. S2A). Reads were aligned to hg18 with TopHat (Trapnell et al. 2009)
allowing for a maximum of 10 multiple alignments. Gene expression score FPKM (fragments
per kilobase per million reads) was determined for all Refseq genes using Cufflinks (Trapnell et
al. 2010). An FPKM threshold of 0.3 was chosen to balance the false discovery and false
negative rates as described by Ramsköld et al. (Ramskold et al. 2009). Genes with FPKMs
below 0.3 were rounded to zero and then the results were tabled. The data obtained for Neural
Precursor Cells (NPCs) was sequenced on the ABI SOLiD platform, and was aligned using
TopHat modified for colorspace reads. Given the different platforms used in sequencing the 12
samples, FPKMs were quantile normalized. Shannon entropy scoring was then performed on the
normalized FPKMs to score cell line specificity of gene expression. 