def fac(a):
    total=1
    for n in range(1,(a+1)):
        total *= n
    return total
def main():
    a = eval(input('Number: '))
    print(fac(a))

main()