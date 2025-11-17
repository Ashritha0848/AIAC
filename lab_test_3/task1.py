
class Stack:
    def __init__(self, items=None):
        self._items = list(items) if items else []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)

    def as_list(self):
        # Return a shallow copy so external code can't mutate internal list.
        return list(self._items)

    def __repr__(self):
        # Shows bottom -> ... -> top (rightmost is top)
        return "Stack(" + repr(self._items) + ")"


def read_initial_stack():
    s = input("Enter initial stack elements separated by spaces (or leave empty): ").strip()
    if not s:
        return []
    return s.split()


def main():
    # Read the initial stack from console
    initial = read_initial_stack()
    stack = Stack(initial)
    print(f"Initial stack (bottom -> top): {stack.as_list()}")

    # Push 5 elements (taken from console)
    print("Now push 5 elements (one per prompt).")
    for i in range(5):
        elem = input(f"Enter element to push #{i+1}: ")
        stack.push(elem)
        print(f"Pushed: {elem} -> current stack (bottom -> top): {stack.as_list()}")

    # Pop 2 elements (confirmation taken from console)
    cmd = input("Type 'pop' to pop 2 elements from the stack, or press Enter to skip: ").strip().lower()
    if cmd == "pop":
        popped = []
        for _ in range(2):
            try:
                popped.append(stack.pop())
            except IndexError:
                print("Cannot pop: stack is empty.")
                break
        print(f"Popped elements (in pop order): {popped}")
    else:
        print("Skipping pop operation.")

    # Display remaining stack
    print(f"Remaining stack (bottom -> top): {stack.as_list()}")
    print(f"Stack size: {stack.size()}")
    top = stack.peek()
    print(f"Top element: {top if top is not None else 'None'}")


if __name__ == "__main__":
    main()