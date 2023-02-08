class BankAccount:
    
    # instances = []
    accounts = []
    
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        # Both work 
        # self.__class__.instances.append(self)
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    def display_account_info(self):
        # your code here
        print(f"Balances: ${self.balance}")
        return self
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("Insufficient Funds to add interest")
        return self
    
    @classmethod
    def print_All_Info(cls):
        
        # My idea
        # for x in BankAccount.instances:
        #     x.display_account_info()
        
        for account in cls.accounts:
            account.display_account_info()
            
            
john = BankAccount(.03,100)
jane = BankAccount(.02,1000)

john.deposit(50)
john.deposit(100)
john.deposit(100)
john.withdraw(1)
# john.yield_interest().display_account_info()
john.yield_interest()

jane.deposit(50)
jane.deposit(10000)
jane.withdraw(30)
jane.withdraw(500)
jane.withdraw(300)
jane.withdraw(50)
# jane.yield_interest().display_account_info()
jane.yield_interest()

BankAccount.print_All_Info()
