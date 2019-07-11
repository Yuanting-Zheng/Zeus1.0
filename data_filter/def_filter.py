def filter(sequence,k):

    if len(sequence) % 3 != 0:
        return 1    #

    if sequence[:3] != 'ATG':
        return 2     #

    if sequence[-3:] not in ['TAA','TGA','TAG']:
        return 3     #

    if len(sequence) < int(k):
        return 4        #
    cnt = {}
    cnt['A'] = 0
    cnt['T'] = 0
    cnt['C'] = 0
    cnt['G'] = 0
    for i in sequence:
        if i in ["A","T","C","G"]:
            cnt[i]+=1
    if cnt['A']+cnt['T']+cnt['C']+cnt['G'] != len(sequence):
        return 5           #

    return 6             #

