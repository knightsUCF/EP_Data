# Overview

I. ChIP-seq Prestige Processing Plan Steps

II. RNA-seq Prestige Processing Plan Steps

III. Quality Control

IV. Filtering





# I. ChIP-seq Prestige Processing Plan Steps

* trim matched inputs for each sample to 10 million reads prior to alignment

* align to the reference genome with BWA

* remove duplicate reads with SAMTools

* use MACS2 for peak calling

* peaks are used to identify enhancer sites

* compile and collapse the overlapping ChIP-seq peaks across the different cell lines

* retrieve the maximum signal in each region across all cell lines and table the results

* normalize for read depth, and varying enrichmenta cross ChIP samples

* quantile normalization applied to maximum signals

* use Shannon entropy scoring on normalized maximum signals to quanity the cell type-secificity for each region

# II. RNA-seq Prestige Processing Plan Steps

* align reads to reference genome (hg18 with TopHat for Prestige), allowing for a maximum of 10 multiple alignments

* determine the FPKM gene expression score using Cufflinks, with an FPKM threshold of 0.3 to balance the false discovery and false negative rates

* round gene expression to zero with FPKM below 0.3

* table the results

* "The data obtained for Neural Precursor Cells (NPCs) was sequenced on the ABI SOLiD platform, and was aligned using
TopHat modified for colorspace reads." (Note: need to research more about NPCs -- this is the question mark in the sheet document)

* use quantile normalization for the FPKMs across the different cell lines

* use Shannon entropy scoring on the normalized FPKMs to score cell line specificity of gene expression


# III. Quality Control

FASTQC is a standard method for assessing the quality of reads:

https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

Another quality control tool is Prinseq:

http://prinseq.sourceforge.net/manual.html




# IV. Filtering

We want to clean the reads, and filter the low-quality ones, and then map them (align to the reference human genome) before we use MACS2 to extract the peaks. 

There are different ways to filter low-quality reads, such as by FPKM, which is what Prestige uses. In our methods covered previously we also used TPM, and RPKM.

Further, a recently published paper proposed an additional improvement over FPKM:

<i>"Our results revealed that hierarchical clustering on normalized count data tended to group replicate samples from the same PDX model together more accurately than TPM and FPKM data. Furthermore, normalized count data were observed to have the lowest median coefficient of variation (CV), and highest intraclass correlation (ICC) values across all replicate samples from the same model and for the same gene across all PDX models compared to TPM and FPKM data... Our findings are consistent with what others have shown for human tumors and cell lines and add further support to the thesis that normalized counts are the best choice for the analysis of RNA-seq data across samples."</i>

https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-021-02936-w

I am not certain whether the above method is just a slight improvement and not worth the effort.


