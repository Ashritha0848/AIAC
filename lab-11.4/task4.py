class Node:
    """
    Represents a single node in a Binary Search Tree.
    Each node stores an integer value and optional left/right children.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    A simple Binary Search Tree implementation supporting insert, search,
    and inorder traversal.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert a new value into the BST.

        Args:
            value (int): The integer value to insert.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            elif value > node.data:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        """
        Search for a value in the BST.

        Args:
            value (int): The integer value to search for.

        Returns:
            bool: True if found, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if node.data == value:
                return True
            elif value < node.data:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self):
        """
        Perform an in-order traversal of the tree.

        Returns:
            list: List of elements in in-order.
        """
        def _inorder(node):
            if node is None:
                return []
            return _inorder(node.left) + [node.data] + _inorder(node.right)

        return _inorder(self.root)


def test_bst():
    print("Binary Search Tree Test")
    print("Commands: insert <int>, search <int>, inorder, quit")
    bst = BST()
    while True:
        inp = input("Enter command: ").strip()
        if not inp:
            continue
        if inp == "quit":
            print("Exiting BST test.")
            break
        elif inp.startswith("insert "):
            try:
                _, val = inp.split(" ", 1)
                num = int(val)
                bst.insert(num)
                print(f"Inserted: {num}")
            except ValueError:
                print("Error: Please provide a valid integer for insert.")
        elif inp.startswith("search "):
            try:
                _, val = inp.split(" ", 1)
                num = int(val)
                found = bst.search(num)
                if found:
                    print(f"{num} found in BST.")
                else:
                    print(f"{num} NOT found in BST.")
            except ValueError:
                print("Error: Please provide a valid integer for search.")
        elif inp == "inorder":
            print("Inorder traversal:", bst.inorder_traversal())
        else:
            print("Unknown command.")

if __name__ == "__main__":
    test_bst()
