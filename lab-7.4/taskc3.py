with open("example.txt", "w") as f:
    f.write("Hello,World")

with open("data1.txt", "w") as f1:
    f1.write("First file content\n")

with open("data2.txt", "w") as f2:
    f2.write("second file content\n")

print("files written successfully")

with open("input.txt", "r") as data_file:
    data = data_file.readlines()

with open("output.txt", "w") as output:
    for line in data:
        output.write(line.upper())

print("processing done")

with open("numbers.txt", "r") as num_file:
    nums = num_file.readlines()

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

with open("squares.txt", "w") as squares_file:
    for sq in squares:
        squares_file.write(str(sq) + "\n")

print("squares written ")
    