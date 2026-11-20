#input and output in python
#print statement
name="Siri"
age=25
print(name)
print(age)
print("Hello Python")

#user input
name=input("Enter your name:")
print("welcome",name)

#type conversion
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a + b)

#operators in python
#arithmetic operators
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#logical operators
age = 25
salary = 30000
print(age >= 18 and salary >= 20000)
print(age >= 18 or salary >= 50000)
print(not(age >= 18))

#assignment operators
a = 10
a += 5
print(a)
a *= 2
print(a)

#membership operators
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)
print("orange" not in fruits)

#identity operators
a = [10, 20]
b = a
c = [10, 20]
print(a is b)
print(a is c)
print(a == c)

#bitwise operators
a = 5
b = 3
print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)