class Account:
    def __init__(self, account_number, name, pin, balance=0, transactions=None):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = transactions if transactions else ["Account Created"]

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount:.2f}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount:.2f}")
            return True
        return False

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "pin": self.pin,
            "balance": self.balance,
            "transactions": self.transactions
        }