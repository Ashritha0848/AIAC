def convert_date_format(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"
assert convert_date_format("2023-10-15") 
# Manual Test Cases for convert_date_format()
# ✅ Test Case 1: Normal valid date
print("Input: 2023-10-15")
print("Expected: 15-10-2023")
print("Got:", convert_date_format("2023-10-15"))
print()
# ✅ Test Case 2: Date with single-digit month and day
print("Input: 2023-01-05")
print("Expected: 05-01-2023")
print("Got:", convert_date_format("2023-01-05"))
print()
# ✅ Test Case 3: Leap year date
print("Input: 2020-02-29")
print("Expected: 29-02-2020")
print("Got:", convert_date_format("2020-02-29"))
print()
# ❌ Test Case 4: Invalid format (slashes instead of dashes)
try:
    print("Input: 2023/10/15")
    print("Expected: ValueError")
    print("Got:", convert_date_format("2023/10/15"))
except ValueError as e:
    print("Caught Exception:", e)
print()
