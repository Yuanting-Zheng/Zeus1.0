def filter(sequence,k):

    if len(sequence) % 3 != 0:
        return 1    # 长度不是3的倍数

    if sequence[:3] != 'ATG':
        return 2     # 不是起始密码子开头

    if sequence[-3:] not in ['TAA','TGA','TAG']:
        return 3     # 不是终止密码子结尾

    if len(sequence) < int(k):
        return 4        # 长度不符合我们的规定
    cnt = {}
    cnt['A'] = 0
    cnt['T'] = 0
    cnt['C'] = 0
    cnt['G'] = 0
    for i in sequence:
        if i in ["A","T","C","G"]:
            cnt[i]+=1
    if cnt['A']+cnt['T']+cnt['C']+cnt['G'] != len(sequence):
        return 5           #含有非ATCG的字母

    return 6             # 正常的序列

