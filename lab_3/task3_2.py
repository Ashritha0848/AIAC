def calculate_power_bill_custom_rates():
    """
    Calculates the total power bill based on the number of customers and their types.
    For each customer type, the rate per unit is asked from the user.
    """
    try:
        num_customers = int(input("Enter the number of customers: "))
        # Ask for rates for each type
        print("Enter the cost per unit for each customer type:")
        rate_residential = float(input("Residential: Rs. per unit = "))
        rate_commercial = float(input("Commercial: Rs. per unit = "))
        rate_industrial = float(input("Industrial: Rs. per unit = "))

        total_bill = 0
        for i in range(1, num_customers + 1):
            print(f"\nCustomer {i}:")
            print("Type of customer:")
            print("1. Residential")
            print("2. Commercial")
            print("3. Industrial")
            cust_type = int(input("Enter customer type (1/2/3): "))
            units = float(input("Enter number of units consumed: "))
            if cust_type == 1:
                rate = rate_residential
                cust_name = "Residential"
            elif cust_type == 2:
                rate = rate_commercial
                cust_name = "Commercial"
            elif cust_type == 3:
                rate = rate_industrial
                cust_name = "Industrial"
            else:
                print("Invalid customer type. Skipping this customer.")
                continue
            bill = units * rate
            print(f"{cust_name} customer bill: Rs. {bill:.2f}")
            total_bill += bill
        print(f"\nTotal power bill for all customers: Rs. {total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_power_bill_custom_rates()
