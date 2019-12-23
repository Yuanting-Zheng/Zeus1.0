#长度检测模块
from def_two.pep_lenth_def import pep_len

f = open('file_storage/dict_filter','r')
a = f.read()
dict_data = eval(a)
f.close()

pep_len(dict_data)