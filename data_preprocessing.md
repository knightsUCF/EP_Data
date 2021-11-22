
# Notes on Filtering

We want to clean the reads, and filter the low-quality ones, and then map them (align to the reference human genome) before we use MACS2 to extract the peaks. 

There are different ways to filter low-quality ones, such as by FPKM, which is what Prestige uses. In our methods covered previously we also used TPM, and RPKM.

Further, a recently published paper proposed an additional improvement over FPKM:

<i>"Our results revealed that hierarchical clustering on normalized count data tended to group replicate samples from the same PDX model together more accurately than TPM and FPKM data. Furthermore, normalized count data were observed to have the lowest median coefficient of variation (CV), and highest intraclass correlation (ICC) values across all replicate samples from the same model and for the same gene across all PDX models compared to TPM and FPKM data."</i>

https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-021-02936-w


* obtain the ChIP-seq peaks and RNA-seq gene expression for each of the 21 samples based on the methods we learned some time ago

* we do not consider the 13th row, as the sample is not from the same condition

* For ChIP-seq, we hope to have both peaks defined by MACS2 and the bigwig files.

* For both data, you need to see how people first clean reads, filter low-quality one and then map before you apply macs2 or the R tool to define gene expression. 

* Please refer to prestidge and let me know your plan of do it first.




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

