from m10_class.account2_str import Account
from m10_class.checkingaccount import checkingaccount
def main():
    acc = Account('123456789','Tom',5000)
    acc.deposit(500)
    acc.withdraw(800)
    print(acc)
    ca = checkingaccount('7654321','Tina',50000,100000)
    ca.deposit(5000)
    ca.withdraw(70000)
    print(ca)

main()





