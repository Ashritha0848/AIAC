"""
Few-shot prompt:
Given a nested dictionary representing student information, create a function that extracts the full name, branch, and sgpa.

Example 1:
Input: {'name': 'radha', 'details': {'branch': 'cse', 'sgpa': 9}}
Output: ('radha', 'cse', 9)

Example 2:
Input: {'name': 'krishna', 'details': {'branch': 'ece', 'sgpa': 9.5}}
Output: ('krishna', 'ece', 9.5)

Example 3:
Input: {'name': 'ravi', 'details': {'branch': 'ee', 'sgpa': 8}}
Output: ('ravi', 'ee', 8)
"""

def parse_student_info(student_dict):
    """
    Parses a nested dictionary representing student information and returns a tuple of (full_name, branch, sgpa).
    """
    full_name = student_dict.get('name')
    details = student_dict.get('details', {})
    branch = details.get('branch')
    sgpa = details.get('sgpa')
    return (full_name, branch, sgpa)

# Example usage:
student1 = {'name': 'radha', 'details': {'branch': 'cse', 'sgpa': 9}}
student2 = {'name': 'krishna', 'details': {'branch': 'ece', 'sgpa': 9.5}}
student3 = {'name': 'ravi', 'details': {'branch': 'ee', 'sgpa': 8}}

print(parse_student_info(student1))  # Output: ('radha', 'cse', 9)
print(parse_student_info(student2))  # Output: ('krishna', 'ece', 9.5)
print(parse_student_info(student3))  # Output: ('ravi', 'ee', 8)
