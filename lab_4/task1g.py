def validate_indian_mobile_number():
    mobile_number = input("Enter an Indian mobile number: ")
    if len(mobile_number) == 10 and mobile_number.isdigit() and mobile_number[0] in ['6', '7', '8', '9']:
        print("Valid Indian mobile number.")
    else:
        print("Invalid Indian mobile number.")

validate_indian_mobile_number()