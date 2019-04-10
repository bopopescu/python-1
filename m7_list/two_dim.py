list1 = [[1,2,3],[4,5,6]]
print(list1[0][0])
print(list1[0][1])
print(list1[0][2])
print(list1[1][0])
print(list1[1][2])

list2 = [[1,2],[3,4],[5,6]]
print(list2[0][0], end=' ')
print(list2[0][1])
print(list2[2][1])
print(list2[1][0])
print(list2[1][1])

list3 = [[1,2],[3,4],[5,6,7]]
print(list3[0][0], end=' ')
print(list3[0][1])
print(list3[1][0])
print(list3[1][1])
print(list3[2][0])
print(list3[2][1])
print(list3[2][2])

print(len(list3))
print(len(list3[0]))
print(len(list3[2]))

print(list3[2])
print(list1[1])
print(list2[0])

for i in range (len(list1)):
    for j in range (len(list1[i])):
        print(list1[i][j],end=' ')
print()
for i in range (len(list3)):
    for j in range (len(list3[i])):
        print(list3[i][j],end=' ')
print()
for i in range(len(list1)):
    print(list1[i])
for i in range(len(list3)):
    print(list3[i])