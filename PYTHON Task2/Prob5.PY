#inheritance
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d=Dog()
d.eat()
d.bark()

#inheritance extension base class
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print("Vehicle Brand:",self.brand)
        print("Vehicle Speed:",self.speed)
class Car(Vehicle):
    def __init__(self,brand,speed,model):
        super().__init__(brand,speed)
        self.model=model
    def display_car(self):
        self.display()
        print("Car Model:",self.model)
car1=Car("Toyota",180,"Innova")
car2=Car("Honda",160,"City")
car1.display_car()
print("-------------------")
car2.display_car()

#employee and manager
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display_employee(self):
        print("Employee Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display_manager(self):
        self.display_employee()
        print("Department:",self.department)
manager1=Manager("Sonu",70000,"IT")
manager2=Manager("Asha",90000,"HR")
print("Manager1 Details:")
manager1.display_manager()
print("-------------------------")
print("Manager2 Details:")
manager2.display_manager()