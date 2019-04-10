set1 = {1,2,3,4,5,6}
set2 = {'python','c','java'}
print(set1)
print(set2)
print(type(set1))

list1 = [35,43,32,54,66,77,77] #重複項轉換成set會被刪除
set3 = set(list1)
print(set3)
tuple1 = (1,2,3,4,5,6,7,7)
set4 = set(tuple1)
print(set4)

set2.add('C++');
print(set2)
set2.remove('c')
print(set2)

set1 = {1,2,3,5,8}
set2 = {1,3,5,7,9}
print(set1 | set2)
print(set1&set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)

set1 = {1,2,3,5,8}
set2 = {1,3,5}
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2 == set1)
print(set2 != set1)