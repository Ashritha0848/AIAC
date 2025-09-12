def sum_even_odd(numbers):
    
    # Initialize sums for even and odd numbers
    even_sum = 0
    odd_sum = 0
    # Iterate through each number in the list
    for num in numbers:
        if num % 2 == 0:
            even_sum += num  # Add to even sum if number is even
        else:
            odd_sum += num   # Add to odd sum if number is odd
    return even_sum, odd_sum  # Return both sums as a tuple

# Example function call
result = sum_even_odd([1, 2, 3, 4, 5, 6])
print("Sum of even numbers:", result[0])
print("Sum of odd numbers:", result[1])

"""
    Calculates the sum of even and odd numbers in a given list.
    Args:
        numbers (list of int): A list of integers to be processed.
    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.
    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5, 6])
        (12, 9)
    """
