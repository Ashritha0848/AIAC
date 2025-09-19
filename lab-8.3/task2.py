def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    try:
        user_input = input("Enter the score: ")
        # Try to convert to float or int
        if '.' in user_input:
            score = float(user_input)
        else:
            score = int(user_input)
    except ValueError:
        score = user_input  # Pass as string to trigger invalid input

    grade = assign_grade(score)
    print("Grade:", grade)

if __name__ == "__main__":
    main()
#  Test Case 1: Valid integer input
# Input: 95
# Expected Output: Grade: A

#  Test Case 2: Valid float input
# Input: 82.5
# Expected Output: Grade: B

#  Test Case 3: Boundary case (exactly 70)
# Input: 70
# Expected Output: Grade: C

#  Test Case 4: Failing grade
# Input: 45
# Expected Output: Grade: F

#  Test Case 5: Out of range (greater than 100)
# Input: 110
# Expected Output: Grade: Invalid input

# Test Case 6: Out of range (negative number)
# Input: -5
# Expected Output: Grade: Invalid input

#  Test Case 7: Non-numeric input
# Input: hello
# Expected Output: Grade: Invalid input

    

