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

#2. Employee Management 

#Base Class
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def calulate_salary(self):
        return self.salary
    
#Sub Class:RegularEmployee
class RegularEmployee(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def calulate_salary(self):
        return self.salary + self.bonus
#Sub Class: ContractEmployee
class ContractEmployee(Employee):
    def __init__(self,name,salary,contract_duration):
        super().__init__(name,salary)
        self.contract_duration = contract_duration
    def calulate_salary(self):
        return self.salary * self.contract_duration
#Sub Class : Manager
class Manager(Employee):   
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size = team_size
    def calulate_salary(self):
        return self.salary + (self.team_size * 1000)

Regular = RegularEmployee("Alice",50000,5000)
Contract = ContractEmployee("Bob",30000,12)
Manager = Manager("Charlie",70000,5)

print(f"{Regular.name}'s Salary: {Regular.calulate_salary()}")
print(f"{Contract.name}'s Salary: {Contract.calulate_salary()}")
print(f"{Manager.name}'s Salary: {Manager.calulate_salary()}")  


#3. Vehicle Rental

#Base Class
class Vehicle:
    def __init__(self, model, rental_rate):
        self.mode = model
        self.rental_rate = rental_rate
    def calculate_rental(self):
        return self.rental_rate
#Subclass : Car
class Car(Vehicle):
    def __init__(self, model, rental_rate, seating_capacity):
        super().__init__(model, rental_rate)
        self.seating_capacity = seating_capacity
    def calculate_rental(self):
        return self.rental_rate * self.seating_capacity
#Subclass : Bike
class Bike(Vehicle):
    def __init__(self, model, rental_rate, engine_capacity):
        super().__init__(model, rental_rate)
        self.engine_capacity = engine_capacity
    def calculate_rental(self):
        return self.rental_rate * (self.engine_capacity / 100)
#Subclass : Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity
    def calculate_rental(self):
        return self.rental_rate * (self.load_capacity / 1000)
    
Car1 = Car("Sedan", 50, 5)
Bike1 = Bike("Sport", 30, 600)
Truck1 = Truck("Lorry", 100, 5000)  

print(f"{Car1.mode} Rental Cost: {Car1.calculate_rental()}")
print(f"{Bike1.mode} Rental Cost: {Bike1.calculate_rental()}")
print(f"{Truck1.mode} Rental Cost: {Truck1.calculate_rental()}")

