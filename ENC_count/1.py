import xlsxwriter
from use_def import handle_text
from use_class import *
from codon_table import *
from enc import *
#from rscu import RSCU
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

row = 0
work_book = xlsxwriter.Workbook(file+"_ENC.xlsx")
work_sheet = work_book.add_worksheet("enc")
work_sheet.write_row(row,0,['title','enc'])

for gene_obj in gene_objs:
    if gene_obj.enc_obj is None:
        gene_obj.enc_obj = ENC(gene_obj, codon_table_obj, codon_table_name)
        gene_obj.enc_obj.compute()
    row += 1
    work_sheet.write_row(row, 0, [gene_obj.name, gene_obj.enc_obj.enc])



work_book.close()
f.close()
