class Stack:
    """A simple Stack (LIFO) data structure implementation.

    Supports basic stack operations: push, pop, peek, and is_empty.
    """

    def __init__(self):
        """Initializes an empty stack."""
        self.items = []

    def push(self, item):
        """Pushes an item onto the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack.

        Returns:
            The item removed from the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Returns the top item from the stack without removing it.

        Returns:
            The top item of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Checks if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return len(self.items) == 0


def test_stack_operations():
    """Interactively tests stack operations using user input."""
    stack = Stack()
    print("Stack created. Available operations: push <value>, pop, peek, is_empty, quit")
    while True:
        command = input("Enter command: ").strip()
        if not command:
            continue
        if command == 'quit':
            print("Exiting stack test.")
            break
        elif command.startswith('push '):
            # Allow space in value after 'push '
            _, value = command.split(' ', 1)
            stack.push(value)
            print(f"Pushed: {value}")
        elif command == 'pop':
            try:
                value = stack.pop()
                print(f"Popped: {value}")
            except IndexError as e:
                print(f"Error: {e}")
        elif command == 'peek':
            try:
                value = stack.peek()
                print(f"Top of stack: {value}")
            except IndexError as e:
                print(f"Error: {e}")
        elif command == 'is_empty':
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        else:
            print("Unknown command.")

if __name__ == "__main__":
    test_stack_operations()

# ---------------------------------------------
# Optimization Suggestion:
# For larger-scale or performance-critical applications, consider using collections.deque,
# which is optimized for fast append and pop operations from both ends.

# Alternative Stack Implementation using deque:
#
# from collections import deque
#
# class Stack:
#     def __init__(self):
#         self.items = deque()
#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.items:
#             raise IndexError("pop from empty stack")
#         return self.items.pop()
#     def peek(self):
#         if not self.items:
#             raise IndexError("peek from empty stack")
#         return self.items[-1]
#     def is_empty(self):
#         return not self.items

