def rectangle_area(x, y):
    return x * y

def square_area(x):
    return x * x

def circle_area(x):
    return 3.14 * x * x

def calculate_area(shape, x, y=0):
    area_functions = {
        "rectangle": lambda x, y: rectangle_area(x, y),
        "square": lambda x, y: square_area(x),
        "circle": lambda x, y: circle_area(x)
    }
    if shape in area_functions:
        return area_functions[shape](x, y)
    else:
        raise ValueError("Unknown shape: {}".format(shape))

# Example function call
result = calculate_area("rectangle", 5, 3)
print(result)
