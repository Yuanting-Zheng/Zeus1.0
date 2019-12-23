
def caculate_cds_pep(cds,pep):
    pep_cds_dict = {}
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