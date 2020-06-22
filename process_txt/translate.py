import re

f = open("usage.txt","r",encoding="utf-16")
f0 = open("time.txt","w",encoding="utf-16")
f1 = open("mem.txt","w",encoding="utf-16")
f2 = open("cpu.txt","w",encoding="utf-16")
f3 = open("gpu.txt","w",encoding="utf-16")
f4 = open("gpu_mem.txt","w",encoding="utf-16")
"""
try:
    while True:
        contents = f.readline()
        

except EOFError:
    pass
"""

## read time and process
contents = f.readline()
str_no_dot = contents.split(".")
strr =str_no_dot[0]
time = int(strr)
current = time - time
f0.writelines(str(current)+"\n")

## first time for each 
contents = f.readline()
f1.writelines(contents)
contents = f.readline()
f2.writelines(contents)
contents = f.readline()
f3.writelines(contents)
contents = f.readline()
f4.writelines(contents)
contents = f.readline()
##loop process

while True:
    contents = f.readline()
    if contents == '':
        break
    str_no_dot = contents.split(".")
    strr =str_no_dot[0]
    current = int(strr)
    current =current -time
    f0.writelines(str(current)+"\n")
    contents = f.readline()
    f1.writelines(contents)
    contents = f.readline()
    f2.writelines(contents)
    contents = f.readline()
    f3.writelines(contents)
    contents = f.readline()
    f4.writelines(contents)
    contents = f.readline()
    if contents == '':
        break
    