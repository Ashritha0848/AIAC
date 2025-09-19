def is_valid_email(email):
    if email.count('@') != 1:
        return False
    if '.' not in email:
        return False
    special_chars = {'@', '.'}
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    return True

if __name__ == "__main__":
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")
# Manual Test Cases

# Test Case 1
# Input: "abc@gmail.com"
# Expected Output: Valid email address.
# Reason: One '@', contains '.', does not start/end with '.' or '@'.

# Test Case 2
# Input: "abc@@mail.com"
# Expected Output: Invalid email address.
# Reason: Contains more than one '@'.

