'''1加到10'''
n = 1
total = 0
while n<=10 :
    total +=n
    n += 1
print(n,total)
'''10加到1'''
n = 10
total = 0
while n>=1 :
    total +=n
    n -= 1
print(n,total)
'''偶數相加'''
n = 0
total = 0
while n<=10 :
    total +=n
    n += 2
print(n,total)
'''奇數相加'''
n = 1
total = 0
while n<=10 :
    total +=n
    n += 2
print(n,total)
'''for ... in range'''
total = 0
for n in range(1, 11):
    total += n
print(n, total)
'''偶'''
total = 0
for n in range(0, 11,2):
    total += n
print(n, total)
'''奇'''
total = 0
for n in range(1, 11,2):
    total += n
print(n, total)