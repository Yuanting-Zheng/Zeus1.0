
def caculate_cds_pep(cds,pep,pep_cds_dict):
    #f = open('file_storage/pep_cds_dict', 'w')

    lenth_pep = len(pep)
    pep = pep + "*"
    i = 0
    j = 0
    k = lenth_pep
    while i < k + 1:
        # print(pep[i])
        # print(cds[j:j+3])
        if pep[i] in pep_cds_dict:
            pep_cds_dict.get(pep[i]).append(cds[j:j + 3])
        else:
            pep_cds_dict.setdefault(pep[i], []).append(cds[j:j + 3])
        i += 1
        j += 3

    return pep_cds_dict





def single_codon(dict,pep_cds_dict):
    f = open('file_storage/pep_cds_dict', 'w')
    for key, value in dict.items():
        for unit in value:
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                # print(V[1])#蛋白序列
                # print(V[2])#基因序列
                # 在这里做筛选
                if len(V[2]) - 3 == len(V[1]) * 3:  # 选择匹配的情况
                    caculate_cds_pep(V[2], V[1],pep_cds_dict)

    f.write(str(pep_cds_dict))
    print(pep_cds_dict)
    f.close()






def caculate_cds_pep_two(cds, pep,pep_cds_dict_two):
    pep = pep + "*"
    len_cds = len(cds)
    len_pep = len(pep)
    #print(len_cds)
    #print(len_pep)

    i = 0
    j = 0
    while i < len_pep - 1:
        pep_two = pep[i]+pep[i+1]
        cds_two = cds[j]+cds[j+1]+cds[j+2]+" "+cds[j+3]+cds[j+4]+cds[j+5]

        if pep_two in pep_cds_dict_two:
            pep_cds_dict_two.get(pep_two).append(cds_two)
        else:
            pep_cds_dict_two.setdefault(pep_two, []).append(cds_two)
        #print(pep_two)
        #print(cds_two)


        i = i + 1
        j = j + 3

    return pep_cds_dict_two




def double_codon(dict,pep_cds_dict_two):
    f = open('file_storage/pep_cds_dict_two', 'w')
    for key, value in dict.items():
        for unit in value:
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                # print(V[1])#蛋白序列
                # print(V[2])#基因序列
                # 在这里做筛选
                if len(V[2]) - 3 == len(V[1]) * 3:  # 选择匹配的情况
                    caculate_cds_pep_two(V[2], V[1],pep_cds_dict_two)

    f.write(str(pep_cds_dict_two))
    print(pep_cds_dict_two)
    f.close()