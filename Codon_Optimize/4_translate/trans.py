import os
os.system("python3 cds-protein.py ../6_output/original.fasta ../6_output/original_translated.fasta")
os.system("python3 cds-protein.py ../6_output/single.fasta ../6_output/single_translated.fasta")
os.system("python3 cds-protein.py ../6_output/pair.fasta ../6_output/pair_translated.fasta")
