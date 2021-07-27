#!/usr/bin/env python
# coding: utf-8


# In[11]:
import sys
import re
args = sys.argv
read_file = args[1]
output_name = args[2]
#----------------------------------------------------------------------------------------------------------------------------------------
read_file = read_file
output_name = output_name
#----------------------------------------------------------------------------------------------------------------------------------------
f = open(read_file, 'r')
t = open(output_name,mode='a')
count = 0
while True:
    line = f.readline()
    if line:
        amari = count % 4
        if amari < 2:
            if amari == 0:
                new = line.replace('@', '>')
                t.write(new)
            else:
                t.write(line)
        else:
            pass
        count += 1
    else:
        break

f.close()

# In[ ]:
