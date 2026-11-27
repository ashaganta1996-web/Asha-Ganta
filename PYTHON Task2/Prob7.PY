#abstraction
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Toy(Vehicle):
    def start(self):
        print("Toy starts with a key")
class Motor(Vehicle):
    def start(self):
        print("Motor starts with a switch")
Toy1=Toy()
Motor1=Motor()
Toy1.start()
Motor1.start()

#abstraction using abc module
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
class SBI(ATM):
    def withdraw(self,amount):
        balance=24000
        if amount>0 and amount<=balance:
            balance=balance-amount
            print("Cash Withdrawn:",amount)
            print("Remaining Balance:",balance)
        else:
            print("Insufficient Balance or Invalid Amount")
atm1=SBI()
atm1.withdraw(9000)

#shape of circle
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Circle Area:",3.14*self.radius*self.radius)
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("Rectangle Area:",self.length*self.width)
c1=Circle(5)
r1=Rectangle(10,5)
c1.area()
r1.area()

#employee requirements
from abc import ABC,abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20000
class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000
emp1=FullTimeEmployee()
emp2=PartTimeEmployee()
emp3=ContractEmployee()
print("Full-Time Employee Salary: ₹",emp1.calculate_salary())
print("Part-Time Employee Salary: ₹",emp2.calculate_salary())
print("Contract Employee Salary: ₹",emp3.calculate_salary())