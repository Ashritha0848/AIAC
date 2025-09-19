class ShoppingCart:
    def __init__(self):
        self.items = {}
    def add_item(self, name, price):
        if name in self.items:
            self.items[name].append(price)
        else:
            self.items[name] = [price]
    def remove_item(self, name):
        if name in self.items:
            if self.items[name]:
                self.items[name].pop()
                if not self.items[name]:
                    del self.items[name]
        else:
            print(f"Item '{name}' not found in cart.")
    def total_cost(self):
        return sum(sum(prices) for prices in self.items.values())
def main():
    cart = ShoppingCart()
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Show total cost")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            name = input("Enter item name: ")
            try:
                price = float(input("Enter item price: "))
                cart.add_item(name, price)
                print(f"Added '{name}' with price {price} to cart.")
            except ValueError:
                print("Invalid price. Please enter a number.")
        elif choice == "2":
            name = input("Enter item name to remove: ")
            cart.remove_item(name)
            print(f"Removed one '{name}' from cart (if present).")
        elif choice == "3":
            total = cart.total_cost()
            print(f"Total cost: {total}")
        elif choice == "4":
            print("Exiting Shopping Cart.")
            break
        else:
            print("Invalid choice. Please select 1-4.")
if __name__ == "__main__":
    main()
cart = ShoppingCart()
cart = ShoppingCart()
# ✅ Test Case 1: Add a single item
cart.add_item("Apple", 50)
print("Expected: 50.0, Got:", cart.total_cost())   # 50.0
# ✅ Test Case 2: Add multiple different items
cart.add_item("Milk", 30)
cart.add_item("Bread", 20)
print("Expected: 100.0, Got:", cart.total_cost())  # 50 + 30 + 20 = 100.0
# ✅ Test Case 3: Add multiple quantities of the same item
cart.add_item("Eggs", 10)
cart.add_item("Eggs", 10)
cart.add_item("Eggs", 10)
print("Expected: 130.0, Got:", cart.total_cost())  # 100 + (10*3) = 130.0
# ✅ Test Case 4: Remove one item when multiple exist
cart.add_item("Orange", 15)
cart.add_item("Orange", 15)
cart.remove_item("Orange")
print("Expected: 145.0, Got:", cart.total_cost())  # 130 + (15*2 - 15) = 145.0
# ❌ Test Case 5: Remove item not in cart
cart.remove_item("Banana")  # Should print "Item 'Banana' not found in cart."
print("Expected: 145.0, Got:", cart.total_cost())  # No change
# ✅ Test Case 6: Remove all items and check total
cart.add_item("Juice", 40)
cart.remove_item("Juice")
print("Expected: 145.0, Got:", cart.total_cost())  # Juice removed
# ❌ Test Case 7: Invalid price entry
try:
    cart.add_item("Pencil", float("abc"))  # Force invalid price
except ValueError:
    print("Expected: Invalid price error caught")
# ❌ Test Case 8: Invalid menu choice → simulated by skipping (menu is interactive)
print("Invalid menu choice test skipped (handled in main loop).")
