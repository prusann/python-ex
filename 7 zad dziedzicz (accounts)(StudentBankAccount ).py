class BankAccount:
    def __init__(self,owner,balance,bank):
         self.owner = owner
         self.balance = balance
         self.bank = bank
    def get_owner(self):
        return "get_owner"
    def get_balance(self):
        return 'get_balance'
    def get_bank(self):
        return 'get_bank'
    def set_balance(self):
        return 'set_balance'        
bank = BankAccount("x",12,"yyy")
print(bank.get_owner())
print(bank.get_balance())
print(bank.get_bank())
print(bank.set_balance())

class StudentBankAccount(BankAccount):
    def __init__(self,overdraft_balance,overdraft_limit):
         self.overdraft_balance = overdraft_balance
         self.overdraft_limit = overdraft_limit
    def get_overdraft_balance(self):
        return "get_overdraft_balance"
    def set_overdraft_balance(self):
        return 'set_overdraft_balance'
    def get_overdraft_limit(self):
        return 'get_overdraft_limit'
    def set_overdraft_limit(self):
        return 'set_overdraft_limit'        
bank2 = StudentBankAccount("x",12)
print(bank2.get_overdraft_balance())
print(bank2.set_overdraft_balance())
print(bank2.get_overdraft_limit())
print(bank2.set_overdraft_limit())
