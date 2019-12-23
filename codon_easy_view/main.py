#主调度文件
import os
from def_one.filedef import *
print("Hello, welcome to use Codon Easy View! ")
print("Codon Easy View now has four functions: ")
print("press 1, you can get QC result\n"
      "press 2, you can check you pep length result\n"
      "press 3, you can get codon bias result\n"
      "press 4, you can save you result into a local file\n"
      "press 5, exit\n"
      "Attention: you must press 1 before other actions at the first time")

print("please input your raw data and press 1 first, then you can \
filter your data and get other results")

ready = input("Is the raw data ready？(Y/N)")
while ready != "Y":
    print("please input the raw data")
    ready = input("Is the raw data ready？(Y/N):")

# import raw data
f = open('file_storage/rawdata','w')
data_dict = process_file('E_cds.fa','E_pep.fa')
f.write(str(data_dict))
f.close()




signal = input("What do you want to do: ")

while signal != "5":
    if signal == "1":
        os.system('python3.5 QC.py')
        signal = input("What do you want to do：")

    if signal == "2":
        os.system('python3.5 length.py')
        sig = input("Do you want to visualize the results? (Y/N)")
        if sig == "Y":
            os.system('python3.5 length_html.py')
        signal = input("What do you want to do: ")


    if signal == "3":
        os.system('python3.5 bias.py')
        sig = input("Do you want to visualize the results? (Y/N)")
        if sig == "Y":
            os.system('python3.5 bias_html.py')
        signal = input("What do you want to do: ")

    if signal == "4":
        os.system('python3.5 save.py')
        signal = input("What do you want to do: ")
    else:
        signal = input("What do you want to do: ")

print("See you")