# Function to print first 10 multiples of a number using a for loop
def print_multiples_for():
    num = int(input("Enter a number: "))
    print("First 10 multiples using for loop:")
    for i in range(1, 11):
        print(num * i)

# Function to print first 10 multiples of a number using a while loop
def print_multiples_while():
    num = int(input("Enter a number: "))
    print("First 10 multiples using while loop:")
    i = 1
    while i <= 10:
        print(num * i)
        i += 1

        
print_multiples_for()
print_multiples_while()