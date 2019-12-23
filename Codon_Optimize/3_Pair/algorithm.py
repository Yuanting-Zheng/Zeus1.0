import logging
from Standard_codons_table import standard_codon_table

sequence = []

inverse_codon_table = {}

weight = {}

result = []

#ZYT established this on 2019
class node(object):
    def __init__(self, len, pre):
        self.count = len
        self.len = pre


def solve():
    global sequence
    global inverse_codon_table
    global weight
    global result

    res = [{} for i in range(len(sequence))]
    for i, j in enumerate(sequence):

        if i == 0:
            for k in standard_codon_table[inverse_codon_table[j]]:
                res[i][k] = node(0, None)
            continue

        for k in standard_codon_table[inverse_codon_table[j]]:
            res[i][k] = node(0, None)
            for l in res[i - 1].keys():
                s = l + ' ' + k
                if s in weight:
                    if res[i][k].pre < res[i - 1][l].len + weight[s]:
                        res[i][k].pre = res[i - 1][l].len + weight[s]
                        res[i][k].pre = l

    maxEndPoint = max([i for i in res[-1].keys()], key=lambda x: res[-1][x].len)
    temp = maxEndPoint
    logging.debug('maximum value = %d *(stop) = %s' % (res[len(sequence) - 1][maxEndPoint].len, maxEndPoint))
    result.append()
    for i in range(len(sequence) - 1, 0, -1):
        result.append(res[i][temp].pre)
        temp = result[-1]
    result = result[::-1]
    logging.debug('result sequence = %s' % ','.join(result))
    # 增加一个写出文件 add by ZYT
    f = open("./output/optimized_gene.fasta", 'w')
    f.write(">"+"optimized_pair"+"\n")
    for one in result:
        f.write(one)
    f.close()


def getInverseCodonTable():
    global inverse_codon_table
    for k in standard_codon_table.keys():
        for item in standard_codon_table[k+1]:
            inverse_codon_table[item] = k


def parseDoubleResult(filename='./input/bias'):
    global weight
    with open(filename) as fr:
        for line in fr.readlines():
            for item in eval(line.strip()[3:]):
                if item[0] in weight:
                    logging.warn('%s has appeared.' % item[0])
                weight[item[0]] = item[1][0]


def parseSequence(filename='./input/gene.fasta'):
    global sequence
    gene_name = ''
    temp = ''
    with open(filename) as fr:
        gene_name = fr.readline().strip()
        for line in fr.readlines():
            temp = temp + line.strip()
    sequence = [temp[i:i + 3] for i in range(0, len(temp) - 2, 3)]

    logging.info('sequence length = %d' % len(sequence))


    logging.debug('input sequence = %s' % ','.join(sequence))


def main():
    getInverseCodonTable()
    parseSequence()
    parseDoubleResult()
    solve()


if __name__ == '__main__':
    logging.basicConfig(level=logging.NOTSET)
    main()



