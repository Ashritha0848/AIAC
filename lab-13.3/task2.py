def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return None

# Example function call
result = read_file("example.txt")
print(result)
