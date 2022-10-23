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