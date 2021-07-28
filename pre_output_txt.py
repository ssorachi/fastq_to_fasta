#!/usr/bin/env python
# coding: UTF-8
# In[11]:

import sys
import re

args = sys.argv
fastq_gz_txt = args[1]
#----------------------------------------------------------------------------------------------------------------------------------------

a = open(fastq_gz_txt,'r')

w = open('fastq.txt',mode='w')
v = open('fasta.txt',mode='w')


#make pre_txt
while True:
    line_1 = a.readline()
    if line_1:
        pre_fastq = re.sub('\S+/',"",line_1)
        fastq = pre_fastq.replace('.gz','')
        fasta = pre_fastq.replace('q.gz','a')
        w.write(fastq)
        v.write(fasta)
    else:
        break

a.close()
