def validate_indian_mobile_number(number):
    """
    Validates if the given number is a valid Indian mobile number.
    Criteria:
    - Starts with 6, 7, 8, or 9
    - Exactly 10 digits
    """
    if len(number) == 10 and number.isdigit() and number[0] in {'6', '7', '8', '9'}:
        return True
    return False

if __name__ == "__main__":
    mobile_number = input("Enter an Indian mobile number: ")
    if validate_indian_mobile_number(mobile_number):
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")
