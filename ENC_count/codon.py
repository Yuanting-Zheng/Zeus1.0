class CODON:
    __slots__ = ('codon_frequency_dict', 'gene_obj')

    def __init__(self, gene_obj, codons):
        self.codon_frequency_dict = {}
        self.gene_obj = gene_obj
        for codon in codons:
            self.codon_frequency_dict[codon] = 0

    def compute(self):
        for i in range(0, len(self.gene_obj.sequence), 3):
            temp = self.gene_obj.sequence[i:i + 3]
            self.codon_frequency_dict[temp] += 1

    def add(self, other_obj):
        for key in self.codon_frequency_dict.keys():
            self.codon_frequency_dict[key] += other_obj.codon_frequency_dict[key]
