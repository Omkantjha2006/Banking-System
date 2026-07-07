from bank import Bank
from utils import validate_pin
from user_menu import user_menu
from admin_menu import admin_menu

bank = Bank()


while True:

    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Enter choice: ")

    # ---------------- Create Account ---------------- #

    if choice == "1":

        name = input("Enter Name: ")

        while True:

            pin = input("Create 4-digit PIN: ")

            if validate_pin(pin):
                break

            print("Invalid PIN! Enter exactly 4 digits.")

        account = bank.create_account(name, pin)

        print("\n====================================")
        print("Account Created Successfully!")
        print(f"Account Number : {account.account_number}")
        print("====================================")

    # ---------------- User Login ---------------- #

    elif choice == "2":

        user_menu(bank)

    # ---------------- Admin Login ---------------- #

    elif choice == "3":

        admin_menu(bank)

    # ---------------- Exit ---------------- #

    elif choice == "4":

        print("\nThank you for using Banking System.")
        break

    else:

        print("Invalid Choice.")