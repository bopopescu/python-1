tuple1 = (1,2,3,4,5,6)
tuple2 = ('Python','C','Java')

print(tuple2[0])

for i in tuple2:
    print (i,end=' ')
print()
for i in range(len(tuple2)):
    print(i,tuple2[i])
print(sum(tuple1))
print(tuple1.count(5))
print(tuple1.index(1))
print('C' in tuple2)

list1 = ['pp','ss','ls']
tuple3 = tuple(list1)
print(tuple3)

tuple1 += (7,)
print(tuple1)
tuple1 +=(7,8)
print(tuple1)

