from bank import Bank
from utils import validate_pin
from admin import ADMIN_USERNAME, ADMIN_PASSWORD

bank = Bank()

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")

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

    elif choice == "3":

        username = input("Admin Username: ")
        password = input("Admin Password: ")

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            print("\nLogin Successful!")

            while True:

                print("\n========== ADMIN PANEL ==========")
                print("1. View All Accounts")
                print("2. Search Account")
                print("3. Delete Account")
                print("4. Total Accounts")
                print("5. Total Bank Balance")
                print("6. Logout")

                admin_choice = input("Enter choice: ")

                # ---------- View All Accounts ---------- #

                if admin_choice == "1":

                    accounts = bank.view_all_accounts()

                    print("\n================ ALL ACCOUNTS ================")

                    if not accounts:
                        print("No accounts found.")

                    else:
                        print(f"{'Account No.':<15}{'Name':<20}{'Balance'}")
                        print("-" * 50)

                        for account in accounts:
                            print(
                                f"{account.account_number:<15}"
                                f"{account.name:<20}"
                                f"₹{account.balance:.2f}"
                            )

                # ---------- Search Account ---------- #

                elif admin_choice == "2":

                    account_number = input("Enter Account Number: ")

                    account = bank.find_account(account_number)

                    if account:

                        print("\n========== ACCOUNT DETAILS ==========")
                        print(f"Account Number : {account.account_number}")
                        print(f"Name           : {account.name}")
                        print(f"Balance        : ₹{account.balance:.2f}")
                        print(f"Transactions   : {len(account.transactions)}")

                    else:
                        print("Account not found.")

                # ---------- Delete Account ---------- #

                elif admin_choice == "3":

                    account_number = input("Enter Account Number to Delete: ")

                    account = bank.find_account(account_number)

                    if account:

                        print("\n========== ACCOUNT DETAILS ==========")
                        print(f"Account Number : {account.account_number}")
                        print(f"Name           : {account.name}")
                        print(f"Balance        : ₹{account.balance:.2f}")

                        confirm = input("\nAre you sure you want to delete this account? (Y/N): ")

                        if confirm.upper() == "Y":

                            if bank.delete_account(account_number):
                                print("Account deleted successfully.")
                            else:
                                print("Failed to delete account.")

                        else:
                            print("Deletion cancelled.")

                    else:
                        print("Account not found.")

                # ---------- Total Accounts ---------- #

                elif admin_choice == "4":

                    total = bank.total_accounts()

                    print("\n========== TOTAL ACCOUNTS ==========")
                    print(f"Total Accounts: {total}")

                # ---------- Total Bank Balance ---------- #

                elif admin_choice == "5":

                    total_balance = bank.total_bank_balance()

                    print("\n========== TOTAL BANK BALANCE ==========")

                    print(f"Total Bank Balance: ₹{total_balance:.2f}")

                # ---------- Logout ---------- #

                elif admin_choice == "6":

                    print("Admin Logged Out.")
                    break

                else:
                    print("Invalid Choice.")
        else:
            print("Invalid Admin Credentials.")

    # ---------------- EXIT ---------------- #

    elif choice == "4":

        print("Thank you for using Banking System.")
        break

    else:
        print("Invalid Choice.")