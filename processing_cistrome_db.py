import pandas as pd


histone_data = pd.read_csv('histones.txt', delimiter = '\t')


'''
        DCid       Species       GSMID    Factor Cell_line  ... UniquelyMappedRatio    PBC  PeaksFoldChangeAbove10      FRiP  PeaksUnionDHSRatio
0        268  Homo sapiens   GSM648494   H3K4me1    aTconv  ...              0.1307  0.971                  1907.0  0.229959              0.6944
1        269  Homo sapiens   GSM648495   H3K4me3    aTconv  ...              0.1340  0.932                  7935.0  0.669119              0.9740
2        272  Homo sapiens   GSM575295  H3K27me3      BG01  ...              0.1048  0.629                  1173.0  0.175297              0.3536
3        273  Homo sapiens   GSM575280   H3K4me3      BG01  ...              0.3263  0.925                  8562.0  0.420731              0.9750
4        274  Homo sapiens   GSM575296  H3K27me3      BG03  ...              0.3280  0.594                    15.0  0.008848              0.9000
'''


h3k27ac = histone_data.loc[histone_data['Factor'] == 'H3K27ac'] # 11,000 entries for H3K27ac


# don't run this if trying to get total value counts csv output
# h3k27ac = histone_data.loc[histone_data['Factor'] == 'H3K27ac'].drop_duplicates(subset = 'Cell_line') # 422 unique cell line entries for H3K27ac



'''
        DCid       Species       GSMID   Factor     Cell_line            Cell_type Tissue_type  FastQC  UniquelyMappedRatio    PBC  PeaksFoldChangeAbove10      FRiP  PeaksUnionDHSRatio
36       864  Homo sapiens   GSM663427  H3K27ac            H1  Embryonic Stem Cell      Embryo    33.0               0.6127  0.986                  2239.0  0.096068            0.934200
101     1025  Homo sapiens   GSM665037  H3K27ac            H9  Embryonic Stem Cell      Embryo    28.0               0.5413  0.985                   244.0  0.007502            0.888553
244     1820  Homo sapiens   GSM521887  H3K27ac         IMR90           Fibroblast        Lung    31.0               0.6975  0.973                 13388.0  0.486290            0.976600
291     1891  Homo sapiens   GSM706065  H3K27ac  iPS DF 19.11                 iPSC    Foreskin    37.0               0.5140  0.955                   414.0  0.013612            0.929400
331     2199  Homo sapiens   GSM686938  H3K27ac         LNCaP           Epithelium    Prostate    30.0               0.7837  0.986                  7163.0  0.273093            0.955800
...      ...           ...         ...      ...           ...                  ...         ...     ...                  ...    ...                     ...       ...                 ...
10835  87696  Homo sapiens  GSM2871002  H3K27ac        SJNB-3                SJNB3        None    32.0               0.8666  0.975                  5594.0  0.495756            0.975600
10841  87812  Homo sapiens  GSM2359490  H3K27ac           N87                 None     Stomach    38.0               0.8176  0.988                    12.0  0.049162            0.903800
10940  88459  Homo sapiens  GSM2523136  H3K27ac          HNE1                 None        None    40.0               0.9053  0.976                  1102.0  0.217087            0.972800
10963  88603  Homo sapiens  GSM2301915  H3K27ac          IMEC           Epithelium      Breast    39.0               0.9199  0.973                    58.0  0.084248            0.943000
11016  88808  Homo sapiens  GSM2523126  H3K27ac         C6661                 None        None    39.0               0.9033  0.883                    42.0  0.068909            0.954000
'''




by_frequency = h3k27ac['Cell_line'].value_counts()

print(by_frequency.to_string())


'''
None                1164
MCF-7                 68
K562                  57
A549                  53
HCT-116               53
GM12878               34
MCF-10A               31
LNCaP                 27
H1                    19
IMR90                 19
HT29                  18
Pfeiffer              17
HUES64                16
HeLa                  15
CyT49                 14
D-341                 12
BICR31                11
H9                    11
MRC5                  11
MDA-MB-231            11
JHU-06                10
Toledo                10
NHEK                  10
SUM159PT              10
Jurkat                 9
MD-901                 9
786-O                  9
LCL                    9
Raji                   9
HepG2                  8
Ishikawa               8
A673                   7
WIBR3                  7
CFPAC-1                7
CHL-1                  7
hMADS-3                6
SHEP-21N               6
VCaP                   6
PANC-1                 6
HCC95                  5
L3.6                   5
SK-N-MC                5
SW480                  5
H1299                  5
D283 Med               5
MOLM-14                5
MV4-11                 5
ZR-75-1                5
ZR-75-30               5
T47D                   5
PC-9                   5
KATO III               5
H2009                  5
MS1                    5
GM19239                5
A375                   5
CUTLL1                 5
P493-6                 5
HCC1954                5
BE2-C                  5
THP-1                  5
'''



by_frequency.to_csv('cistrome_db_h3k27ac_histone_by_cell_line_frequency_counts.csv') # , index=False, header=True)




