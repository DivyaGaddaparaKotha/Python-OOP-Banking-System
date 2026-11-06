
from bank import Bank

bank = Bank()

while True:
    print("\n===== PYTHON BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit()

    elif choice == "3":
        bank.withdraw()

    elif choice == "4":
        bank.check_balance()

    elif choice == "5":
        bank.transaction_history()

    elif choice == "6":
        print("Thank you for using Python Banking System!")
        break

    else:
        print("Invalid choice. Try again.")
