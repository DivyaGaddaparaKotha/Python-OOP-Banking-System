from account import SavingsAccount

class Bank:

    def __init__(self):
        self.accounts = {}

    def create_account(self):
        number = input("Enter account number: ")

        if number in self.accounts:
            print("Account already exists!")
            return

        name = input("Enter account holder name: ")

        account = SavingsAccount(number, name)
        self.accounts[number] = account

        print("Account created successfully!")

    def get_account(self):
        number = input("Enter account number: ")
        account = self.accounts.get(number)

        if account is None:
            print("Account not found!")

        return account

    def deposit(self):
        account = self.get_account()
        if account:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

    def withdraw(self):
        account = self.get_account()
        if account:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

    def check_balance(self):
        account = self.get_account()
        if account:
            account.display()

    def transaction_history(self):
        account = self.get_account()
        if account:
            account.show_transactions()
