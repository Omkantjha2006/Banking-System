import json
import os

from account import Account


class Bank:

    def __init__(self):

        self.file_path = "data/accounts.json"
        self.accounts = []

        self.load_accounts()

    # ----------------------------------
    # Load Accounts
    # ----------------------------------

    def load_accounts(self):

        if not os.path.exists(self.file_path):

            os.makedirs("data", exist_ok=True)

            with open(self.file_path, "w") as file:
                json.dump([], file, indent=4)

        with open(self.file_path, "r") as file:

            try:

                data = json.load(file)

                self.accounts = [
                    Account.from_dict(account)
                    for account in data
                ]

            except json.JSONDecodeError:

                self.accounts = []

    # ----------------------------------
    # Save Accounts
    # ----------------------------------

    def save_accounts(self):

        with open(self.file_path, "w") as file:

            json.dump(

                [account.to_dict() for account in self.accounts],

                file,

                indent=4

            )

    # ----------------------------------
    # Generate Account Number
    # ----------------------------------

    def generate_account_number(self):

        if not self.accounts:
            return "100001"

        last_number = max(

            int(account.account_number)

            for account in self.accounts

        )

        return str(last_number + 1)

    # ----------------------------------
    # Create Account
    # ----------------------------------

    def create_account(self, name, pin):

        account_number = self.generate_account_number()

        account = Account(

            account_number,

            name,

            pin

        )

        self.accounts.append(account)

        self.save_accounts()

        return account

    # ----------------------------------
    # Login
    # ----------------------------------

    def login(self, account_number, pin):

        for account in self.accounts:

            if (

                account.account_number == account_number

                and

                account.pin == pin

            ):

                return account

        return None

    # ----------------------------------
    # Find Account
    # ----------------------------------

    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:

                return account

        return None

    # ----------------------------------
    # Transfer Money
    # ----------------------------------

    def transfer_money(

            self,

            sender,

            receiver_account_number,

            amount

    ):

        receiver = self.find_account(receiver_account_number)

        if receiver is None:

            return False, "Receiver account not found."

        if sender.account_number == receiver.account_number:

            return False, "Cannot transfer to your own account."

        if amount <= 0:

            return False, "Amount must be greater than zero."

        if sender.balance < amount:

            return False, "Insufficient balance."

        sender.balance -= amount

        receiver.balance += amount

        sender.add_transaction(

            f"Transferred ₹{amount:.2f} to {receiver.account_number}"

        )

        receiver.add_transaction(

            f"Received ₹{amount:.2f} from {sender.account_number}"

        )

        self.save_accounts()

        return True, "Transfer Successful."

    # ----------------------------------
    # View All Accounts
    # ----------------------------------

    def view_all_accounts(self):

        return self.accounts

    # ----------------------------------
    # Delete Account
    # ----------------------------------

    def delete_account(self, account_number):

        account = self.find_account(account_number)

        if account:

            self.accounts.remove(account)

            self.save_accounts()

            return True

        return False

    # ----------------------------------
    # Total Accounts
    # ----------------------------------

    def total_accounts(self):

        return len(self.accounts)

    # ----------------------------------
    # Total Bank Balance
    # ----------------------------------

    def total_bank_balance(self):

        total = 0

        for account in self.accounts:

            total += account.balance

        return total

    # ----------------------------------
    # Change PIN
    # ----------------------------------

    def change_pin(self, account, old_pin, new_pin):

        # Verify current PIN
        if account.pin != old_pin:
            return False, "Incorrect Current PIN."

        # PIN must contain exactly 4 digits
        if not new_pin.isdigit() or len(new_pin) != 4:
            return False, "PIN must be exactly 4 digits."

        # New PIN must be different
        if old_pin == new_pin:
            return False, "New PIN cannot be the same as the current PIN."

        account.pin = new_pin

        account.add_transaction("PIN Changed")

        self.save_accounts()

        return True, "PIN Changed Successfully."