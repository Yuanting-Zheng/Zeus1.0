import xlsxwriter
from use_def import handle_text
from use_class import *
from codon_table import *
from codon import *
#from enc import *
from rscu import RSCU
#from basic_index import BASIC_INDEX
import sys
file = sys.argv[1]  #
f = open(file,"r")

#f = open("cds","r")  #
#file = "cds"
gene_text = f.read()
gene_objs = handle_text(gene_text) # 
codon_table_obj = CODON_TABLE()
codon_table_name = "Standard_codons_table"

ssu = ['CCT','CGT','GCT','GGT']
wwu = ['AAC','ATC','TAC','TTC']
ssc = ['CCC','CGC','GCC','GGC']
wwc = ['AAT','ATT','TAT','TTT']

huge_sequence = ''
for gene_obj in gene_objs:
    huge_sequence+=gene_obj.sequence
huge_gene = GENE(huge_sequence,'huge gene')
huge_gene.rscu_obj = RSCU(huge_gene,codon_table_obj,codon_table_name)
huge_gene.rscu_obj.compute()
SSU = 0
WWU = 0
SSC = 0
WWC = 0
for codon in ssu:
    SSU+=huge_gene.rscu_obj.rscu_dict[codon]
for codon in wwu:
    WWU+=huge_gene.rscu_obj.rscu_dict[codon]
for codon in ssc:
    SSC+=huge_gene.rscu_obj.rscu_dict[codon]
for codon in wwc:
    WWC+=huge_gene.rscu_obj.rscu_dict[codon]
p2 = (WWC+SSU)/(WWC+WWU+SSC+SSU)

print(p2)



f.close()
