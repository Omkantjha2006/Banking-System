from datetime import datetime


class Account:

    def __init__(
            self,
            account_number,
            name,
            pin,
            balance=0.0,
            transactions=None
    ):

        self.account_number = str(account_number)
        self.name = name
        self.pin = pin
        self.balance = balance

        self.transactions = transactions if transactions else []

        # Add first transaction only for newly created accounts
        if not transactions:
            self.add_transaction("Account Created")

    # ---------------------------------------
    # Add Transaction with Date & Time
    # ---------------------------------------

    def add_transaction(self, message):

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        self.transactions.append(
            f"[{timestamp}] {message}"
        )

    # ---------------------------------------
    # Deposit
    # ---------------------------------------

    def deposit(self, amount):

        self.balance += amount

        self.add_transaction(
            f"Deposited ₹{amount:.2f}"
        )

    # ---------------------------------------
    # Withdraw
    # ---------------------------------------

    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            self.add_transaction(
                f"Withdrawn ₹{amount:.2f}"
            )

            return True

        return False

    # ---------------------------------------
    # Mini Statement
    # ---------------------------------------

    def get_mini_statement(self, limit=5):

        return self.transactions[-limit:]

    # ---------------------------------------
    # Convert Object to Dictionary
    # ---------------------------------------

    def to_dict(self):

        return {
            "account_number": self.account_number,
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }

    # ---------------------------------------
    # Create Object from Dictionary
    # ---------------------------------------

    @classmethod
    def from_dict(cls, data):

        return cls(
            account_number=data["account_number"],
            name=data["name"],
            pin=data["pin"],
            balance=data.get("balance", 0.0),
            transactions=data.get("transactions", [])
        )