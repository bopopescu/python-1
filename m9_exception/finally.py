try:
    n1,n2 = eval(input("Enter 2 numbers to divide : "))
    div = n1 / n2
    print('{} / {} = {} '.format(n1,n2,div))
except ZeroDivisionError:
    print('Division error')
except SyntaxError:
    print('Comma is missing')
except NameError:
    print('Input number!!!!')
except:
    print('Something wrong')
else:
    print('No exception')
finally:
    print('Must be done')


