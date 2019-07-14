import math
from codon import CODON
class ENC:

    __slots__ = ('gene_obj','enc','codon_table','F')

    def __init__(self,gene_obj,codon_table_obj,codon_table_name):
        self.gene_obj = gene_obj
        self.codon_table = codon_table_obj.get_codon_table(codon_table_name)
        codons = codon_table_obj.get_codons()
        if self.gene_obj.codon_obj is None:
            self.gene_obj.codon_obj = CODON(self.gene_obj,codons)
            self.gene_obj.codon_obj.compute()
        # if not has_init:
        #     self.sequence = gene_obj.delete_init(self.sequence)
        # if not has_termination:
        #     self.sequence = gene_obj.delete_termination(self.sequence)
        self.F = {}
        self.F['F2'] = []
        self.F['F3'] = []
        self.F['F4'] = []
        self.F['F6'] = []

    def compute(self):
        '''
        计算ENC
        '''
        # n = len(self.gene_obj.sequence)/3
        self.enc = 2
        for aa in self.codon_table.keys():
            k = len(self.codon_table[aa])
            f=self.computeF(aa)
            if k ==2 :
                self.F['F2'].append(f)
            elif k == 3:
                self.F['F3'].append(f)
            elif k == 4:
                self.F['F4'].append(f)
            elif k == 6:
                self.F['F6'].append(f)
        
        ave2 = self.clear_zero('F2')
        #self.clear_zero('F3')
        ave4 = self.clear_zero('F4')
        self.clear_zero('F6')

        if self.F['F3'][0] == 0:
            self.F['F3'][0] = (ave2*2+ave4*4)/6

        self.enc += self.do_sum('F2')
        self.enc += self.do_sum('F3')
        self.enc += self.do_sum('F4')
        self.enc += self.do_sum('F6')
        if self.enc>61:
            self.enc=61
        
    def computeF(self,aa_name):
        '''
        计算F
        n:基因密码子个数
        k:同义密码子数量
        '''
        n=0
        f=0
        for codon in self.codon_table[aa_name]:
            n+=self.gene_obj.codon_obj.codon_frequency_dict[codon]
        if n <= 1:
            return f
        for codon in self.codon_table[aa_name]:
            f+=math.pow(self.gene_obj.codon_obj.codon_frequency_dict[codon],2)
        f = (f/n-1)/(n-1)
        return f

    def clear_zero(self,f_name):
        '''
        清除F=0的氨基酸，令其F值为平均值
        '''
        total_sum = 0
        non_zero_num = 0
        for item in self.F[f_name]:
            total_sum+=item
            if item != 0:
                non_zero_num+=1

            # 0409

        if non_zero_num == 0:
            non_zero_num = 1
        average = total_sum/non_zero_num
        if non_zero_num != len(self.F[f_name]):
            for i in range(len(self.F[f_name])):
                if self.F[f_name][i] == 0:
                    self.F[f_name][i] = average
        return average
    
    def do_sum(self,f_name):
        temp = 0
        for item in self.F[f_name]:
            if item == 0:#f3=0
                continue
            temp += 1/item
        return temp

    def row_format(self):
        pass