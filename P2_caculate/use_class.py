class GENE:
    __slots__ = (
    'sequence', 'name', 'codon_obj', 'codon_num', 'basic_index_obj', 'rscu_obj', 'enc_obj', 'codon_pair_obj', 'cpb')

    init_codon = ['ATG']
    termination_codon = ['TAA', 'TGA', 'TAG']

    def __init__(self, sequence, name):
        '''
        sequence:基因序列
        name:基因名称
        '''
        self.cpb = 0
        self.sequence = sequence
        self.name = name
        self.codon_num = len(sequence) / 3
        self.codon_obj = None
        self.enc_obj = None
        self.basic_index_obj = None
        self.rscu_obj = None
        self.codon_pair_obj = None

    def handle_gene(self, sequence=None):
        '''
        删除基因的起始和终止密码子
        '''
        return self.delete_termination(self.delete_init(sequence))

    def delete_init(self, sequence=None):
        '''
        删除起始密码子
        '''
        if sequence is None:
            if self.sequence[:3] == self.init_codon:
                return self.sequence[3:]
            else:
                return self.sequence
        elif sequence[:3] == self.init_codon:
            return sequence[3:]
        return sequence

    def delete_termination(self, sequence=None):
        '''
        删除终止密码子
        '''
        if sequence is None:
            if self.sequence[-3:] in self.termination_codon:
                return self.sequence[0:-3]
            else:
                return self.sequence[0:-3]
        elif sequence[-3:] in self.termination_codon:
            return sequence[0:-3]
        return sequence[0:-3]

    def delete_codons(self):
        # self.sequence = self.delete_init()
        # self.sequence = self.delete_termination()
        # d_codons=['ATG','TGG']
        temp_list = list(self.sequence)
        for i in range(0, len(temp_list), 3):
            if temp_list[i + 2] == 'G':
                if temp_list[i] == 'A' and temp_list[i + 1] == 'T':
                    temp_list[i] = ''
                    temp_list[i + 1] = ''
                    temp_list[i + 2] = ''
                elif temp_list[i] == 'T' and temp_list[i + 1] == 'G':
                    temp_list[i] = ''
                    temp_list[i + 1] = ''
                    temp_list[i + 2] = ''
        self.sequence = ''.join(temp_list)