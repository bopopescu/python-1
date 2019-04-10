try:
    num = int(input('input 0 ~100:'))
    if num < 0 or num > 100:
        raise ValueError
    print('score is {}'.format(num))
except ValueError as e :
    print("input number out of range '{}'".format(num))