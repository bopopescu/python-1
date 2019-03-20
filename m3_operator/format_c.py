a= 123
b= 12345.678
c= 'python'
print('/'+'%5d' % a +'/')
print('/'+'%10.2f' % b +'/')
print('/'+'%10.2e' % b +'/')
print('/'+'%10.2E' % b +'/')
print('/'+'%10s' % c +'/')

print('/'+'%-5d' % a +'/')
print('/'+'%-10.2f' % b +'/')
print('/'+'%-10.0f' % b +'/')
print('/'+'%-10.2e' % b +'/')
print('/'+'%-10.2E' % b +'/')
print('/'+'%-10s' % c +'/')

print('/'+'%5x' % a +'/')
print('/'+'%5X' % a +'/')
print('/'+'%#5X' % a +'/')
print('/'+'%05d' % a +'/')
print('/'+'%5o' % a +'/')
print('/'+'%#5o' % a +'/')
print('/'+'%5d%%' % a +'/')
print('/'+'%+5d' % a +'/')
print('/'+'%5d %10.2f %10s' % (a,b,c) +'/')


print('/' + '%10r' % 'aaaa\thhh' + '/')
print('/' + '%10s' % 'aaaa\thhh' + '/')
print('/' + '%15s' % 'aaaa\thhh' + '/')
