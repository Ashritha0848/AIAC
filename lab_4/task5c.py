"""
Few-shot prompt:
Given a paragraph, write a Python function that:
- Accepts a paragraph as input,
- Converts all text to lowercase,
- Removes punctuation,
- Analyzes word frequency (returns a dictionary of word counts).
Example 1:
Input: "My name is Niha."
Output: {'my': 1, 'name': 1, 'is': 1, 'niha': 1}
Example 2:
Input: "I’m from Kataram."
Output: {'im': 1, 'from': 1, 'kataram': 1}
Example 3:
Input: "I completed my schooling in Montessori."
Output: {'i': 1, 'completed': 1, 'my': 1, 'schooling': 1, 'in': 1, 'montessori': 1}
"""
def analyze_word_frequency(paragraph):
    import string
    # Convert to lowercase
    text = paragraph.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation + "’‘“”"))
    # Split into words
    words = text.split()

    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
para1 = "My name is Niha."
para2 = "I’m from Kataram."
para3 = "I completed my schooling in Montessori."
print(analyze_word_frequency(para1))  # Output: {'my': 1, 'name': 1, 'is': 1, 'niha': 1}
print(analyze_word_frequency(para2))  # Output: {'im': 1, 'from': 1, 'kataram': 1}
print(analyze_word_frequency(para3))  # Output: {'i': 1, 'completed': 1, 'my': 1, 'schooling': 1, 'in': 1, 'montessori': 1}
