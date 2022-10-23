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


class PremiumBankAccount(BankAccount):
    def __init__(self,financial_manager):
         self.financial_manager = financial_manager
    def get_financial_manager(self):
        return "get_financial_manager"
    def set_financial_manager(self):
        return "set_financial_manager"
bank1 = PremiumBankAccount("x")
print(bank1.get_financial_manager())
print(bank1.set_financial_manager())