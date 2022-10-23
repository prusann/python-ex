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