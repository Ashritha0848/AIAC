def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = 5  # You can change this value to compute factorial of another number
print(f"Factorial of {num} is {factorial(num)}")
