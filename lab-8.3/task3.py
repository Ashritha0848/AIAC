import string
def is_sentence_palindrome(sentence):
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_sentence_palindrome(sentence):
        print("Palindrome")
    else:
        print("Not a palindrome")
# ✅ Test Case 1: Simple palindrome
# Input: "madam"
# Expected Output: Palindrome
# ✅ Test Case 2: Palindrome with spaces
# Input: "nurses run"
# Expected Output: Palindrome
# ✅ Test Case 3: Palindrome with punctuation
# Input: "A man, a plan, a canal: Panama"
# Expected Output: Palindrome
# ✅ Test Case 4: Not a palindrome
# Input: "hello world"
# Expected Output: Not a palindrome
# ✅ Test Case 5: Single character
# Input: "x"
# Expected Output: Palindrome
# ✅ Test Case 6: Empty string
# Input: ""
# Expected Output: Palindrome   # (empty is considered symmetric)
# ✅ Test Case 7: Mixed case palindrome
# Input: "RaceCar"
# Expected Output: Palindrome

