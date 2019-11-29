class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, num):
        self.balance += num
        return self.balance


    def withdraw(self, num):
        self.balance -= num
        return self.balance



class MinimumBalanceAccount(BankAccount):
    def __init__(self,minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance


    def withdraw(self,num):
        if self.balance - num > self.minimum_balance:
            return BankAccount.withdraw(self,num)
        else:
            return None

money = MinimumBalanceAccount(100)
money.deposit(2000)
print(money.balance)
money.withdraw(990)
print(money.balance)
