
class ListQueue:
    """Queue implementation using Python lists."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def __str__(self):
        return f"Queue: {self.items}"


def test_list_queue():
    print("List-based Queue. Commands: enqueue <value>, dequeue, is_empty, show, quit")
    queue = ListQueue()
    while True:
        command = input("Enter command: ").strip()
        if not command:
            continue
        if command == 'quit':
            print("Exiting ListQueue test.\n")
            break
        elif command.startswith('enqueue '):
            _, value = command.split(' ', 1)
            queue.enqueue(value)
            print(f"Enqueued: {value}")
        elif command == 'dequeue':
            try:
                value = queue.dequeue()
                print(f"Dequeued: {value}")
            except IndexError as e:
                print(f"Error: {e}")
        elif command == 'is_empty':
            print(f"Is empty: {queue.is_empty()}")
        elif command == 'show':
            print(queue)
        else:
            print("Unknown command.")


# AI performance review
def performance_review():
    print("\n=== AI Queue Performance Review ===")
    print(
        "The above ListQueue uses a Python list. While appending (enqueue) is O(1), "
        "removing from the front (dequeue) is O(n) because all remaining elements must be shifted.\n"
        "For large queues or frequent dequeues, this is inefficient. "
        "A better alternative is to use collections.deque, which provides O(1) time for both enqueueing and dequeueing "
        "as it is implemented as a double-ended queue.\n"
        "Below is the optimized version using collections.deque."
    )


# Optimized version using deque
from collections import deque

class DequeQueue:
    """Queue implementation using collections.deque for efficiency."""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def __str__(self):
        return f"Queue: {list(self.items)}"


def test_deque_queue():
    print("Deque-based Queue. Commands: enqueue <value>, dequeue, is_empty, show, quit")
    queue = DequeQueue()
    while True:
        command = input("Enter command: ").strip()
        if not command:
            continue
        if command == 'quit':
            print("Exiting DequeQueue test.")
            break
        elif command.startswith('enqueue '):
            _, value = command.split(' ', 1)
            queue.enqueue(value)
            print(f"Enqueued: {value}")
        elif command == 'dequeue':
            try:
                value = queue.dequeue()
                print(f"Dequeued: {value}")
            except IndexError as e:
                print(f"Error: {e}")
        elif command == 'is_empty':
            print(f"Is empty: {queue.is_empty()}")
        elif command == 'show':
            print(queue)
        else:
            print("Unknown command.")


if __name__ == "__main__":
    print("=== Queue Test (List version) ===")
    test_list_queue()
    performance_review()
    print("\n=== Queue Test (Deque version) ===")
    test_deque_queue()


