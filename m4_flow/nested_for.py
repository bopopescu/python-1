for i in range (1,10):
    for j in range (1,10):
        print('{0}*{1}={2}'.format(i,j,i*j),end='\t')
    print()
    '''row 跑9次後換行'''
print()
for i in range (1,10):
    for j in range (1,10):
        print('{1}*{0}={2}'.format(i,j,i*j),end='\t')
    print()