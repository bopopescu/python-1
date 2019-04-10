list1 = [i for i in range(1,11)]
print(list1)
list2 = [i*i for i in range(1,10)]
print(list2)
dict1 = {i:i*i for i in range(1,10)}
print(dict1)
gen1 = (i**i for i in range(1,5))
print(gen1)
for n in gen1:
    print(n,end=' ')
print()

evens = [i for i in range(1,51) if i%2 == 0]
print(evens)
odds = [i for i in range(1,51) if i%2 != 0]
print(odds)
odds = [i for i in range(1,51) if i % 2] #因為python 的true&false 就是 1&0
print(odds)
evens = [i for i in range(1,51) if not(i%2)]
print(evens)
prime = [x for x in range(2,101) if ((x % 6) == 5 and (x % 5) != 0 and (x % 7) != 0) or ((x%6)==1 and (x%5)!=0 and (x%7)!=0) or (x==2 or x== 3 or x==5 or x==7)]
print(prime)

