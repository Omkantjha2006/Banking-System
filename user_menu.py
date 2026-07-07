from utils import validate_amount, format_currency


def user_menu(bank):

    account_number = input("Account Number: ")
    pin = input("PIN: ")

    account = bank.login(account_number, pin)

    if not account:
        print("Invalid Account Number or PIN.")
        return

    while True:

        print("\n========================================")
        print(f"Welcome {account.name}")
        print("========================================")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Mini Statement")
        print("7. Account Details")
        print("8. Change PIN")
        print("9. Logout")

        option = input("\nEnter Choice: ")

        # ---------------- Deposit ---------------- #

        if option == "1":

            try:

                amount = float(input("Enter Amount: ₹"))

                if not validate_amount(amount):
                    print("Amount must be greater than zero.")
                    continue

                account.deposit(amount)
                bank.save_accounts()

                print(f"Deposit Successful. {format_currency(amount)} added.")

            except ValueError:
                print("Please enter a valid amount.")

        # ---------------- Withdraw ---------------- #

        elif option == "2":

            try:

                amount = float(input("Enter Amount: ₹"))

                if not validate_amount(amount):
                    print("Amount must be greater than zero.")
                    continue

                if account.withdraw(amount):

                    bank.save_accounts()

                    print(f"Withdrawal Successful. {format_currency(amount)} withdrawn.")

                else:
                    print("Insufficient Balance.")

            except ValueError:
                print("Please enter a valid amount.")

        # ---------------- Transfer ---------------- #

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
                print("Please enter a valid amount.")

        # ---------------- Balance ---------------- #

        elif option == "4":

            print("\n========== ACCOUNT BALANCE ==========")
            print(f"Current Balance : {format_currency(account.balance)}")

        # ---------------- Transaction History ---------------- #

        elif option == "5":

            print("\n========== TRANSACTION HISTORY ==========")

            if account.transactions:

                for transaction in account.transactions:
                    print(transaction)

            else:
                print("No transactions found.")

        # ---------------- Mini Statement ---------------- #

        elif option == "6":

            print("\n========== MINI ACCOUNT STATEMENT ==========")

            print(f"Account Number : {account.account_number}")
            print(f"Account Holder : {account.name}")
            print(f"Current Balance: {format_currency(account.balance)}")

            print("\nRecent Transactions")
            print("-" * 60)

            transactions = account.get_mini_statement()

            if transactions:

                for transaction in transactions:
                    print(transaction)

            else:
                print("No transactions available.")

        # ---------------- Account Details ---------------- #

        elif option == "7":

            print("\n========== ACCOUNT DETAILS ==========")

            print(f"Account Number : {account.account_number}")
            print(f"Account Holder : {account.name}")
            print(f"Balance        : {format_currency(account.balance)}")
            print(f"Transactions   : {len(account.transactions)}")

        # ---------------- Change PIN ---------------- #

        elif option == "8":

            old_pin = input("Enter Current PIN: ")

            new_pin = input("Enter New 4-digit PIN: ")

            confirm_pin = input("Confirm New PIN: ")

            if new_pin != confirm_pin:
                print("New PIN and Confirm PIN do not match.")

                continue

            success, message = bank.change_pin(

                account,

                old_pin,

                new_pin

            )

            print(message)

        # ---------------- Logout ---------------- #

        elif option == "9":

            print("Logged Out Successfully.")
            break

        else:
            print("Invalid Choice.")