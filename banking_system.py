from bank import Bank
from utils import validate_pin

bank = Bank()

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    # ---------------- CREATE ACCOUNT ---------------- #

    if choice == "1":

        name = input("Enter Name: ")

        while True:
            pin = input("Create 4-digit PIN: ")

            if validate_pin(pin):
                break

            print("Invalid PIN! Enter exactly 4 digits.")

        account = bank.create_account(name, pin)

        print("\nAccount Created Successfully!")
        print(f"Your Account Number: {account.account_number}")

    # ---------------- LOGIN ---------------- #

    elif choice == "2":

        account_number = input("Account Number: ")
        pin = input("PIN: ")

        account = bank.login(account_number, pin)

        if account:

            while True:

                print(f"\nWelcome {account.name}")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer Money")
                print("4. Check Balance")
                print("5. Transaction History")
                print("6. Account Details")
                print("7. Logout")

                option = input("Choose: ")

                # ---------- Deposit ---------- #

                if option == "1":

                    try:
                        amount = float(input("Enter Amount: ₹"))

                        if amount <= 0:
                            print("Amount must be greater than zero.")
                            continue

                        account.deposit(amount)
                        bank.save_accounts()

                        print("Deposit Successful.")

                    except ValueError:
                        print("Invalid amount.")

                # ---------- Withdraw ---------- #

                elif option == "2":

                    try:
                        amount = float(input("Enter Amount: ₹"))

                        if amount <= 0:
                            print("Amount must be greater than zero.")
                            continue

                        if account.withdraw(amount):
                            bank.save_accounts()
                            print("Withdrawal Successful.")
                        else:
                            print("Insufficient Balance.")

                    except ValueError:
                        print("Invalid amount.")

                # ---------- Transfer ---------- #

                elif option == "3":

                    receiver = input("Receiver Account Number: ")

                    try:
                        amount = float(input("Enter Amount: ₹"))

                        success, message = bank.transfer_money(
                            account,
                            receiver,
                            amount
                        )

                        print(message)

                    except ValueError:
                        print("Invalid amount.")

                # ---------- Balance ---------- #

                elif option == "4":

                    print(f"\nCurrent Balance : ₹{account.balance:.2f}")

                # ---------- Transaction History ---------- #

                elif option == "5":

                    print("\n===== TRANSACTION HISTORY =====")

                    if account.transactions:

                        for transaction in account.transactions:
                            print(transaction)

                    else:
                        print("No transactions found.")

                # ---------- Account Details ---------- #

                elif option == "6":

                    print("\n===== ACCOUNT DETAILS =====")

                    print(f"Account Number : {account.account_number}")
                    print(f"Name           : {account.name}")
                    print(f"Balance        : ₹{account.balance:.2f}")

                # ---------- Logout ---------- #

                elif option == "7":

                    print("Logged Out Successfully.")
                    break

                else:
                    print("Invalid Option.")

        else:
            print("Invalid Account Number or PIN.")

    # ---------------- EXIT ---------------- #

    elif choice == "3":

        print("Thank you for using Banking System.")
        break

    else:
        print("Invalid Choice.")