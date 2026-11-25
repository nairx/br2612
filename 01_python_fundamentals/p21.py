class Account:
    def __init__(self,accnum,name,balance):
        self.accnum = accnum
        self.name = name
        self.balance = balance 
    def view_balance(self):
        print(self.balance)

customer = Account(1001,"John",1000)
customer.view_balance()