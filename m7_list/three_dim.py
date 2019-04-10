list1 = [[[1,2],[3,4]],
         [[5,6],[7,8]],
         [[9,10],[11,12]]
         ]
'''
print(list1)
print(list1[2][1][1],end=' ')#layer,row,col
print(list1[2][1][0],end=' ')
print(list1[2][0][1],end=' ')
print(list1[2][0][0],end=' ')
print(list1[1][1][1],end=' ')
print(list1[1][1][0],end=' ')
print(list1[1][0][1],end=' ')
print(list1[1][0][0],end=' ')
print(list1[0][1][1],end=' ')
print(list1[0][1][0],end=' ')
print(list1[0][0][1],end=' ')
print(list1[0][0][0])

print(list1[0][0])
print(list1[1])
print(len(list1))
'''
'''
for i in range(len(list1)):
    for j in range(len(list1[i])):
        for k in range(len(list1[i][j])):
            print(list1[i][j][k],end=' ')
print()

for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end=' ')
print()

for i in range(len(list1)):
    print(list1[i], end=' ')
'''
import random
lay = eval(input('layer: '))
row = eval(input('row: '))
col = eval(input('col : '))
list2 = []
for i in range(lay):
    list2.append([])
    for j in range(row):
        list2[i].append([])
        for k in range(col):
            list2[i][j].append(random.randint(1,100))
print(list2)