def greet(*names):
    for name in names:
        print("Hello",name)
greet('TOM','HOME','JERRY','ILLY')

def stu (**data):
    for key,value in data.items():
        print("{} is {}".format(key,value))
stu(name = "TOM",age = "25",mobile = "034582202")
stu(name = "JIMMY",age = "33",email="J123@gmail.com",mobile="0955874441")