from admin import (
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
    ADMIN_NAME,
    ADMIN_ROLE
)

from utils import format_currency


def admin_menu(bank):

    print("\n========== ADMIN LOGIN ==========")

    username = input("Username : ")
    password = input("Password : ")

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        print("Invalid Admin Credentials.")
        return

    print("\n========================================")
    print(f"Welcome {ADMIN_NAME}")
    print(f"Role : {ADMIN_ROLE}")
    print("========================================")

    while True:

        print("\n========== ADMIN PANEL ==========")
        print("1. View All Accounts")
        print("2. Search Account")
        print("3. Delete Account")
        print("4. Total Accounts")
        print("5. Total Bank Balance")
        print("6. Logout")

        choice = input("\nEnter Choice: ")

        # -----------------------------------
        # View All Accounts
        # -----------------------------------

        if choice == "1":

            accounts = bank.view_all_accounts()

            print("\n================ ALL ACCOUNTS ================")

            if not accounts:
                print("No accounts found.")
                continue

            print(f"{'Account No.':<15}{'Name':<20}{'Balance'}")
            print("-" * 50)

            for account in accounts:

                print(
                    f"{account.account_number:<15}"
                    f"{account.name:<20}"
                    f"{format_currency(account.balance)}"
                )

        # -----------------------------------
        # Search Account
        # -----------------------------------

        elif choice == "2":

            account_number = input("Enter Account Number: ")

            account = bank.find_account(account_number)

            if account:

                print("\n========== ACCOUNT DETAILS ==========")
                print(f"Account Number : {account.account_number}")
                print(f"Account Holder : {account.name}")
                print(f"Balance        : {format_currency(account.balance)}")
                print(f"Transactions   : {len(account.transactions)}")

            else:
                print("Account not found.")

        # -----------------------------------
        # Delete Account
        # -----------------------------------

        elif choice == "3":

            account_number = input("Enter Account Number: ")

            account = bank.find_account(account_number)

            if not account:
                print("Account not found.")
                continue

            print("\n========== ACCOUNT DETAILS ==========")
            print(f"Account Number : {account.account_number}")
            print(f"Account Holder : {account.name}")
            print(f"Balance        : {format_currency(account.balance)}")

            confirm = input(
                "\nDelete this account? (Y/N): "
            )

            if confirm.upper() == "Y":

                if bank.delete_account(account_number):
                    print("Account deleted successfully.")

                else:
                    print("Failed to delete account.")

            else:
                print("Deletion cancelled.")

        # -----------------------------------
        # Total Accounts
        # -----------------------------------

        elif choice == "4":

            total = bank.total_accounts()

            print("\n========== TOTAL ACCOUNTS ==========")
            print(f"Total Accounts : {total}")

        # -----------------------------------
        # Total Bank Balance
        # -----------------------------------

        elif choice == "5":

            total_balance = bank.total_bank_balance()

            print("\n====== TOTAL BANK BALANCE ======")
            print(
                f"Total Balance : {format_currency(total_balance)}"
            )

        # -----------------------------------
        # Logout
        # -----------------------------------

        elif choice == "6":

            print("Admin Logged Out Successfully.")
            break

        else:
            print("Invalid Choice.")