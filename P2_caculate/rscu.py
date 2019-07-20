from codon import CODON

class RSCU:
    '''
    计算RSCU值
    '''
    __slots__ = ('gene_obj', 'codon_table', 'rscu_dict', 'percent_dict')

    def __init__(self, gene_obj, codon_table_obj, codon_table_name):
        self.gene_obj = gene_obj
        self.codon_table = codon_table_obj.get_codon_table(codon_table_name)
        codons = codon_table_obj.get_codons()
        if self.gene_obj.codon_obj is None:
            self.gene_obj.codon_obj = CODON(self.gene_obj, codons)
            self.gene_obj.codon_obj.compute()
        self.rscu_dict = {}
        self.percent_dict = {}
        for codon in codons:
            self.rscu_dict[codon] = 0
            self.percent_dict[codon] = 0

    def compute(self):
        '''
        计算所有的密码子的RSCU值
        '''
        for k in self.codon_table.keys():
            self.compute_rscu_by_aa(k)

    def compute_rscu_by_aa(self, aa_name):
        '''
        通过氨基酸计算部分密码子rscu值
        '''
        codons = self.codon_table[aa_name]

        sum1 = 0
        for codon in codons:
            sum1 += self.gene_obj.codon_obj.codon_frequency_dict[codon]

        if sum1 == 0:
            for codon in codons:
                self.percent_dict[codon] = 0
                self.rscu_dict[codon] = 0
            return

        sum2 = sum1 / len(codons)

        for codon in codons:
            self.percent_dict[codon] = self.gene_obj.codon_obj.codon_frequency_dict[codon] / sum1
            self.rscu_dict[codon] = self.gene_obj.codon_obj.codon_frequency_dict[codon] / sum2

    def row_format(self):
        '''
        返回二维数据
        每一行对应一个密码子的统计结果
        '''
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