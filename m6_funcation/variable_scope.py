'''
x=10
y=11
def main():
    x=20
    print(x)
    print(y)
main()
print(x)
print(y)

def outer():
    def inner():
        print('first')
    def inner2():
        print('second')
    inner() #呼叫inner
    inner2() #呼叫inner2
outer() #呼叫outer

def outer():
    def inner():
        print('first')
        def inner2():
            print('second')
        inner2()
    inner()
outer()#一層層呼叫

x=30
def outer():
    x=20
    print(x)
    def inner():
        x=10
        print(x)
    inner()
    print(x)
outer()
print(x)

x = 10
y = 11
def main():
    x=20
    print(x)
    global y
    y=22
    print(y)
main()
print(x)
print(y)
'''
'''
x = 10
def outer():
    x = 20
    def inner():
        nonlocal x
        print(x)
        x = 30
    inner()
    print(x)
outer()
print(x)
'''
x = 10
def outer():
    x = 20
    def inner():
        nonlocal x
        x = 30
        def inner2():
            nonlocal x
            print(x)
            x=40
        inner2()
        print(x)
    inner()
    print(x)
outer()
print(x)