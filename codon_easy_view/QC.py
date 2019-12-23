#质量检测模块
from def_one.checkdef import *
from def_one.filter_dict_def import *

# import raw data
f11 = open('file_storage/rawdata','r')
a = f11.read()
data_dict = eval(a)
f11.close()

##QC check
#summary。 count how many genes transcript and Each gene corresponds to how many transcripts
structure_check(data_dict)

#length long check, four situations
filter_lenth_key = []
lenth_check(data_dict,filter_lenth_key)
#print(filter_lenth__key)
#print(len(filter_lenth__key))

# Abnormal check does Amino acid begin with M | cds include * | pep has *
filter_irregular_key = []
irregular_check(data_dict,filter_irregular_key)
#print(filter_irregular_key)
#print(len(filter_irregular_key))

# rare codons check
# There are two rare codons, one is a rare amino acid and the other is not in a standard codon list.
filter_rarecodon_key =[]
rarecondon_check(data_dict,filter_rarecodon_key)
#print(filter_rarecodon_key)
#print(len(filter_rarecodon_key))


##QC filter


f = open('file_storage/dict_original','w')
f.write(str(data_dict))
f.close()

#filter_lenth_key = []
#filter_irregular_key = []
#filter_rarecodon_key = []
filter_dict(data_dict,filter_lenth_key,filter_irregular_key,filter_rarecodon_key)









