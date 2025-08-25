def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example input-output pair:
# Input: 3
# Output: 6

num = int(input("Enter a number to calculate its factorial: "))
output = factorial(num)
print(f"The factorial of {num} is: {output}")