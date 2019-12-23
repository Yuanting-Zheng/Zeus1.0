#密码子偏好分析可视化模块
from def_three.view_def import *
f = open('file_storage/single_model','r')
a = f.read()
single_dict = eval(a)
f.close()

f = open('file_storage/double_model','r')
b = f.read()
double_dict = eval(b)
f.close()


view_single(single_dict)

#(double_dict)

view_double(double_dict)










