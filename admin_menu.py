from admin import ADMIN_USERNAME, ADMIN_PASSWORD


def admin_menu(bank):

    username = input("Admin Username: ")
    password = input("Admin Password: ")

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        print("Invalid Admin Credentials.")
        return

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

                confirm = input(
                    "\nAre you sure you want to delete this account? (Y/N): "
                )

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
            print(f"Total Accounts : {total}")

        # ---------- Total Bank Balance ---------- #

        elif admin_choice == "5":

            total_balance = bank.total_bank_balance()

            print("\n====== TOTAL BANK BALANCE ======")
            print(f"Total Bank Balance : ₹{total_balance:.2f}")

        # ---------- Logout ---------- #

        elif admin_choice == "6":

            print("Admin Logged Out Successfully.")
            break

        else:
            print("Invalid Choice.")