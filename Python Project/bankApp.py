#!/usr/bin/python3
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Your account balance is #{self.account_balance}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount
            print(f"You have successfully withdrawn #{amount}")
            print(f"New account balance is #{self.account_balance}")

    def get_balance(self):
            print(f"Account Balance: #{self.account_balance}")
    
account = Account("yusuf137", "yusuf137")
account.deposit(500)
account.withdraw(400)
account.get_balance()
