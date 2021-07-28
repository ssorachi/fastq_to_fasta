#!/usr/bin/env python
# coding: UTF-8
# In[11]:


import sys
import re

args = sys.argv
fastq_gz_txt = args[1]
fq_to_fa_py = args[2]
#----------------------------------------------------------------------------------------------------------------------------------------
a = open(fastq_gz_txt,'r')
b = open('fastq.txt','r')
c = open('fasta.txt','r')

z = open('fqgz_to_fq.txt',mode='w')
y = open('fq_to_fa.txt',mode='w')
x = open('fa_to_fagz.txt',mode='w')
w = open('fq_to_fqgz.txt',mode='w')


#make txt
while True:
    line_2 = a.readline()
    line_3 = b.readline()
    line_4 = c.readline()
    if line_2 or line_3 or line_4:
        final_line_3 = line_3.replace('\n','')
        final_line_4 = line_4.replace('\n','')
        z.write('gunzip '+line_2)
        y.write('python '+fq_to_fa_py+' '+final_line_3+' '+final_line_4+'\n')
        x.write('gzip '+final_line_4+'\n')
        w.write('gzip '+final_line_3+'\n')
    else:
        break

a.close()
b.close()
c.close()
