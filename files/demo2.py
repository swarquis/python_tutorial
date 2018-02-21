from os import *
from os import path
filename = "D:/redis-64.3.0.503.zip"
re = access(filename, F_OK)
print re
print(path.isfile(filename))

re = access(filename, W_OK)
print re
print(access(filename, R_OK))