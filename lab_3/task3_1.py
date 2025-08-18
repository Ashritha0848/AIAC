def calculate_power_bill():
    """
    Calculates the total power bill based on the number of customers and their types.
    Customer types:
        1. Residential: Rs. 5 per unit
        2. Commercial: Rs. 8 per unit
        3. Industrial: Rs. 10 per unit
    """
    try:
        num_customers = int(input("Enter the number of customers: "))
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
                rate = 5
                cust_name = "Residential"
            elif cust_type == 2:
                rate = 8
                cust_name = "Commercial"
            elif cust_type == 3:
                rate = 10
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

# Example usage:
if __name__ == "__main__":
    calculate_power_bill()
