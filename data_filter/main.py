import sys
from def_filter import filter
file = sys.argv[1]  #

k = sys.argv[2] #

f = open(file,'r')  #
lines = f.readlines()  #
n = len(lines)
dict = {}             #

for i in range(0,n,2):           #
    key = lines[i].strip()        #
    value = lines[i+1].strip()
    dict[key] = value

f2 = open("raw_dict",'w')  #
f2.write(str(dict))
f2.close()
f.close()

filter_result = file+"_remain"
filter_out = file+"_out"

f3 = open(filter_result, "w")
f4 = open(filter_out, "w")

total_num = 0
remain_num = 0

for key, value in dict.items():
    ok = filter(value,k)
    total_num+=1

    if ok == 1:
        f4.write("长度不是3的倍数"+key+"\n")
        f4.write(value+"\n")
    if ok == 2:
        f4.write("不是起始密码子开头"+key+"\n")
        f4.write(value+"\n")
    if ok == 3:
        f4.write("不是终止密码子结尾"+key+"\n")
        f4.write(value+"\n")
    if ok == 4:
        f4.write("长度不符合我们的规定"+key+"\n")
        f4.write(value+"\n")
    if ok == 5:
        f4.write("含有非ATCG的字母"+key+"\n")
        f4.write(value+"\n")
    if ok == 6:
        remain_num+=1
        f3.write(key+"\n")
        f3.write(value+"\n")


print("Total: " + str(total_num))
print("remain: " + str(remain_num))
f3.close()
f4.close()







