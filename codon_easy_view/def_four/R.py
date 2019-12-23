def r_view_single(dict):
    f = open('R/single','w')
    f.write('codon frequency'+'\n')

    for key, value in dict.items():
        for K, V in value.items():
            f.write(K+' '+str(V[1])+'\n')

    f.close()

def r_view_double(dict):
    f = open('R/double','w')
    f.write('codon frequency'+'\n')

    for key,value in dict.items():
        #print(key)
        for K,V in value.items():
            f.write(K.replace(' ','_') + ' ' + str(V[0]) + '\n')

    f.close()


