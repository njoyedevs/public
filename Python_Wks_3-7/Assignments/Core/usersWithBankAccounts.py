class BankAccount:
    
    accounts = []
    
    # don't forget to add some default values for these parameters!
    def __init__(self, account_name, int_rate, balance=0): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.account_name = account_name
        self.int_rate = int_rate
        self.balance = balance
        # Both work 
        BankAccount.accounts.append(self)
        
    def deposit(self, amount):
        # your code here
        self.balance += amount
        
    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("\n\nInsufficient funds: Charging a $5 fee\n\n")
            self.balance -= 5
            
    def display_account_info(self):
        # your code here
        print(f"\nAccount Name: {self.account_name}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.int_rate}\n")
        return self
    
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("\n\nInsufficient Funds to add interest\n\n")
        return self
    
    @classmethod
    def print_All_Info(cls):
        
        for account in cls.accounts:
            account.display_account_info()
            
            
class User:
    
    user_accounts = {}
    
    def __init__(self, name, email, account_nm):
        
        self.name = name
        self.email = email
        self.account_nm = account_nm
        self.account = BankAccount(account_name=self.account_nm, int_rate=0.02, balance=0)
        
        self.accounts = {}
        
        if f"{self.name}:{self.account_nm}" not in self.user_accounts.keys() and f"{self.name}:{self.account_nm}" not in self.user_accounts.keys():
            self.user_accounts[f"{self.name}:{self.account_nm}"] = self.account
            self.accounts[f"{self.name}:{self.account_nm}"] = self.account
        else:
            print("Error: Account Name Already Taken, Try Another Name")
    
    # other methods
    
    def make_deposit(self, amount):
        # your code here
        # print(self.accounts)
        new_list = list(self.accounts)
        # print(new_list)
        self.dep_account_num= int(input(f"Select from the accounts (Example: 1,2, or 3): {new_list}")) - 1
        print(self.dep_account_num)
        print(self.accounts)
        print(new_list[self.dep_account_num])
        print(f"Account Number: {self.accounts[new_list[self.dep_account_num]]}")
        self.accounts[new_list[self.dep_account_num]].deposit(amount)
        self.accounts[new_list[self.dep_account_num]].display_account_info()

    def make_withdrawl(self, amount):
        # your code here
        # print(self.user_accounts)
        new_list = list(self.accounts)
        # print(new_list)
        self.with_account_num= int(input(f"Select from the accounts (Example: 1,2, or 3): {new_list}")) - 1
        print(self.with_account_num)
        print(self.accounts)
        print(new_list[self.with_account_num])
        print(f"Account Number: {self.accounts[new_list[self.with_account_num]]}")
        self.accounts[new_list[self.with_account_num]].withdraw(amount)
        self.accounts[new_list[self.with_account_num]].display_account_info()
        
    def display_user_balance(self):
        # print(self.user_accounts)
        new_list = list(self.accounts)
        # print(new_list)
        self.disp_account_num= int(input(f"Select from the accounts (Example: 1,2, or 3): {new_list}")) - 1
        print(self.disp_account_num)
        print(self.accounts)
        print(f"{new_list[self.disp_account_num]}")
        # print(self.user_accounts[new_list[self.account_num]])
        self.accounts[new_list[self.disp_account_num]].display_account_info()
        
    def create_account(self,new_account_nm):
        
        self.new_account_nm = new_account_nm
        self.new_account = BankAccount(account_name=self.new_account_nm, int_rate=0.02, balance=0)
        self.accounts[f"{self.name}:{self.new_account_nm}"] = self.new_account
        print(f"User Name: {self.name}")
        print(f"User ID: {self.new_account_nm}")
        print(f"Account Number: {self.accounts[f'{self.name}:{self.new_account_nm}']}")
        self.accounts[f"{self.name}:{self.new_account_nm}"].display_account_info()
        
    def transfer_money(self,amount, to_user):
        
        # Select which account self want to withdrawl
        self_list = list(self.accounts)
        # print(new_list)
        self.transf_account_num= int(input(f"Select from the accounts (Example: 1,2, or 3): {self_list}")) - 1
        print(self.transf_account_num)
        print(f"From Account Name: {self_list[self.transf_account_num]}")
        print(f"From Account Number: {self.accounts[f'{self_list[self.transf_account_num]}']}")
        self.accounts[f"{self_list[self.transf_account_num]}"].withdraw(amount)
        self.accounts[f"{self_list[self.transf_account_num]}"].display_account_info()
        
        # Select which account to_user wants to deposit
        to_list = list(to_user.accounts)
        # print(new_list)
        to_user.transf_account_num= int(input(f"\n\nSelect from the accounts (Example: 1,2, or 3): {to_list}")) - 1
        print(to_user.transf_account_num)
        print(f"To Account Name: {to_list[to_user.transf_account_num]}")
        print(f"To Account Number: {to_user.accounts[f'{to_list[to_user.transf_account_num]}']}")
        to_user.accounts[f"{to_list[to_user.transf_account_num]}"].deposit(amount)
        to_user.accounts[f"{to_list[to_user.transf_account_num]}"].display_account_info()
        

user_1 = User("John","johndoe@gmail.com","First_Account")
# user_1.display_user_balance()

user_1.create_account("Second_Account")
# user_1 = User("John","johndoe@gmail.com","Second_Account")
# user_1.display_user_balance()

user_1.make_deposit(100)
user_1.make_deposit(100)
# user_1.make_withdrawl(100)
# user_1.make_withdrawl(100)

user_2 = User("Jane","janedoe@gmail.com","Janes_Account")

user_2.make_deposit(100)
# user_2.make_withdrawl(100)
# user_2.display_user_balance()

user_2.transfer_money(50,user_1)
