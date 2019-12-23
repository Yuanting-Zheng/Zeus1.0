import os
os.chdir("2_single")
os.system("python3 single.py")
os.chdir("../3_Pair")
os.system("python3 Pair.py")
os.chdir("../4_translate")
os.system("python3 trans.py")
os.chdir("../5_alignment")
os.system("python3 align.py")






