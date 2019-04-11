from m10_class.account2_str import Account
class checkingaccount(Account):
    def __init__(self,number,name,balance = 0,credit_limit = 10000):
        self.number = number
        self.name = name
        self.balance = balance
        self.credit_limit = credit_limit

    def withdraw(self,amount):
        try:
            if amount <= self.balance + self.credit_limit:
                self.balance -= amount
            else :
                raise ValueError
        except ValueError:
            print('餘額不足')

    def __str__(self):
        return ('number:{0} \nname:{1} \nbalance:{2} \ncredit_limit{3}'.format(self.number,self.name,self.balance,self.credit_limit))

def main():
    acc = Account('123456789','Tom',5000)
    print(acc)
    ca = checkingaccount('7654321','Tina',50000,100000)
    print(ca)







