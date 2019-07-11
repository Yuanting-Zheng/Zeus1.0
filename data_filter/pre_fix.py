import sys
file = sys.argv[1]
f = open(file,'r')
lines = f.readlines()

name2 = file+"_standard"
f2 = open(name2,"w")
for line in lines:
    line = line.strip()
    if ">" in line:
        name = line.split(' ')[0]
        f2.write("\n"+name+"\n")
    else:
        f2.write(line)

f.close()
f2.close()