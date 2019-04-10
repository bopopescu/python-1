class Account:
    def __init__(self,number,name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit (self,amount):
        try :
            if amount <= 0:
                raise ValueError
            self.balance += amount
        except ValueError:
            print('金額需是正整數')

    def withdraw(self,amount):
        try:
            if amount <= self.balance:
                self.balance -= amount
            else :
                raise ValueError
        except ValueError:
            print('餘額不足')

def main():
    acc = Account('123456789','Tom')
    print(acc.number)
    print(acc.balance)

    amount = eval(input('存入金額 : '))
    acc.deposit(amount)
    print(acc.balance)
    amount = eval(input('領出金額 : '))
    acc.withdraw(amount)
    print(acc.balance)

    acc1 = Account('123456777','Tina')
    print(acc1.number)
    print(acc1.balance)

    amount = eval(input('存入金額 : '))
    acc1.deposit(amount)
    print(acc1.balance)
    amount = eval(input('領出金額 : '))
    acc1.withdraw(amount)
    print(acc1.balance)
    # 變數名稱必須不同，才能保留之前的資料
main()





