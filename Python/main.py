# 1. Bank Account
# Base Class
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number   # private attribute
        self.__balance = balance                 # encapsulated balance

    def get_balance(self):
        return self.__balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Withdraw method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # Display account info
    def display_info(self):
        print(f"Account Number: {self.__account_number}, Balance: {self.__balance}")


# Subclass: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.05):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest earned: {interest}")
        return interest


# Subclass: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=1000):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount > 0 and (self.get_balance() - amount) >= self.minimum_balance:
            # Call parent withdraw
            super().withdraw(amount)
        else:
            print("Withdrawal denied. Minimum balance requirement not met.")


# --- Usage Example ---
# Create accounts
savings = SavingsAccount("SA123", 2000, 0.04)
current = CurrentAccount("CA456", 5000, 1000)

# Operations
savings.deposit(500)
savings.calculate_interest()
savings.withdraw(1000)
savings.display_info()

current.withdraw(4500)   # Denied due to minimum balance
current.withdraw(3000)   # Allowed
current.display_info()
