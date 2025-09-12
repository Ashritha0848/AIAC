def sum_even(numbers):
    
    return sum(num for num in numbers if num % 2 == 0)
def sum_odd(numbers):
    return sum(num for num in numbers if num % 2 != 0)
nums = [1, 2, 3, 4, 5, 6]
even_sum = sum_even(nums)
odd_sum = sum_odd(nums)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

"""
    This module provides functions to calculate the sum of even and odd numbers in a list.

    Functions:
        sum_even(numbers): Returns the sum of all even numbers in the input list.
        sum_odd(numbers): Returns the sum of all odd numbers in the input list.

    Example usage:
        even_sum = sum_even(nums)  # Returns 12
        odd_sum = sum_odd(nums)    # Returns 9
    """
