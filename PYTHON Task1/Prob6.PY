#functions in python
#create a function
def greet():
    print("Hello, Welcome to Python!")
greet()

#function with parameters
def add(a, b):
    print("Addition:", a + b)
add(10, 20)
add(50, 30)

#function with return statement
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)

#function with default parameter
def student(name, age=20):
    print("Name:", name)
    print("Age:", age)
student("Rahul")
student("Priya", 22)

#keywords arguments
def employee(name, salary):
    print(name, salary)
employee(salary=30000, name="John")

#variable length arguments
def total(*numbers):
    print(sum(numbers))
total(10, 20)
total(10, 20, 30, 40)

#methods in python
#user-defined method
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
obj = Calculator()
print(obj.add(10, 20))
print(obj.subtract(20, 5))

#list in python
#creating a list
numbers = [10, 20, 30, 40, 50]
print(numbers)
#accessing list elements
numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[2])
print(numbers[-1])

#tuple in python
#creating a tuple
numbers = (10, 20, 30, 40)
print(numbers)
print(numbers[0])
print(numbers[2])
#tuple methods
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
print(numbers.index(30))

#set in python
#creating a set
numbers = {10, 20, 30, 40, 50}
print(numbers)
#accessing set elements
numbers = {10, 20, 30, 40, 50}
for n in numbers:
    print(n)

#dictionary in python
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Hyderabad"
}
print(student)
print(student["name"])
print(student["age"])
#loop through dictionary
for key, value in student.items():
    print(key, ":", value)

#arrays in python
import array
numbers = array.array('i', [10, 20, 30, 40])
print(numbers)
print(numbers[0])
