Standard_codons_table = {
    'A':['GCT','GCC','GCA','GCG'],
    'L':['TTA','TTG','CTT','CTC','CTA','CTG'],
    'R':['CGT','CGC','CGA','CGG','AGA','AGG'],
    'K':['AAA','AAG'],
    'N':['AAT','AAC'],
    'M':['ATG'],
    'D':['GAT','GAC'],
    'F':['TTT','TTC'],
    'C':['TGT','TGC'],
    'P':['CCT','CCC','CCA','CCG'],
    'Q':['CAA','CAG'],
    'S':['TCT','TCC','TCA','TCG','AGT','AGC'],
    'E':['GAA','GAG'],
    'T':['ACT','ACC','ACA','ACG'],
    'G':['GGT','GGC','GGA','GGG'],
    'W':['TGG'],
    'H':['CAT','CAC'],
    'Y':['TAT','TAC'],
    'I':['ATT','ATC','ATA'],
    'V':['GTT','GTC','GTA','GTG'],
    '*':['TAG','TGA','TAA']
}

class CODON_TABLE:
    __slots__ = ('codon_table')

    def __init__(self):
        self.codon_table = {}
        self.codon_table['Standard_codons_table'] = Standard_codons_table

    def get_codon_table(self, name):
        return self.codon_table[name]

    def get_codons(self):
        return ['GCT', 'GCC', 'GCA', 'GCG', 'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG', 'CGT', 'CGC', 'CGA', 'CGG', 'AGA',
                'AGG', 'AAA', 'AAG', 'AAT', 'AAC', 'GAT', 'GAC', 'TTT', 'TTC', 'TGT', 'TGC', 'CCT', 'CCC', 'CCA', 'CCG',
                'CAA', 'CAG', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC', 'GAA', 'GAG', 'ACT', 'ACC', 'ACA', 'ACG', 'GGT',
                'GGC', 'GGA', 'GGG', 'TGG', 'CAT', 'CAC', 'TAT', 'TAC', 'ATT', 'ATC', 'ATA', 'GTT', 'GTC', 'GTA', 'GTG',
                'ATG', 'TAG', 'TGA', 'TAA']
