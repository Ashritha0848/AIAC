def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = 10
print(f"Factorial of {num} is {factorial(num)}")

