with open('lang.txt','r') as f :
    line = f.readline()
    while line != '':
        print(line,end='')
        line = f.readline()
print("=================================")

with open('lang.txt','r') as f :
    line = f.readline()
    while line != '':
        print(repr(line))
        line = f.readline()

print("=================================")

with open('lang.txt','r') as f:
    data = f.read()
    print(data)
    print(repr(data))
print("=================================")
with open('lang.txt','r') as f:
    data = f.read(14)
    print(data)
    data = f.read(10)
    print(data)
print("=================================")

with open('lang.txt','r') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line,end='')
print("=================================")
import  os
with open("lang.txt",'r') as f:
    f.seek(10,os.SEEK_SET)#跟f.seek(10,0)一樣
    print(f.read(10))
