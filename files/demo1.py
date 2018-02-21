from os import listdir
import os
from os.path import isdir, isfile

dir = "D:\cddsyy"
dirlist = listdir(dir)
dest = "D:/temp"
srcdir = []
for i in dirlist:
    if isdir(os.path.join(dir,i)):
        pass
        #print(i+" is directory")
    elif isfile(os.path.join(dir,i)):
        #print(i+" is file")
        srcdir.append(i)
#for i in srcdir:
#    with open(os.path.join(dest,i),'w') as f:
#        f.write(os.path.join(dir,i))

for i in srcdir:
    j = i

    j = j.replace('.asp','.php')
    with open(os.path.join(dest,j), 'w') as f:
        f.write(os.path.join(dir,i))
