def calculate_power_bill_variable_slabs():
    """
    Calculates the total power bill based on the number of customers and their types.
    For each customer type, the user is asked to enter the per unit cost for different consumption ranges (slabs).
    """
    try:
        num_customers = int(input("Enter the number of customers: "))

        # Define slabs for each customer type
        customer_types = {
            1: "Residential",
            2: "Commercial",
            3: "Industrial"
        }

        # Ask for number of slabs for each type and their ranges and rates
        slab_info = {}
        for ctype, cname in customer_types.items():
            print(f"\nEnter slab details for {cname} customers:")
            num_slabs = int(input(f"How many slabs for {cname}? "))
            slabs = []
            last_upper = 0
            for i in range(num_slabs):
                if i < num_slabs - 1:
                    upper = float(input(f"  Enter upper limit for slab {i+1} (units): "))
                    rate = float(input(f"  Enter rate for units up to {upper} (Rs. per unit): "))
                    slabs.append((upper, rate))
                    last_upper = upper
                else:
                    # Last slab: no upper limit
                    rate = float(input(f"  Enter rate for units above {last_upper} (Rs. per unit): "))
                    slabs.append((float('inf'), rate))
            slab_info[ctype] = slabs

        total_bill = 0
        for i in range(1, num_customers + 1):
            print(f"\nCustomer {i}:")
            print("Type of customer:")
            for ctype, cname in customer_types.items():
                print(f"{ctype}. {cname}")
            cust_type = int(input("Enter customer type (1/2/3): "))
            if cust_type not in customer_types:
                print("Invalid customer type. Skipping this customer.")
                continue
            units = float(input("Enter number of units consumed: "))
            slabs = slab_info[cust_type]
            bill = 0
            prev_upper = 0
            remaining_units = units
            for upper, rate in slabs:
                if remaining_units <= 0:
                    break

                slab_units = min(remaining_units, upper - prev_upper)
                bill += slab_units * rate
                remaining_units -= slab_units
                prev_upper = upper
            print(f"{customer_types[cust_type]} customer bill: Rs. {bill:.2f}")
            total_bill += bill
        print(f"\nTotal power bill for all customers: Rs. {total_bill:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_power_bill_variable_slabs()
