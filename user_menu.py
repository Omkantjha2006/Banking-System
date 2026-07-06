def user_menu(bank):

    account_number = input("Account Number: ")
    pin = input("PIN: ")

    account = bank.login(account_number, pin)

    if not account:
        print("Invalid Account Number or PIN.")
        return

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

        # ---------- Transfer Money ---------- #

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

        # ---------- Check Balance ---------- #

        elif option == "4":

            print("\n========== BALANCE ==========")
            print(f"Current Balance : ₹{account.balance:.2f}")

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

            print("\n========== ACCOUNT DETAILS ==========")
            print(f"Account Number : {account.account_number}")
            print(f"Name           : {account.name}")
            print(f"Balance        : ₹{account.balance:.2f}")
            print(f"Transactions   : {len(account.transactions)}")

        # ---------- Logout ---------- #

        elif option == "7":

            print("Logged Out Successfully.")
            break

        else:
            print("Invalid Choice.")