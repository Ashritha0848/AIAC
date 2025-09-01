def sum_to_n(n):
    """Calculate the sum of the first n natural numbers using a for loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Take input from the console
try:
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        result = sum_to_n(n)
        print(f"The sum of the first {n} numbers is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")

