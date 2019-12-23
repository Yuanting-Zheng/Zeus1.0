# 1cds 转成pep
# 2pep 转成CDS
import os
from sbias import standard_codon_table
os.system("python3 ../4_translate/cds-protein.py ../1_input/original.fasta original_translated.fasta")
f = open("original_translated.fasta","r")
lines = f.readlines()
AA = ""
for line in lines[1:]:
    line = line.strip()
    AA = AA+line

AA = AA+"*"
seq = ''
for unit in AA:
    seq = seq+standard_codon_table[unit]

name = lines[0].split("_",3)[1]

f2 = open("single_result",'w')
f2.write(">"+name+"_single"+"\n")
f2.write(seq+"\n")
f.close()
f2.close()
os.system("cp ../1_input/original.fasta ../6_output/")
os.system("cp ../2_single/single_result ../6_output/single.fasta")




