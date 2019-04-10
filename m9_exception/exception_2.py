try:
    num = int(input('input number:'))
    print('{} is a {}'.format(num,'odd' if num%2 else 'even'))
except ValueError as e :
    print("please in put a number no a string !")