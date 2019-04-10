class Account:
    pass
def deposit (acc,amount):
    try :
        if amount <= 0:
            raise ValueError
        acc.balance += amount
    except ValueError:
        print('金額需是正整數')

def withdraw(acc,amount):
    try:
        if amount <= acc.balance:
            acc.balance -= amount
        else :
            raise ValueError
    except ValueError:
        print('餘額不足')

def main():
    acc = Account()
    acc.balance = 0
    acc.number = '123456789'
    acc.name = 'Tom'

    print(acc.number)
    print(acc.balance)

    amount = eval(input('存入金額 : '))
    deposit(acc,amount)
    print(acc.balance)
    amount = eval(input('領出金額 : '))
    withdraw(acc,amount)
    print(acc.balance)

    acc1 = Account()
    acc1.balance = 0
    acc1.number = '123456777'
    acc1.name = 'Tina'

    print(acc1.number)
    print(acc1.balance)

    amount = eval(input('存入金額 : '))
    deposit(acc1, amount)
    print(acc1.balance)
    amount = eval(input('領出金額 : '))
    withdraw(acc1, amount)
    print(acc1.balance)
# 變數名稱必須不同，才能保留之前的資料

main()



