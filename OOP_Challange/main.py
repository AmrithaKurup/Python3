class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return  (f'Account owner: {self.owner} \nAccount balance: ${self.balance}')

    def deposit(self, cash):
        self.balance = self.balance + cash
        print(f'${cash} credited to your account')

    def withdraw(self, cash):
        self.balance = self.balance - cash
        if self.balance >= 0:
            print(f'${cash} debited from your account')
        else:
            self.balance = self.balance + cash
            print('Funds Unavailable!')


acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
