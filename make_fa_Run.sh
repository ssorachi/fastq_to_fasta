#! /bin/sh
#$ -S /bin/sh
#$ -cwd


export PATH=#Input your conda pass:${PATH}
#Culutivar
Culutivar=xxx
#fastq.gz pass ex)xxx/xxx/example1_fastq.gz \n yyy/yyy/example2_fastq.gz
fastq_gz_txt=xxx.txt
#used cpu
used_cpu=x
#full pass of fastq_to_fasta.py 
fq_to_fa_py=xxx/xxx/xxx/xxx/fastq_to_fasta.py
#------------------------------------------------------------------------------------------------
echo "make pre_txt"
python pre_output_txt.py ${fastq_gz_txt}

echo "make txt"
python output_txt.py ${fastq_gz_txt} ${fq_to_fa_py}

echo "make fastq"
cat fqgz_to_fq.txt|xargs -P${used_cpu} -I % sh -c %

echo "make fasta"
cat fq_to_fa.txt|xargs -P${used_cpu} -I % sh -c %

echo "make fasta.gz"
cat fa_to_fagz.txt|xargs -P${used_cpu} -I % sh -c %

echo "remake fastq.gz"
cat fq_to_fqgz.txt|xargs -P${used_cpu} -I % sh -c %

mkdir ${Culutivar}_fasta_gz_pass
mv *.fasta.gz ${Culutivar}_fasta_gz_pass

mkdir ${Culutivar}_fastq_gz_pass
mv *.fastq.gz ${Culutivar}_fastq_gz_pass
