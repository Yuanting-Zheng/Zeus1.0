#密码子偏好分析模块
from def_three.codon_def import *
from def_three.percent_def import *

f = open('file_storage/dict_filter','r')
a = f.read()
dict_data = eval(a)
f.close()


caculate_percent = {}
#single
pep_cds_dict = {}
single_codon(dict_data,pep_cds_dict)
percent(pep_cds_dict)


#make a caculate_percent for later caculate
f = open('file_storage/pep_cds_dict','r')
b = f.read()
dict_data_model = eval(b)
f.close()
make_single_model(dict_data_model)



#double
pep_cds_dict_two = {}
double_codon(dict_data,pep_cds_dict_two)
percent_two(pep_cds_dict_two)


#make a caculate_percent_two for later caculate
f = open('file_storage/pep_cds_dict_two','r')
c = f.read()
dict_data_model_two = eval(c)
f.close()
make_double_model(dict_data_model_two)











