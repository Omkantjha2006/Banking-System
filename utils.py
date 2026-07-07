def validate_pin(pin):
    """
    Validate that the PIN contains exactly 4 digits.
    """

    return pin.isdigit() and len(pin) == 4


def validate_amount(amount):
    """
    Validate that the amount is greater than zero.
    """

    return amount > 0


def format_currency(amount):
    """
    Format amount in Indian Rupees.
    """

    return f"₹{amount:.2f}"