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
                sequence = sequence[3:-3]
                gene_objs.append(GENE(sequence, name))
                gene_objs[-1].delete_codons()

            sequence = ''
            name = line.split(' ')[0]
            continue
        sequence+=line
    if sequence != '' and name != '':
        sequence = sequence[3:-3]
        gene_objs.append(GENE(sequence, name))
        gene_objs[-1].delete_codons()

    return gene_objs