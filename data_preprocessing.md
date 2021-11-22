# ChIP-seq Processing Plan Steps

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

# RNA-seq Processing Plan Steps

* align reads to reference genome (hg18 with TopHat for Prestige), allowing for a maximum of 10 multiple alignments

* determine the FPKM gene expression score using Cufflinks, with an FPKM threshold of 0.3 to balance the false discovery and false negative rates

* round gene expression to zero with FPKM below 0.3

* table the results

* "The data obtained for Neural Precursor Cells (NPCs) was sequenced on the ABI SOLiD platform, and was aligned using
TopHat modified for colorspace reads." (Note: need to research more about NPCs -- this is the question mark in the sheet document)

* use quantile normalization for the FPKMs across the different cell lines

* use Shannon entropy scoring on the normalized FPKMs to score cell line specificity of gene expression

