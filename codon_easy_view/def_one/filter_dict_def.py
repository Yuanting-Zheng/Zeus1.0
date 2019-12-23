def filter_dict(dict,list1,list2,list3):
    list = []
    list.extend(list1)
    list.extend(list2)
    list.extend(list3)
    f = open('file_storage/dict_filter','w')
    n = 1

    gene_to_transcript = {}

    for key, value in dict.items():
        gene_to_transcript[key]=[]
        for unit in value:
            tanscript_to_info = {}
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                if K not in list:
                    tanscript_to_info[K]=V
                    n = n + 1

            gene_to_transcript[key].append(tanscript_to_info)








    print("still have："+str(n))
    f.write(str(gene_to_transcript))
    f.close()







