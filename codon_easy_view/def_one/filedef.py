def process_file(cds,pep):
    f_cds_file = open(cds, "r")
    f_pep_file = open(pep, "r")
    f_cds_change = open("file_storage/cds_change", "w")
    f_pep_change = open("file_storage/pep_change", "w")
    lines_cds = f_cds_file.readlines()
    f_cds_change.write(lines_cds[0].strip() + "+++")
    for line_cds in lines_cds[1:]:
        line_cds = line_cds.strip()
        if '>' in line_cds:
            f_cds_change.write("\n" + line_cds + "+++")
        if '>' not in line_cds:
            f_cds_change.write(line_cds)
    lines_pep = f_pep_file.readlines()
    f_pep_change.write(lines_pep[0].strip() + "+++")
    for line_pep in lines_pep[1:]:
        line_pep = line_pep.strip()
        if '>' in line_pep:
            f_pep_change.write("\n" + line_pep + "+++")
        if '>' not in line_pep:
            f_pep_change.write(line_pep)
    f_cds_file.close()
    f_pep_file.close()
    f_cds_change.close()
    f_pep_change.close()
    #### produce sp file
    f = open("file_storage/pep_change", "r")
    f2 = open("file_storage/cds_change", "r")

    ## put cds in complex
    cds_ref = {}  # dict store cds
    cds_lines = f2.readlines()
    for line in cds_lines:
        # split title and seq
        line = line.strip()
        unit = line.split("+++")
        title = unit[0]
        seq = unit[1]

        # split title
        seq_info = title.split(' ', 5)
        seq_info[0] = seq_info[0].replace(">", "")  # Trans

        # transcript - > cds
        cds_ref[seq_info[0]] = seq
    ## cds done


    ## pep in complex
    seqs_ref = {}  # dict store pep
    lines = f.readlines()  #
    for line in lines:
        #split title and seq
        line = line.strip()
        unit = line.split("+++")
        title = unit[0]
        seq = unit[1]

        # split title
        seq_info = title.split(' ', 6)
        seq_info[3] = seq_info[3].replace("gene:", "")  # gene
        seq_info[4] = seq_info[4].replace("transcript:", "")  # transcript
        seq_info[6] = seq_info[6].replace("transcript_biotype:", "")  # transcript_biotype

        #  transcript_biotype split
        gdef = "ND"
        if " " in seq_info[6]:
            two_parts = seq_info[6].split(" ", 1)
            seq_info[6] = two_parts[0]
            gdef = two_parts[1]

        # Trans to list

        # dict
        Transcript = {}
        # list
        list = []
        # in list
        list.append(gdef)
        list.append(seq)

        # cds in list
        list.append(cds_ref[seq_info[4]])

        # key - value
        Transcript[seq_info[4]] = list
        # gene - trans
        if seq_info[3] in seqs_ref:

            seqs_ref.get(seq_info[3]).append(Transcript)
        else:
            seqs_ref.setdefault(seq_info[3], []).append(Transcript)
    ## complex seqs_ref done

    f.close()
    f2.close()


    return seqs_ref

