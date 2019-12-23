#保存文件模块
from def_four.R import *
f = open('file_storage/single_model','r')
a = f.read()
single_dict = eval(a)
f.close()

f = open('file_storage/double_model','r')
b = f.read()
double_dict = eval(b)
f.close()


r_view_single(single_dict)
r_view_double(double_dict)

print("files are saved in R folders")



