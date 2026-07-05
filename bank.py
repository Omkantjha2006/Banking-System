import json
import os
from account import Account


class Bank:

    def transfer_money(self, sender, receiver_account_number, amount):

        receiver = self.find_account(receiver_account_number)

        if receiver is None:
            return False, "Receiver account not found."

        if sender.account_number == receiver.account_number:
            return False, "You cannot transfer money to your own account."

        if amount <= 0:
            return False, "Invalid amount."

        if sender.balance < amount:
            return False, "Insufficient balance."

        sender.balance -= amount
        receiver.balance += amount

        sender.transactions.append(
            f"Transferred ₹{amount:.2f} to {receiver.account_number}"
        )

        receiver.transactions.append(
            f"Received ₹{amount:.2f} from {sender.account_number}"
        )

        self.save_accounts()

        return True, "Transfer successful."

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def generate_account_number(self):
        if not self.accounts:
            return "100001"

        last_account = max(
            int(account.account_number)
            for account in self.accounts
        )

        return str(last_account + 1)

    def __init__(self):
        self.accounts = []
        self.file_path = "data/accounts.json"
        self.load_accounts()

    def load_accounts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                try:
                    data = json.load(file)
                    for item in data:
                        account = Account(
                            item["account_number"],
                            item["name"],
                            item["pin"],
                            item["balance"],
                            item.get("transactions", [])
                        )
                        self.accounts.append(account)
                except json.JSONDecodeError:
                    pass

    def save_accounts(self):
        with open(self.file_path, "w") as file:
            json.dump(
                [account.to_dict() for account in self.accounts],
                file,
                indent=4
            )

    def create_account(self, name, pin):
        account_number = self.generate_account_number()

        account = Account(account_number, name, pin)

        self.accounts.append(account)
        self.save_accounts()

        return account

    def login(self, account_number, pin):
        for account in self.accounts:
            if (
                account.account_number == account_number
                and account.pin == pin
            ):
                return account
        return None