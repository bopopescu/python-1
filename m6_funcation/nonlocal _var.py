def func():
    x = 10
    def get_x():
        return x
    def set_x(n):
        nonlocal x
        x = n
    return get_x,set_x
getx,setx = func()
x1 = getx()
print(x1)

setx(30)
x1 = getx()
print(x1)