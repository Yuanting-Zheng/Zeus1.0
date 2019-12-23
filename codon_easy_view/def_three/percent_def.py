def percent_list_model(list):
    cont = {} # 定义一个字典 密码子对应个数的字典
    for unit in list:

        if unit in cont:
            cont[unit] += 1
        else:
            cont[unit] = 1

    n = len(list) #计算总的个数

    for key, value in cont.items():
        num_percent = value/n
        cont[key] = [num_percent, value]
    return cont
def make_single_model(dict):
    f7 = open('file_storage/single_model', 'w')
    caculate_percent ={}
    for key, value in sorted(dict.items(),key=lambda item:item[0]):
        print(key + ":" + str(percent_list_model(value))) # 这里处理字典的元素的值，丢到一个函数中去，函数见上
        caculate_percent[key] = percent_list_model(value)
    f7.write(str(caculate_percent))
    f7.close()


def percent_list_model_two(list,key):
    f8 = open('file_storage/single_model', 'r')
    a = f8.read()
    caculate_percent = eval(a)
    f8.close()

    key1 = key[0]
    key2 = key[1]
    cont = {} # 定义一个字典 密码子对应个数的字典
    for unit in list:

        if unit in cont:
            cont[unit] += 1
        else:
            cont[unit] = 1

    n = len(list) #计算总的个数

    for key, value in cont.items():
        percent = format(value/n, '.4')
        keys = key.split(" ")
        pos_one = keys[0]
        pos_two = keys[1]

        nature_percent_num = caculate_percent[key1][pos_one][0] * caculate_percent[key2][pos_two][0]
        nature_percent = format(nature_percent_num, '.4')
        if  value/n > nature_percent_num:
            up = "up"
            cont[key] = value, percent, up, nature_percent

        if  value/n == nature_percent_num:
            down = "null"
            cont[key] = value, percent, down, nature_percent

        if  value/n < nature_percent_num:
            down = "down"
            cont[key] = [value, percent, down, nature_percent]

    return cont


def make_double_model(dict):
    f8 = open('file_storage/double_model', 'w')
    caculate_percent_two = {}
    for key, value in sorted(dict.items(),key=lambda item:item[0]):
        print(key + ":" + str(percent_list_two(value,key))) # 这里处理字典的元素的值，丢到一个函数中去，函数见上
        caculate_percent_two[key] = percent_list_model_two(value,key)

    f8.write(str(caculate_percent_two))
    f8.close()













def percent_list(list):
    cont = {} # 定义一个字典 密码子对应个数的字典
    for unit in list:

        if unit in cont:
            cont[unit] += 1
        else:
            cont[unit] = 1

    n = len(list) #计算总的个数

    for key, value in cont.items():
        percent = format(value/n, '.3%')
        cont[key] = [value, percent]


    return sorted(cont.items(),key=lambda item:item[1][0],reverse=True)

def percent(dict):
    f3 = open('file_storage/single_result', 'w')
    for key, value in sorted(dict.items(), key=lambda item: item[0]):
        print(key + ":" + str(percent_list(value)))  # 这里处理字典的元素的值，丢到一个函数中去，函数见上
        f3.write(key + str(percent_list(value)) + "\n")












def percent_list_two(list,key):
    f8 = open('file_storage/single_model', 'r')
    a = f8.read()
    caculate_percent = eval(a)
    f8.close()

    key1 = key[0]
    key2 = key[1]
    cont = {} # 定义一个字典 密码子对应个数的字典
    for unit in list:

        if unit in cont:
            cont[unit] += 1
        else:
            cont[unit] = 1

    n = len(list) #计算总的个数

    for key, value in cont.items():
        percent = format(value/n, '.4%')
        keys = key.split(" ")
        pos_one = keys[0]
        pos_two = keys[1]

        nature_percent_num = caculate_percent[key1][pos_one][0] * caculate_percent[key2][pos_two][0]
        nature_percent = format(nature_percent_num, '.4%')
        if  value/n > nature_percent_num:
            up = "up"
            cont[key] = value, percent, up, nature_percent

        if  value/n == nature_percent_num:
            down = "null"
            cont[key] = value, percent, down, nature_percent

        if  value/n < nature_percent_num:
            down = "down"
            cont[key] = [value, percent, down, nature_percent]

    return sorted(cont.items(),key=lambda item:item[1][0],reverse=True)


def percent_two(dict):
    f4 = open('file_storage/double_result', 'w')
    for key, value in sorted(dict.items(),key=lambda item:item[0]):
        #print(key + ":" + str(value))
        print(key + ":" + str(percent_list_two(value,key))) # 这里处理字典的元素的值，丢到一个函数中去，函数见上
        f4.write(key + ":" + str(percent_list_two(value,key)) + "\n")
    f4.close()






