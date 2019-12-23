import sys
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
def make_protein_record(nuc_record):
    """Returns a new SeqRecord with the translated sequence (default table)."""
    return SeqRecord(seq = nuc_record.seq.translate(cds=True), \
                     id = "trans_" + nuc_record.id, \
                     description = "translation of CDS, using default table")

filename = sys.argv[1]
filename2 = sys.argv[2]
print(filename)
print(filename2)
proteins = (make_protein_record(nuc_rec) for nuc_rec in \
            SeqIO.parse(filename, "fasta"))
SeqIO.write(proteins, filename2, "fasta")