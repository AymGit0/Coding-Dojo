class BankAccount:
    all_accounts=[]

    def __init__(self, int_rate, balance=0): 
        self.balance = balance
        self.rate= int_rate
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-= amount
            return self.balance
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self.balance
    def display_account_info(self):
        print(f"Balance: {self.balance}$")
    def yield_interest(self):
        if self.balance>0:
            self.balance= self.balance*(1+ self.rate)
            return self.balance
    @classmethod
    def all_infos(cls):
        for i in range (0, len(cls.all_accounts)):
            print (f"account {i+1}'s balance : {cls.all_accounts[i].balance} ")


class User:
    def __init__(self, name, email):
        self.accounts=[]
        self.name = name
        self.email = email

    def make_account(self):
        self.accounts.append(BankAccount(0.02))
        

    def make_deposit(self, amount, account):
        self.accounts[account].deposit(amount)
    
    def make_withdrawal(self, amount , account):
        self.accounts[account].withdraw(amount)
    
    def display_user_balance(self,account):
        self.accounts[account].display_account_info()
    
    def transfer_money(self,account, amount, other_user,other_index):
        self.accounts[account].withdraw(amount)
        other_user.accounts[other_index].deposit(amount)

John = User ("John", "email")
John.make_account()
John.make_account()
John.make_deposit(10000,0)
John.make_deposit(5000,1)
John.display_user_balance(0)
John.display_user_balance(1)


Wei = User ("Wei","email")
Wei.make_account()
John.transfer_money(0,400,Wei,0)
John.display_user_balance(0)
Wei.display_user_balance(0)





