import unittest
from task4 import ShoppingCart
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
    def test_add_single_item(self):
        self.cart.add_item("Apple", 50)
        self.assertEqual(self.cart.total_cost(), 50)
    def test_add_multiple_different_items(self):
        self.cart.add_item("Milk", 30)
        self.cart.add_item("Bread", 20)
        self.assertEqual(self.cart.total_cost(), 50)
    def test_add_multiple_quantities_same_item(self):
        self.cart.add_item("Eggs", 10)
        self.cart.add_item("Eggs", 10)
        self.cart.add_item("Eggs", 10)
        self.assertEqual(self.cart.total_cost(), 30)
    def test_remove_one_of_multiple_items(self):
        self.cart.add_item("Orange", 15)
        self.cart.add_item("Orange", 15)
        self.cart.remove_item("Orange")
        self.assertEqual(self.cart.total_cost(), 15)
    def test_remove_item_not_in_cart(self):
        self.cart.add_item("Apple", 10)
        self.cart.remove_item("Banana")
        self.assertEqual(self.cart.total_cost(), 10)
    def test_remove_all_items_and_check_total(self):
        self.cart.add_item("Juice", 40)
        self.cart.remove_item("Juice")
        self.assertEqual(self.cart.total_cost(), 0)
    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0)
    def test_add_and_remove_various(self):
        self.cart.add_item("A", 5)
        self.cart.add_item("B", 10)
        self.cart.add_item("A", 5)
        self.cart.remove_item("A")
        self.assertEqual(self.cart.total_cost(), 15)  # One A removed, one left
    def test_remove_item_until_gone(self):
        self.cart.add_item("Pen", 2)
        self.cart.add_item("Pen", 2)
        self.cart.remove_item("Pen")
        self.cart.remove_item("Pen")
        self.assertEqual(self.cart.total_cost(), 0)
        self.assertNotIn("Pen", self.cart.items)
    def test_add_item_with_float_price(self):
        self.cart.add_item("Notebook", 12.75)
        self.assertAlmostEqual(self.cart.total_cost(), 12.75)
    def test_add_item_with_zero_price(self):
        self.cart.add_item("Freebie", 0)
        self.assertEqual(self.cart.total_cost(), 0)
    def test_remove_item_from_empty_cart(self):
        self.cart.remove_item("Ghost")
        self.assertEqual(self.cart.total_cost(), 0)
if __name__ == "__main__":
    unittest.main()
