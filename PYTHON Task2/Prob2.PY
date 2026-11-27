class Student:
    def display(self):
        print("Welcome to BlackRoth")
student1=Student()
student2=Student()
student3=Student()
student1.display()
student2.display()
student3.display()

class Student:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print("Student Name:",self.name)
        print("Student Age:",self.age)
        print("Student City:",self.city)
        print("-------------------")
student1=Student("AliKhan",25,"Hyderabad")
student2=Student("Samaya",23,"Vijayawada")
student3=Student("Karan",21,"Bangalore")
student1.display()
student2.display()
student3.display()

#create class with instantiate multiple objects
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        print(self.name,"scored",self.marks,"marks")
s1=Student("Sudheer",84)
s2=Student("Sanjay",90)
s3=Student("Sukanya",73)
s4=Student("Sneha",65)
s1.result()
s2.result()
s3.result()
s4.result()

#employee role and salary details
class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
    def display(self):
        print("Employee Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
        print("------------------------")
emp1=Employee("Bhagya",25200,"IT")
emp2=Employee("Jyothi",30500,"HR")
emp3=Employee("Suguna",35300,"Finance")
emp1.display()
emp2.display()
emp3.display()