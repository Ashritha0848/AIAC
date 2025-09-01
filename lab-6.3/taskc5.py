class BankAccount:
    def __init__(self, name, balance=0):

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        
        print(f"Account balance for {self.name}: ${self.balance}")

# Example usage from console:
if __name__ == "__main__":
    # Create a new bank account for Alice with $100
    account = BankAccount("Alice", 100)
    account.check_balance()      # Output: Account balance for Alice: $100
    account.deposit(50)          # Output: Deposited $50. New balance: $150
    account.withdraw(30)         # Output: Withdrew $30. New balance: $120
    account.withdraw(200)        # Output: Insufficient funds.
    account.check_balance()      # Output: Account balance for Alice: $120


