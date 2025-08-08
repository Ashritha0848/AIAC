def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    if choice == '1':
        result = num1 + num2
        op = '+'
    elif choice == '2':
        result = num1 - num2
        op = '-'
    elif choice == '3':
        result = num1 * num2
        op = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero.")
            return
        result = num1 / num2
        op = '/'

    print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    calculator()