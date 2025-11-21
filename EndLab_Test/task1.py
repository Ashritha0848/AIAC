
"""


This script demonstrates a binary search implementation that:
- Sorts the input list before searching.
- Preserves original indices so the returned index corresponds to the original (unsorted) list.
- Uses an iterative binary search for efficiency.
- Reads input from the console.

Input:
1) A line containing numbers separated by spaces (e.g. "3 1 4 5 9")
2) A line containing a single number as the target (e.g. "5")

Output:
A message indicating whether the target was found and its index in the original list,
or -1 if not found.
"""

from typing import List, Union

Number = Union[int, float]


def binary_search(arr: List[Number], target: Number) -> int:
    """
    Perform binary search on a sorted list of (value, original_index) pairs.

    Important behavior:
    - The function expects the input `arr` to be a list of tuples where each tuple is
      (value, original_index) and `arr` is already sorted by value.
    - If the target is found, the function returns the original index (original_index)
      of the first matching pair encountered.
    - If the target is not found, the function returns -1.

    Args:
        arr (List[Tuple[Number, int]]): Sorted list of (value, original_index) pairs.
        target (Number): The value to search for.

    Returns:
        int: Index of target in the original (unsorted) list, or -1 if not found.
    """
    # Initialize the search bounds for the sorted list
    left = 0
    right = len(arr) - 1

    # Iterative binary search loop
    while left <= right:
        # Compute middle index (use floor division)
        mid = (left + right) // 2

        # Extract the value at mid (arr stores (value, original_index) tuples)
        mid_value, mid_orig_index = arr[mid]

        # Compare mid_value with target
        if mid_value == target:
            # Target found — return its original index
            return mid_orig_index
        elif mid_value < target:
            # Target must be in the right half (values greater than mid_value)
            left = mid + 1
        else:
            # Target must be in the left half (values less than mid_value)
            right = mid - 1

    # If we exit the loop, the target is not present
    return -1


def parse_number(s: str) -> Number:
    """
    Parse a string into a number (int if possible, otherwise float).
    Raises ValueError if parsing fails.
    """
    try:
        # Try integer first for cleaner results when possible
        return int(s)
    except ValueError:
        # Fall back to float; let ValueError propagate if not a number
        return float(s)


def main():
    """
    Main entry point:
    - Reads a list from the console
    - Reads a target value
    - Sorts the list while preserving original indices
    - Calls binary_search and prints the result
    """
    try:
        # Read list input from user
        raw_list = input("Enter numbers separated by spaces (e.g. '3 1 4 5 9'): ").strip()
        if not raw_list:
            print("Empty input list. Exiting.")
            return

        # Convert input tokens into numbers (int or float)
        tokens = raw_list.split()
        original_list: List[Number] = [parse_number(tok) for tok in tokens]

        # Read target value
        raw_target = input("Enter the target value: ").strip()
        if not raw_target:
            print("Empty target. Exiting.")
            return

        target = parse_number(raw_target)

    except ValueError as e:
        # Friendly error message for invalid numeric input
        print(f"Invalid numeric input: {e}")
        return
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nInput cancelled by user.")
        return

    # Create a list of pairs (value, original_index) so we can sort without losing original indices
    paired_list = [(value, idx) for idx, value in enumerate(original_list)]
    # Sort the paired list by the value (stable sort). This is the "script sorts itself" step.
    paired_list.sort(key=lambda pair: pair[0])

    # Debugging: show sorted values (optional)
    # print("Debug: sorted paired list:", paired_list)

    # Perform binary search on the sorted paired list
    result_index = binary_search(paired_list, target)

    if result_index != -1:
        print(f"Target {target} found at original index {result_index}.")
    else:
        print(f"Target {target} not found. (returned {result_index})")


if __name__ == "__main__":
    main()
