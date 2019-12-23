def pep_len(dict_data):
    f = open('show_result/lenth','w')
    f1 = open('show_result/name','w')
    i = 0
    lenth = []
    name_lenth = []
    for key, value in dict_data.items():
        for unit in value:
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                i = i + 1
                lenth.append(len(V[1]))
                name_lenth.append(K)




    print('total have ：'+str(i)+'peps')
    #f.write('总共计算了：'+str(i)+'条'+'\n')
    print(str(lenth))
    f.write(str(lenth))
    print(len(lenth))
    f1.write(str(name_lenth))
    print(str(name_lenth))


    f.close()
    f1.close()









