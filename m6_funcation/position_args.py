def msg (name,age):
    print("{0} is {1} years old!!".format(name,age))

msg('Tom', 25)
msg('Tom', age=25)
msg(name='Tom', age=25)
msg(age=25,name='Tom')
