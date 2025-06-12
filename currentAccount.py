from account import Account
class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)
    
currentAccount = CurrentAccount(200000)
currentAccount.deposit(1000)
print(currentAccount.balance)