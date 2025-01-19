import sys

class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        """  print(f"Deposited ${amount}. New balance is ${self.account_balance}.") """

    def withdraw(self, amount):
        if amount > self.account_balance:
            """ print(f"Account balance ${self.account_balance}")
            print("Insufficient funds.") """
            return False
        else:
            """ print(f"Withdrew ${amount}. New balance is ${self.account_balance - amount}.") """
            return True
        
    def display_balance(self):
        return print(f"Current Balance: ${self.account_balance:.2f}.")
        #return self.account_balance
    

