class BankCard:
    def __init__(self,owner,number,provider):
         self.owner = owner
         self.number = number
         self.provider = provider
    def get_owner(self):
        return "get_owner"
    def get_number(self):
        return 'get_number'
    def get_provider(self):
        return 'get_provider'
bank = BankCard("x",1202,"y")
print(bank.get_number())
print(bank.get_owner())
print(bank.get_provider())

class CreditCard(BankCard):
    def __init__(self,balance, payments_history):
         self.balance = balance
         self.payments_history = payments_history
    def get_balance(self):
        return "get_balance"
    def set_balance(self):
        return 'set_balance'
    def get_payments_history(self):
        return 'get_payments_history'      
bank1 = CreditCard(7,8)
print(bank1.get_balance())
print(bank1.set_balance())
print(bank1.get_payments_history())         