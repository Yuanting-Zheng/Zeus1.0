from use_def import handle_text
from use_class import GENE

import sys
file = sys.argv[1]

f = open(file,"r")
gene_text = f.read()

gene_objs = handle_text(gene_text)

f1 = open(file+"delete_5_result",'w')

for obj in gene_objs:
    ID = obj.name
    seq = obj.sequence
    f1.write(ID+"\n"+seq+'\n')

f.close()
f1.close()