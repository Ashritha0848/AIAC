def is_valid_palindrome(s: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if cleaned string is a palindrome
    return cleaned == cleaned[::-1]

# Example usage
if __name__ == "__main__":
    test_str = ""
    test_str = input("Enter a string: ")
    print(is_valid_palindrome(test_str))