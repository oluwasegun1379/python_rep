#!/usr/bin/python3
class Bank:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.account_balance = 0
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Account balance: {self.account_balance}")
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds")
        else:
            self.account_balance -= amount
            print(f"You have successfully withdrawn: {amount}")
            print(f"Account balance: {self.account_balance}")
    def get_balance(self):
        print(f"Acount balance: {self.account_balance}")
bank = Bank("John", "John137")
bank.deposit(500)
bank.get_balance()

