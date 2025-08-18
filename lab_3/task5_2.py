def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Example usage:
f = float(input("Enter temperature in Fahrenheit: "))
c = fahrenheit_to_celsius(f)
print(f"{f}°F is {c}°C")



