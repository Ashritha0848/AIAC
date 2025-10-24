class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node in the list; initially None.

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list (head pointer is None).

    def insert_at_end(self, value):
        """Insert a new node with the given value at the end of the list."""
        new_node = Node(value)
        if not self.head:
            # If the list is empty, update head to point to new node
            self.head = new_node
            # Comment: The head pointer now references the new node.
        else:
            current = self.head
            # Traverse to the last node (whose .next is None)
            while current.next:
                current = current.next
            # Set the last node's next pointer to our new node
            current.next = new_node
            # Comment: Link from previous tail node now points to the new node.

    def delete_value(self, value):
        """Delete the first node with the given value."""
        current = self.head
        prev = None
        # Traverse to find the node to delete
        while current:
            if current.data == value:
                if prev:
                    # Bypass the current node by pointing prev.next to current.next
                    prev.next = current.next
                    # Comment: The node to delete is unlinked from the list by updating prev.next.
                else:
                    # We're deleting the head node, so move head to next node
                    self.head = current.next
                    # Comment: The head pointer moves to the next node.
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Return a list of all node values in the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move pointer to the next node.
        return elements

def test_linked_list():
    print("Singly Linked List. Commands: insert <value>, delete <value>, traverse, quit")
    ll = LinkedList()
    while True:
        command = input("Enter command: ").strip()
        if not command:
            continue
        if command == 'quit':
            print("Exiting linked list test.")
            break
        elif command.startswith('insert '):
            _, value = command.split(' ', 1)
            ll.insert_at_end(value)
            print("Inserted:", value)
        elif command.startswith('delete '):
            _, value = command.split(' ', 1)
            result = ll.delete_value(value)
            if result:
                print("Deleted:", value)
            else:
                print("Value not found:", value)
        elif command == 'traverse':
            print("List contents:", ll.traverse())
        else:
            print("Unknown command.")

# AI Test Case Suggestions:
# 1. Insert several values and traverse to ensure all values are in order.
# 2. Delete head node and check if the new head is correct.
# 3. Delete a value from the middle and check that the linkage is correct (i.e., no values lost/skipped).
# 4. Delete the last node and check the list's integrity.
# 5. Attempt to delete a value that doesn't exist (should not change list).
# 6. Traverse on an empty list.
# 7. Insert and immediately delete to check single-element behavior.

if __name__ == "__main__":
    test_linked_list()
