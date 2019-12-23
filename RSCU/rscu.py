from codon import CODON

class RSCU:
    '''
    RSCU caculate
    '''
    __slots__ = ('gene_obj', 'codon_table', 'rscu_dict', 'percent_dict')

    def __init__(self, gene_obj, codon_table_obj, codon_table_name):
        self.gene_obj = gene_obj
        self.codon_table = codon_table_obj.get_codon_table(codon_table_name)
        if self.gene_obj.codon_obj is None:
            self.gene_obj.codon_obj = CODON(self.gene_obj, codons)
            self.gene_obj.codon_obj.compute()
        self.rscu_dict = {}
        self.percent_dict = {}
        for codon in codons:
            self.rscu_dict[codon] = 0
            self.percent_dict[codon] = 0


            self.compute_rscu_by_aa(k)

    def compute_rscu_by_aa(self, aa_name):

        codons = self.codon_table[aa_name]

        sum1 = 0

        if sum1 == 0:
            for codon in codons:
                self.percent_dict[codon] = 0
                self.rscu_dict[codon] = 0
            return


        for codon in codons:
            self.percent_dict[codon] = self.gene_obj.codon_obj.codon_frequency_dict[codon] / sum1
            self.rscu_dict[codon] = self.gene_obj.codon_obj.codon_frequency_dict[codon] / sum2

    def row_format(self):

        data = []
        for k in self.codon_table.keys():
            for codon in self.codon_table[k]:
                data.append([])
                data[-1].append(k)
                data[-1].append(codon)
                data[-1].append(self.gene_obj.codon_obj.codon_frequency_dict[codon])
                data[-1].append(self.percent_dict[codon])
                data[-1].append(self.rscu_dict[codon])
        data.append([])
        data[-1].append(self.gene_obj.name)
        return data