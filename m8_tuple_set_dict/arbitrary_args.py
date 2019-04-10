def greet(*names):
    for name in names:
        print("Hello",name)
greet('TOM','HOME','JERRY','ILLY')

tuple1 = ('tom','home','kiki','nina')
greet(*tuple1)
list1 = ['tom','home','kiki','nina']
greet(*list1)
str1 = 'python'
greet(*str1)

def stu (**data):
    for key,value in data.items():
        print("{} is {}".format(key,value))
stu(name = "TOM",age = "25",mobile = "034582202")
stu(name = "JIMMY",age = "33",email="J123@gmail.com",mobile="0955874441")

student = {'name' :"JIMMY",'age' : "33",'email':"J123@gmail.com",'mobile':"0955874441"}
stu(**student)

