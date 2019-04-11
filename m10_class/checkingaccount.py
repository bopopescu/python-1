from m10_class.account2_str import Account
class checkingaccount(Account):
    def __init__(self,number,name,balance = 0,credit_limit = 10000):
        super(checkingaccount,self).__init__(number,name,balance)
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
        return (super(checkingaccount,self).__str__() + ' \ncredit_limit{}'.format(self.credit_limit))

def main():
    acc = Account('123456789','Tom',5000)
    print(acc)
    ca = checkingaccount('7654321','Tina',50000,100000)
    print(ca)







