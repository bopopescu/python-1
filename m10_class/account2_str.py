class Account:
    def __init__(self,number,name,balance = 0):
        self.number = number
        self.name = name
        self.balance = balance


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

    def __str__(self):
        return ('number:{0} \nname:{1} \nbalance:{2}'.format(self.number,self.name,self.balance))

def main():
    acc = Account('123456789','Tom',5000)
    print(acc)
    print(acc.balance)







