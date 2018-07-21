#
#
#   18.05.31
#   은행 계좌 클래스 상속 + 부모 클래스의 메소드 deposit를 이용하기
#


class BankAccount():
    def __init__(self, name, number, balance):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def deposit(self, amount):      
        self.balance += amount
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name, number, balance, interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate
    '''
    def add_interest(self):
        self.balance += self.balance * self.interest_rate
    '''
    def add_interest(self):         # Use parent class's method.
        BankAccount.deposit(self, self.balance * self.interest_rate)

    def __str__(self):
        return " name : %s\n number : %s\n balance : %s" % \
               (str(self.name), str(self.number), str(self.balance))

class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withdraw_charge = 10000

    def withdraw(self, amount):     # Use parent class's method.
        return BankAccount.withdraw(self, amount + self.withdraw_charge)

a1 = SavingsAccount("홍길동", 123456, 10000, 0.05)
a1.add_interest()
print("저축예금의 잔액 = ", a1.balance)

a2 = CheckingAccount("김철수", 123457, 2000000)
a2.withdraw(100000)
print("당좌예금의 잔액 = ", a2.balance)

print(a1)
