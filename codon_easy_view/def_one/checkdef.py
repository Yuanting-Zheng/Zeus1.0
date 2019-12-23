from file_storage.Standard_codons_table import *


def structure_check(dict):
    f3 = open("check_result/structure_check_result",'w')

    i = 0
    for key, value in dict.items():
        i += 1
    print("genes：")
    print(i)

    k = 0
    for key, value in dict.items():
        for unit in value:
            k += 1
    print("transcripts：")
    print(k)

    f_structure = open("file_storage/pep_change", "r")
    f3.write("total have " + str(i) + " genes" + "\n")
    f3.write("total have " + str(k) + " transcripts" + "\n")

    structure_seqs_ref = {}
    structure_seqs_ref2 = {}
    structure_conden = {}
    structure_biotype_ref = {}

    structure_lines = f_structure.readlines()

    for structure_line in structure_lines:
        structure_line = structure_line.strip()
        structure_unit = structure_line.split("+")
        structure_title = structure_unit[0]
        structure_seq = structure_unit[1]

        structure_seq_info = structure_title.split(' ', 6)
        structure_seq_info[3] = structure_seq_info[3].replace("gene:", "")  # gene
        structure_seq_info[4] = structure_seq_info[4].replace("transcript:", "")  # transcript
        structure_seq_info[5] = structure_seq_info[5].replace("gene_biotype:", "")  # gene_biotype
        structure_seq_info[6] = structure_seq_info[6].replace("transcript_biotype:", "")  # transcript_biotype
        # f1.write(seq_info[6] + "\n")
        structure_gdef = "ND"
        if " " in structure_seq_info[6]:
            structure_two_parts = structure_seq_info[6].split(" ", 1)
            structure_seq_info[6] = structure_two_parts[0]
            structure_gdef = structure_two_parts[1]

        if structure_seq_info[5] in structure_biotype_ref:
            structure_biotype_ref.get(structure_seq_info[5]).append(structure_seq_info[3])
        else:
            structure_biotype_ref.setdefault(structure_seq_info[5], []).append(
                structure_seq_info[3])  # gene_biotype ->  gene

        if structure_seq_info[3] in structure_seqs_ref2:
            structure_seqs_ref2.get(structure_seq_info[3]).append(structure_seq_info[4])
        else:
            structure_seqs_ref2.setdefault(structure_seq_info[3], []).append(structure_seq_info[4])  # gen -> transcript

        structure_seq_info[4] = []
        structure_seq_info[4].append(structure_gdef)  # transcript -> def + seq
        structure_seq_info[4].append(structure_seq)
        structure_seqs_ref[structure_seq_info[3]] = structure_seq_info[4]  # gen -> transcript(列表)

    print("transcript attributes diffs ，each numbers below:")
    f3.write("transcript attributes diffs ，each numbers below:" + "\n")
    for structure_key in structure_biotype_ref.keys():
        print(structure_key + ":" + (str(len(structure_biotype_ref[structure_key]))))
        f3.write(structure_key + ":" + (str(len(structure_biotype_ref[structure_key]))) + "\n")

    structure_gcnt = 0
    structure_tcnt = 0
    structure_tcnt = {}

    print("total have " + str(len(structure_seqs_ref2)) + " genes，one gene points to several transcripts：")
    f3.write("total have " + str(len(structure_seqs_ref2)) + " genes，one gene points to several transcripts：" + "\n")
    for structure_key in structure_seqs_ref2.keys():
        if str(len(structure_seqs_ref2[structure_key])) in structure_tcnt:
            structure_tcnt[str(len(structure_seqs_ref2[structure_key]))] += 1
        else:
            structure_tcnt[str(len(structure_seqs_ref2[structure_key]))] = 1

    for structure_key in structure_tcnt.keys():
        print(structure_key + " : " + str(structure_tcnt[structure_key]))
        f3.write(structure_key + " : " + str(structure_tcnt[structure_key]) + "\n")
    f_structure.close()
    f3.close()



def irregular_check(dict,filter_irregular_key):
    count_num = 0
    f5 = open('check_result/irregular_check_result','w')
    for key, value in dict.items():
        for unit in value:
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                pep = V[1]
                cds = V[2]

                if pep[0] != 'M':
                    print("Amino acid not begin with M")
                    print(K + '\n' + cds + '\n' +pep)
                    f5.write("Amino acid not begin with M"+'\n')
                    f5.write(K + "\n")
                    f5.write(cds + "\n")
                    f5.write(pep + "\n")
                    filter_irregular_key.append(K)

                if '*' in pep:
                    print("pep has *")
                    print(pep)
                    print(K + '\n' + cds + '\n' + pep)
                    f5.write("pep has *" + '\n')
                    f5.write(K + "\n")
                    f5.write(cds + "\n")
                    f5.write(pep + "\n")
                    filter_irregular_key.append(K)

                if '*' in cds:
                    print("cds include *")
                    print(cds)
                    print(K + '\n' + cds + '\n' + pep)
                    f5.write("cds include *" + '\n')
                    f5.write(K + "\n")
                    f5.write(cds + "\n")
                    f5.write(pep + "\n")
                    filter_irregular_key.append(K)

                count_num += 1



    print("total check number：")
    f5.write("total check number："+'\n')
    print(count_num)
    f5.write(str(count_num) + '\n')

    f5.write("total check " + str(count_num) + " transcripts" + "\n")

    f5.close()



def lenth_check(dict,filter_lenth_key):
    count_num = 0
    global n__1
    global n__2
    global n__3
    global n__4
    n__1 = 0  # lenth_cds == lenth_pep*3
    n__2 = 0  # lenth_cds-3 == lenth_pep*3
    n__3 = 0  # lenth_cds-1 == lenth_pep*3
    n__4 = 0  # lenth_cds-2 == lenth_pep*3
    f4 = open('check_result/length_check_result', 'w')
    for key, value in dict.items():
        for unit in value:
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                pep = V[1]
                cds = V[2]
                lenth_cds = len(cds)
                lenth_pep = len(pep)

                if lenth_cds == lenth_pep * 3:
                    #global n__1
                    n__1 = n__1 + 1

                if lenth_cds - 3 == lenth_pep * 3:
                    #global n__2
                    n__2 = n__2 + 1

                if lenth_cds - 1 == lenth_pep * 3:
                    #global n__3
                    n__3 = n__3 + 1

                if lenth_cds - 2 == lenth_pep * 3:
                    #global n__4
                    n__4 = n__4 + 1

                if lenth_cds != lenth_pep * 3:
                    if lenth_cds - 3 != lenth_pep * 3:
                        if lenth_cds - 1 != lenth_pep * 3:
                            if lenth_cds - 2 != lenth_pep * 3:
                                print("this lengths has big problem not in four:")
                                f4.write("this lengths has big problem not in four:")
                                # if have problem, we will write it in f4
                                f4.write(K)
                                f4.write(cds + "\n")
                                f4.write(pep + "\n")
                                filter_lenth_key.append(K)


                count_num += 1

    print("total check number：")
    f4.write("total check number："+'\n')
    print(count_num)
    f4.write(str(count_num) + '\n')

    f4.write("total check " + str(count_num) + " transcripts" + "\n")
    f4.write("cds*3 = pep：" + str(n__1) + "\n")
    f4.write("(cds-3)*3 = pep, 3 is Terminate codon：" + str(n__2) + "\n")
    f4.write("(cds-1)*3 = pep：" + str(n__3) + "\n")
    f4.write("(cds-2)*3 = pep：" + str(n__4) + "\n")
    f4.write("four situations all：" + str(n__1 + n__2 + n__3 + n__4) + "\n")
    print("cds*3 = pep：")
    print(n__1)
    print("(cds-3)*3 = pep, 3 is Terminate codon：")
    print(n__2)
    print("(cds-1)*3 = pep：")
    print(n__3)
    print("(cds-2)*3 = pep：")
    print(n__4)
    print("four situations all：")
    print(n__1 + n__2 + n__3 + n__4)

    f4.close()



def rarecondon_check(dict,filter_rarecodon_key):
    count_num = 0
    f6 = open('check_result/rare_codons_check_results', 'w')
    for key, value in dict.items():
        for unit in value:
            dict_trans = unit.copy()
            for K, V in dict_trans.items():
                pep = V[1]
                cds = V[2]
                count_num = count_num + 1
                #print(count_num)
                pep_num = 0

                rare_pep = []
                while pep_num < len(pep):
                    if pep[pep_num] not in standard_codon_table.keys():
                        filter_rarecodon_key.append(K)
                        print("has rare codons：")
                        print(K + '\n' + pep + '\n' + cds)
                        f6.write("has rare codons：" + K + '\n' + pep + '\n' + cds + '\n')
                        rare_pep.append(pep[pep_num])


                    pep_num = pep_num + 1


                # attention there is filter when did length check, but E.cool do not need


                lenth_pep = len(pep)
                pep = pep + "停"
                i = 0
                j = 0
                k = lenth_pep
                while i < k + 1:
                    if pep[i] in rare_pep:
                        print('raw Amino acid：')
                        print(cds[j:j + 3]+':'+pep[i])
                        f6.write(cds[j:j + 3] + ':' + pep[i] + '\n')
                        f6.write("raw Amino acid：" + K + '\n' + pep + '\n' + cds + '\n')
                        filter_rarecodon_key.append(K)
                        i += 1
                        j += 3
                        continue


                    if cds[j:j + 3] not in standard_codon_table[pep[i]]:
                        filter_rarecodon_key.append(K)
                        print(cds[j:j + 3]+':'+pep[i])
                        f6.write(cds[j:j + 3]+':'+pep[i]+ '\n')
                        print("not in a standard codon list：")
                        print(K + '\n' + pep + '\n' + cds)
                        f6.write("not in a standard codon list：" + K + '\n' + pep + '\n' + cds + '\n')
                    i += 1
                    j += 3




    print("total check number:")
    f6.write("total check number：" + '\n')
    print(count_num)
    f6.write(str(count_num) + '\n')

    f6.write("total check " + str(count_num) + " transcript" + "\n")

    f6.close()


