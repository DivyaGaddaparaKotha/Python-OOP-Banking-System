
from abc import ABC, abstractmethod
from datetime import datetime


# Abstraction
class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Inheritance
class Account(BankAccount):

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.__balance = balance  # Encapsulation
        self.transactions = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
            return

        self.__balance += amount
        self.transactions.append(
            f"Deposited Rs.{amount} - {datetime.now()}"
        )
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            self.transactions.append(
                f"Withdrawn Rs.{amount} - {datetime.now()}"
            )
            print("Withdrawal successful!")

    def display(self):
        print("\nAccount Number:", self.account_number)
        print("Account Holder:", self.name)
        print("Balance: Rs.", self.__balance)

    def show_transactions(self):
        print("\nTransaction History:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


# Polymorphism through method overriding
class SavingsAccount(Account):

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            super().withdraw(amount)
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Enter a valid amount.")
