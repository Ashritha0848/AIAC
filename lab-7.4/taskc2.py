
# The current sort_list will fail with mixed types (int and str).
# To sort numbers before strings, define a custom key:
def sort_list(data):
    return sorted(data, key=lambda x: (isinstance(x, str), x))
items = [3, "apple", 1, "banana", 2]
print(sort_list(items))








