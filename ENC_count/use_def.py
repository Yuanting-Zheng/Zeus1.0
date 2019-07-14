from use_class import GENE
def handle_text(gene_text):
    gene_text_lines = gene_text.split('\n')
    sequence = ''
    name = ''
    gene_objs = []
    for line in gene_text_lines:
        line = line.strip()
        if line == '':
            break
        if line[0] == '>':
            if sequence != '' and name != '':

                gene_objs.append(GENE(sequence, name))


            sequence = ''
            name = line.split(' ')[0]
            continue
        sequence+=line
    if sequence != '' and name != '':

        gene_objs.append(GENE(sequence, name))


    return gene_objs