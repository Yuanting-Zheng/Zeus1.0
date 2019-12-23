#开始模块
import os
os.system("cp ../1_input/original.fasta input/gene.fasta")
os.system('python3.5 algorithm.py')
f = open("../2_single/original_translated.fasta","r")
lines = f.readlines()
name = lines[0].split("_",3)[1]

f1 = open("output/optimized_gene.fasta",'r')
lines1 = f1.readlines()

f2 = open("../6_output/pair.fasta",'w')
f2.write(">"+name+"_pair"+"\n")
seq = ""
for line in lines1[1:]:
    seq = seq+line

f2.write(seq+"\n")
f.close()
f1.close()
f2.close()
