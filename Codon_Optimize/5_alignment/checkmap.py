import os
import sys
filename = sys.argv[1]
cmd = "muscle -in "+filename+" -clw"
os.system(cmd)
