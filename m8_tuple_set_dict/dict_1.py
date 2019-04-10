dict1 = {'name':'Tom','age':25,'mobile':'0922454878'}
dict2 = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
print(dict1['name'])
print(dict2.get(13))

for key in dict1:
    print('%s :  %s' % (key,dict1[key]))

print(dict1.keys())
print(dict1.values())

print(list(dict1.keys()))
print(list(dict1.values()))

print(tuple(dict1.keys()))
print(tuple(dict1.values()))

print(dict1.items())
print(tuple(dict1.items()))
print(list(dict1.items()))

for key,value in dict1.items():
    print('%s :  %s' % (key,value))

print(len(dict1))
print('name' in dict1)

dict3 = {'name':'Tom','mobile':'0922454878','age':25,}
print(dict1 == dict3)

dict1['email'] = 'Tomisboy@gmail.com'
print(dict1)
del dict3['age']
print(dict3)
print(dict3.pop('name'))
print(dict3)
dict3.clear()
print(dict3) #會保留dict3

dict3 = dict1.copy()
print(dict3)
dict3 = {'name':'Tom','mobile':'0922454878','age':32,'id':'H1222334441'}
dict1.update(dict3)
print(dict1)