class Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print (f'Your opening account balance is {self.balance}')

    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print (f'{deposit} has been deposited. Your account balance is {self.balance}')
    
    def withdraw(self,withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw
            print (f'{withdraw} has been withdrawn. Your account balance is {self.balance}')
        else:
            print ('Sorry. Your account does not have sufficient balance')

        
