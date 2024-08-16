class Bank:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Customer:
    def __init__(self, customerID, name):
        self.id = customerID
        self.name = name

    @property
    def name(self):
        return self.name

class Account:
    def __init__(self, accountNumber, money, Bank, customer):
        self.Account = accountNumber
        self.Money = money
        self.TheBank = Bank
        self.Owner = customer

    def transfer(self, account_obj, money_to_transfer):
        if account_obj.Money >= money_to_transfer:
            account_obj.Money += money_to_transfer
            self.Money -= money_to_transfer
        else:
            raise ValueError('Not enough money')

    def balance(self):
        print("account balance is : {}$".format(self.Money))

    def __str__(self):
        return """acc_id: {} customer: {} balance: {} Bank: {} """.format(self.Account, self.Owner.name, self.Money, self.TheBank.name)
    
class BankCustomer:
    def __init__(self, Bank, customer):
        self.bank = Bank
        self.customer = customer