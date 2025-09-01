def classify_age(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teen"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    else:
        return "Invalid age"

# Take age input from console
try:
    age_input = int(input("Enter your age: "))
    group = classify_age(age_input)
    print(f"Age group: {group}")
except ValueError:
    print("Please enter a valid integer for age.")