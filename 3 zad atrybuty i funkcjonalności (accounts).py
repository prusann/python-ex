class Bank:
    def __init__(self,name,bank_accounts,bank_cards):
         self.name = name
         self.bank_accounts = bank_accounts
         self.bank_cards = bank_cards
    def get_bank_accounts(self):
        return "get_bank_accounts"
    def get_bank_cards(self):
        return 'get_bank_cards'
bank = Bank("x",12,"yyy")

print(bank.get_bank_accounts())
print(bank.get_bank_cards())