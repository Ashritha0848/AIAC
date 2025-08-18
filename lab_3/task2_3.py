def sort_list_without_inbuilt(lst):
    """
    Sorts a list of numbers in ascending order without using inbuilt sort functions.

    Args:
        lst (list): The list of numbers to sort.

    Returns:
        list: The sorted list.
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Example usage:
input_list = [5, 2, 9, 1, 5, 6]
print("Input:", input_list)
print("Output:", sort_list_without_inbuilt(input_list.copy()))

