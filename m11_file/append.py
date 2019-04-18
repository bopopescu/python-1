with open('lang.txt','a') as f:

    f.write('C++\n')
    f.write('Javascript\n')
    f.write('C#\n')

    list1 = ['a\n','b\n','c\n']
    f.writelines(list1) #此方法在大量write的情況下效能會比較好