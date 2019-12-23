import xlsxwriter
from use_def import handle_text
from use_class import *
from codon_table import *
from rscu import RSCU

import sys
file = sys.argv[1]
f = open(file,"r")

gene_text = f.read()
gene_objs = handle_text(gene_text)

row = 0
work_book = xlsxwriter.Workbook(file+"_rscu.xlsx")
work_sheet = work_book.add_worksheet("rscu")
work_sheet.write_row(row,0,['AA','codon','个数','比例','rscu'])

codon_table_obj = CODON_TABLE()

for gene_obj in gene_objs:
    if gene_obj.rscu_obj is None:
        gene_obj.rscu_obj = RSCU(gene_obj, codon_table_obj, "Standard_codons_table")
        gene_obj.rscu_obj.compute()
    for row_format in gene_obj.rscu_obj.row_format():
        row += 1
        work_sheet.write_row(row, 0, row_format)

work_book.close()

f.close()