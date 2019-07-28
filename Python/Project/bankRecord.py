class Bank():
    def __init__(self, accountName, balance):
        self.accountName = accountName
        self.balance = balance
        print("Account Owner: ", self.accountName)
        print("Account Balance: ", self.balance)
    
    def deposit(self, dep_amount):
        self.balance += dep_amount
        print('Deposit Accepted!!!')
    
    def withdraw(self, withdrawAmount):
        if withdrawAmount <= self.balance:
            print('Withdrawal Accepted')
            self.balance = self.balance - withdrawAmount
            print('Balance Amount:', self.balance)
        else:
            print('Amount unavailable, cant perform the action!!!')
            print('Balance Amount:', self.balance)


myAccount = Bank('SKK', 200000)
myAccount.deposit(25000)
myAccount.withdraw(200000)
myAccount.withdraw(100000)
