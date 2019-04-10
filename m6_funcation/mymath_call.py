import m6_funcation.my_math

print(m6_funcation.my_math.mypow(2,3))
print(m6_funcation.my_math.mysum(2,3))
print(m6_funcation.my_math.myabs(-8))

import m6_funcation.my_math as my_math

print(my_math.mypow(2,3))
print(my_math.mysum(2,3))
print(my_math.myabs(-8))

from m6_funcation.my_math import *
print(mypow(2,8))
print(mysum(8,7))
print(myabs(-87))

print(dir(m6_funcation.my_math))