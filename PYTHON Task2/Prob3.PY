#constructor _init_
class Student:
    def __init__(self):
        self.name="Ranjan"
        self.age=31
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=Student()
s1.display()

#constructor with parameters
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s1=Student("Athul",22,85)
s2=Student("Shriya",21,90)
s3=Student("Tarun",23,75)
s1.display()
s2.display()
s3.display()

#constructor with default values
class Employee:
    def __init__(self,name="Unknown",salary=20000):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee Name:",self.name)
        print("Employee Salary:",self.salary)
e1=Employee("Radha",30000)
e2=Employee("Krishna",40000)
e3=Employee()
e1.display()
e2.display()
e3.display()

#bank account receipt
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn:",amount)
        else:
            print("Insufficient Balance")
    def display(self):
        print("Account Holder:",self.account_holder)
        print("Available Balance:",self.balance)
a1=BankAccount("Asha",7000)
a1.display()
a1.deposit(500)
a1.withdraw(700)
a1.display()