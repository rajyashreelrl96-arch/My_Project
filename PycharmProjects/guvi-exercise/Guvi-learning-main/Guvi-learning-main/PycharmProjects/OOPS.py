#1.Bank Account
class BankAccount:
    def __init__(self, account_number, balance):   #using attributes: account_number, balance
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):    #deposit method
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount rs.{amount}, current Balance rs{self.balance}")
        else:
            print("Deposit amount should be positive")
    def withdraw(self, amount):   #withdraw method
        if amount <= 0:
            print("withdraw amount should be positive")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
           self.balance -= amount
           print(f"withdraw amount rs{amount}, current Balance rs.{self.balance}")
    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest {interest} added. Current balance is {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance
    def withdraw(self, amount):
        if amount > 0:
            print("withdraw amount should be positive")
        elif self.balance - amount < self.minimum_balance:
            print("withdraw amount do not exceed the minimum balance")
        else:
            self.balance -= amount
            print(f"withdraw amount rs.{amount}, Current Balance rs{self.balance}")
savings = SavingsAccount("AA112200", 5000, 5)
savings.deposit(1000)
savings.calculate_interest()
savings.withdraw(1000)

print("-" * 40)
current = CurrentAccount("AA2200",  3000, 1000)
current.deposit(2000)
current.withdraw(1000)
current.withdraw(500)

#Employee Management
class Employee:
    def __init__(self,name):
        self.name = name
        self._salary = 0  #using encapsulated to protect salary
    def calculate_salary(self):
        pass
    def get_salary(self):
        return self._salary
class  RegularEmployee(Employee):
    def __init__(self,name,basic_salary,hra,da):
        super().__init__(name)
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
    def calculate_salary(self):
        self._salary = self.basic_salary+self.hra*self.da
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_salary(self):
        self._salary = self.hourly_rate * self.hours_worked
class Manager(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name)
        self.basic_salary = basic_salary
        self.bonus = bonus
    def calculate_salary(self):
        self._salary = self.basic_salary + self.bonus

Employees = [
    RegularEmployee("john", 10000, 5000, 1000 ),
    ContractEmployee("joe", 500, 30 ),
    Manager("raji", 20000, 1000)
]
for emp in Employees:
    emp.calculate_salary()
    print(f"{emp.name} salary: rs.{emp.get_salary()}")


#Vehicle Rental
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate
    def calculate_rental(self, days):
        pass
class Car(Vehicle):
    def __init__(self, model, rental_rate, insurance_fee ):
        super().__init__(model, rental_rate)
        self.insurance_fee = insurance_fee
    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.insurance_fee
class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee):
        super().__init__(model, rental_rate)
        self.helmet_fee = helmet_fee
    def calculate_rental(self, days):
        return (self.rental_rate * days) + self.helmet_fee
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_fee):
        super().__init__(model, rental_rate)
        self.load_fee = load_fee
    def calculate_rental(self, days):
        return (self.rental_rate *days) + self.load_fee
vehicles = [
    Car("Ford", 3000, 500 ),
    Bike("yamaha", 2000, 50 ),
    Truck("Volkswagen", 1500, 1500)
]
for v in vehicles:
    print(f"{v.model} Rental cost for 5 days: rs.{v.calculate_rental(5)}")