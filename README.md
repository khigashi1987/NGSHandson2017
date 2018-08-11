# NGSHandson2017 Hi-C解析
事前準備  


## 元論文
http://www.sciencedirect.com/science/article/pii/S0092867414014974  
A 3D Map of the Human Genome at Kilobase Resolution Reveals Principles of Chromatin Looping  
Rao et al, 2014  


##データダウンロード
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE63525  
から  
サンプルHIC020 （GSM1551569）: SRR1658592  
サンプルHIC022 （GSM1551571）: SRR1658594, SRR1658595  
をダウンロード  


## SRA to FASTQ
SRA Toolkit のダウンロード  
https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software  
fastq-dump --origfmt --gzip --split-files --accession SRR1658592  
などでダウンロード、R1R2に分解。  


## Reference Genome
ヒトゲノムリファレンス配列hg19の各染色体配列をダウンロード。  
http://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/chr*.fa.gz  
chr1-22, chrX, chrY, chrM  
ギャップ情報も  
wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/database/gap.txt.gz  
でダウンロードしておく。  


## bowtie2ダウンロードとインストール
ソースコードは、http://bowtie-bio.sourceforge.net/bowtie2/index.shtml からダウンロード。  


## samtoolsのダウンロードとインストール
ソースコードは http://samtools.sourceforge.net 中段のダウンロードページから。  
configureしてmake  


## hdf5-toolsのダウンロードとインストール
macの場合はbrew install hdf5でもOK.  
Ubuntuの場合はsudo apt-get install libhdf5-serial-dev も必要。  


## pythonライブラリのダウンロードとインストール
condaやpipで以下をインストール  
cython  
biopython  
joblib  
pysam  
bx-python  
numpyは必要に応じて適宜、環境を区切って特定のバージョンを入れることが必要かも  


## mirnylibのダウンロードとセッティング
https://bitbucket.org/mirnylab/mirnylib/get/tip.zip  
python install_linux.py  
fopenmpなどがない場合は適宜インストール。  
PYTHONPATHを通しておく。  


## hiclibのダウンロードとセッティング
https://bitbucket.org/mirnylab/hiclib/get/85979ac69b55.zip  
からダウンロード。  
ドキュメントは https://mirnylab.bitbucket.io/hiclib/  
python install_linux.py  
PYTHONPATHを通しておく。  


## bowtie2-build
bowtie2-build ./chr*.fa hg19  
環境によってはヒトゲノムで２時間弱かかる。  


## Juiceboxのダウンロード元
https://data.mendeley.com/datasets/dj4nrsc552/1 
