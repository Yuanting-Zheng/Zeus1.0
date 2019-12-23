import os
os.system("cat ../6_output/original.fasta ../6_output/single.fasta ../6_output/pair.fasta > ../6_output/three_cds.fasta")
os.system("cat ../6_output/original_translated.fasta ../6_output/single_translated.fasta ../6_output/pair_translated.fasta > ../6_output/three_pep.fasta")
os.system("python3 checkmap.py ../6_output/three_cds.fasta > ../6_output/cds_map")
os.system("python3 checkmap.py ../6_output/three_pep.fasta > ../6_output/pep_map")

