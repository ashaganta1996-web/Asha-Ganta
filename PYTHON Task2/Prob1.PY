class Student:
    name="Ragini"
    age=23
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=Student()
s1.display()

#constuctor _init_
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=Student("Chari",25)
s2=Student("Chandu",22)
s1.display()
s2.display()

#class attribute
class Student:
    school="St.Ann's School"
s1=Student()
s2=Student()
print(s1.school)
print(s2.school)

#instance attribute
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("Sandeep", 24)
s2=Student("Sirisha", 21)
print(s1.name)
print(s2.name)

#methods
class Student:
    def display(self):
        print("Welcome to Python OOP")
    def study(self):
        print("Avinah is studying Python OOP")
s1=Student()
s1.display()
s1.study()

#employee company details
class Employee:
    company="Infosys"
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def display(self):
        print("Employee Name:",self.name)
        print("Employee Age:",self.age)
        print("Employee Salary:",self.salary)
        print("Company:",self.company)
    def work(self):
        print(self.name,"is working")
e1=Employee("Lucky",25,30000)
e2=Employee("Riya",24,35000)
e3=Employee("Arjun",26,40000)
e1.display()
e1.work()
print("------------------")
e2.display()
e2.work()
print("------------------")
e3.display()
e3.work()