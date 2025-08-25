# One-shot prompt: For example, if input is 5, output should be 120 (since 5! = 5*4*3*2*1 = 120).

def factorial(n):
    """
    Returns the factorial of n.
    If n is negative, returns an error message.
    Handles 0! correctly (returns 1).
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    output = factorial(num)
    print(f"Factorial of {num} is: {output}")

# Example input-output:
# Input: 5
# Output: Factorial of 5 is: 120
