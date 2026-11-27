#student course details using class,objects,attributes,methods and _init_ constructor
class Student:
    def __init__(self,name,age,course,city):
        self.name=name
        self.age=age
        self.course=course
        self.city=city
    def display_details(self):
        print("Student Name:",self.name)
        print("Student Age:",self.age)
        print("Student Course:",self.course)
        print("Student City:",self.city)
    def study(self):
        print(self.name,"is studying",self.course)
    def attend_class(self):
        print(self.name,"is attending class.")
student1=Student("Sandhya",22,"Cloud computing","Hyderabad")
student2=Student("Sujay",21,"Java","Chennai")
student3=Student("Srishika",23,"Python","Bangalore")
student1.display_details()
student1.study()
student1.attend_class()
print("-------------------")
student2.display_details()
student2.study()
student2.attend_class()
print("-------------------")
student3.display_details()
student3.study()
student3.attend_class()

#employee salary details using encapsulation,inheritance,polymorphism and abstraction
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()+5000
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()+2000
class ContractEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()+3000
emp1=FullTimeEmployee("Varun",30000)
emp2=PartTimeEmployee("Tarun",15000)
emp3=ContractEmployee("Arun",25000)
employees=[emp1,emp2,emp3]
for emp in employees:
    print("Employee Name:",emp.name)
    print("Basic Salary: Rs.",emp.get_salary())
    print("Total Salary: Rs.",emp.calculate_salary())
    print("----------------------")

#library management system
from abc import ABC,abstractmethod
class Library(ABC):
    def __init__(self,book_name,book_id):
        self.book_name=book_name
        self.book_id=book_id
        self.__available=True
    def get_availability(self):
        return self.__available
    def set_availability(self,status):
        self.__available=status
    @abstractmethod
    def book_type(self):
        pass
    def display_details(self):
        print("Book Name:",self.book_name)
        print("Book ID:",self.book_id)
        print("Book Type:",self.book_type())
        print("Available:",self.get_availability())
    def issue_book(self):
        if self.__available:
            self.__available=False
            print(self.book_name,"has been issued.")
        else:
            print(self.book_name,"is not available.")
    def return_book(self):
        if not self.__available:
            self.__available=True
            print(self.book_name,"has been returned.")
        else:
            print(self.book_name,"is already available.")
class StoryBook(Library):
    def book_type(self):
        return "Story Book"
class ScienceBook(Library):
    def book_type(self):
        return "Science Book"
class HistoryBook(Library):
    def book_type(self):
        return "History Book"
class ComputerBook(Library):
    def book_type(self):
        return "Computer Book"
book1=StoryBook("Harry Potter",201)
book2=ScienceBook("Physics",302)
book3=HistoryBook("Indian History",403)
book4=ComputerBook("Python Programming",504)
print("----- Library Book Details -----")
book1.display_details()
print()
book2.display_details()
print()
book3.display_details()
print()
book4.display_details()
print()
print("----- Issue Book -----")
book1.issue_book()
print("Available:",book1.get_availability())
print("\n----- Return Book -----")
book1.return_book()
print("Available:",book1.get_availability())
print("\n----- Polymorphism -----")
books=[book1,book2,book3,book4]
for book in books:
    print(book.book_name,"-",book.book_type())

#employee management system
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,name,emp_id):
        self.name=name
        self.emp_id=emp_id
        self.__salary=0
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    @abstractmethod
    def calculate_salary(self):
        pass
    def display_details(self):
        print("Employee Name:",self.name)
        print("Employee ID:",self.emp_id)
        print("Salary: ₹",self.calculate_salary())
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 60000
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 40000
class ContractEmployee(Employee):
    def calculate_salary(self):
        return 20000
emp1=FullTimeEmployee("Anshu",101)
emp2=PartTimeEmployee("Aarpith",102)
emp3=ContractEmployee("Arya",103)
emp1.set_salary(60000)
emp2.set_salary(40000)
emp3.set_salary(20000)
print("----- Full-Time Employee -----")
emp1.display_details()
print("\n----- Part-Time Employee -----")
emp2.display_details()
print("\n----- Contract Employee -----")
emp3.display_details()
print("\n----- Polymorphism -----")
employees=[emp1,emp2,emp3]
for emp in employees:
    print(emp.name, "Salary: ₹",emp.calculate_salary())

#banking management system
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,customer_name,account_number,balance):
        self.customer_name=customer_name
        self.account_number=account_number
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposited: ₹",amount)
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawn: ₹",amount)
        else:
            print("Insufficient balance or invalid amount")
    @abstractmethod
    def account_type(self):
        pass
    def display_details(self):
        print("Customer Name:",self.customer_name)
        print("Account Number:",self.account_number)
        print("Account Type:",self.account_type())
        print("Balance: ₹",self.get_balance())
class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"
class CurrentAccount(BankAccount):
    def account_type(self):
        return "Current Account"
class SalaryAccount(BankAccount):
    def account_type(self):
        return "Salary Account"
class FixedDepositAccount(BankAccount):
    def account_type(self):
        return "Fixed Deposit Account"
acc1=SavingsAccount("Ram",301,10000)
acc2=CurrentAccount("Christin",502,20000)
acc3=SalaryAccount("Adam",703,30000)
acc4=FixedDepositAccount("Sneha",904,50000)
print("----- Bank Account Details -----")
acc1.display_details()
print()
acc2.display_details()
print()
acc3.display_details()
print()
acc4.display_details()
print()
print("----- Deposit Money -----")
acc1.deposit(5000)
print("Updated Balance: ₹",acc1.get_balance())
print()
print("----- Withdraw Money -----")
acc1.withdraw(2000)
print("Updated Balance: ₹",acc1.get_balance())
print()
print("----- Polymorphism -----")
accounts=[acc1,acc2,acc3,acc4]
for account in accounts:
    print(
        account.customer_name,
        "-",
        account.account_type(),
        "- Balance: ₹",
        account.get_balance()
    )