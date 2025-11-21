import re

"""
task2.py

Simple password validator:
- At least 8 characters
- At least one digit
- At least one uppercase letter
- At least one special character from the set: ! @ # $
Takes input from the console and prints "Password is valid" or "invalid password".
"""


def validate_password(password: str) -> bool:
    """
    Validate a password string.

    Returns True if the password meets all criteria:
      - length >= 8
      - contains at least one digit
      - contains at least one uppercase letter
      - contains at least one special character from ! @ # $

    Returns False otherwise. Does not raise exceptions for invalid input.
    """
    if not isinstance(password, str):
        # Non-string inputs are considered invalid
        return False

    # Check length with a simple conditional
    if len(password) < 8:
        return False

    # Use regular expressions for the other checks
    if not re.search(r"\d", password):           # at least one digit
        return False
    if not re.search(r"[A-Z]", password):        # at least one uppercase letter
        return False
    if not re.search(r"[!@#$]", password):       # at least one of the specified special chars
        return False

    # All checks passed
    return True


if __name__ == "__main__":
    # Read password from console
    pwd = input("Enter password: ")

    # Validate and print result. If invalid, print the required message but do not raise an error.
    if validate_password(pwd):
        print("Password is valid")
    else:
        print("invalid password")