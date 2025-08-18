def sort_list_from_input():
    input_str = input("Enter numbers separated by spaces: ")
    try:
        numbers = list(map(float, input_str.strip().split()))
        sorted_numbers = sorted(numbers)
        print("Sorted list:", sorted_numbers)
    except ValueError:
        print("Please enter valid numbers.")

sort_list_from_input()

