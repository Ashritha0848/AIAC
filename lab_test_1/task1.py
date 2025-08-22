# Function to calculate factorial and Fibonacci series
def factorial_febo(n):
    # Calculate factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Generate Fibonacci series up to n terms
    fibo_series = []
    a, b = 0, 1
    for _ in range(n):
        fibo_series.append(a)
        a, b = b, a + b

    return factorial, fibo_series

# Take input from console
n = int(input("Enter a positive integer: "))

# Get factorial and Fibonacci series
fact, fibo = factorial_febo(n)

# Print results
print(f"Factorial of {n}: {fact}")
print(f"Fibonacci series up to {n} terms: {fibo}")
