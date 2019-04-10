list1 = [45,67,88,39,11,34,90,88]
list1.append(777)
print(list1)

list2 = []
list2.append(54)
print(list2)

list1.insert(1,888)
print(list1)
print(list1.pop(1))
print(list1)
print(list1.pop(3))
print(list1)
print(list1.count(88))
print(list1.index(67))
list1.remove(88)
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)