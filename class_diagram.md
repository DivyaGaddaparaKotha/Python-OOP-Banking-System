
# Banking System - Class Diagram

## Classes

### BankAccount (Abstract Class)
- deposit()
- withdraw()

### Account (Inherits BankAccount)
- account_number
- name
- __balance
- transactions
- display()
- show_transactions()

### SavingsAccount (Inherits Account)
- withdraw()

### Bank
- accounts
- create_account()
- get_account()
- deposit()
- withdraw()
- check_balance()
- transaction_history()

## Relationships

1. BankAccount is the parent abstract class.
2. Account inherits BankAccount.
3. SavingsAccount inherits Account.
4. Bank manages multiple SavingsAccount objects.
