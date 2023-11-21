class BankAccount:
    def __init__(self, interest_rate, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance * self.interest_rate
            self.balance += interest_earned
            print(f"Interest earned: ${interest_earned}. New balance: ${self.balance}")
        else:
            print("No interest earned. Balance is not positive.")
        return self
    
account1 = BankAccount(0.01, 0)
account2 = BankAccount(0.01, 0)
print(account1)
print(account2)
account1.deposit(1000).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
account2.deposit(1000).deposit(1000).withdraw(100).withdraw(500).withdraw(100).withdraw(100).yield_interest().display_account_info()