print('{0} is {1} years old !' .format('TOM',30))
print('{1} is {0} years old !' .format(30,'TOM'))
print('{} is {} years old !' .format('TOM',30))
print('{name} is {age} years old !' .format(name='TOM',age=30))
print('{name} is {age} years old !' .format(age=30,name='TOM'))
print('{} is {age} years old !' .format('TOM',age=30))

print('{0} is {1} years old ! He is {2}m!!' .format('TOM',30,1.8872))
print('{0} is {1} years old ! He is {2: .2f}m!!' .format('TOM',30,1.8872))

print('String : {:>10s}'.format('GM'))
print('String : {:^10s}'.format('GM'))
print('String : {:<10s}'.format('GM'))
print('String : {:-^10s}'.format('GM'))

