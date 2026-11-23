#variables,data types and type conversion
#student information
name = "Rahul"
age = "22"
marks = "85.5"
course = "Python"
# Check data types
print(type(name))
print(type(age))
print(type(marks))
print(type(course))
# Type conversion
age = int(age)
marks = float(marks)
# Display student details
print("Student Name:", name)
print("Student Age:", age)
print("Student Marks:", marks)
print("Student Course:", course)
# Display converted data types
print(type(age))
print(type(marks))

#I/O and operators
#age calculator
ame = input("Enter your name: ")
age = int(input("Enter your age: "))
next_year_age = age + 1
print("\nHello", name)
print("Your current age:", age)
print("Your age next year:", next_year_age)
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#conditional statements and loops
#number guessing game
secret_number = 7
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break     
    elif guess < secret_number:
        print("Too low! Try again.")   
    else:
        print("Too high! Try again.")

#reusable functions/methods and practice collections/arrays
#student score calculator
def get_marks():
    marks = []
    for i in range(5):
        mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
        marks.append(mark)
    return marks
# Function to calculate total marks
def calculate_total(marks):
    total = sum(marks)
    return total
# Function to calculate average
def calculate_average(marks):
    average = sum(marks) / len(marks)
    return average
#python program
print("Student Marks Management")
student_marks = get_marks()
total = calculate_total(student_marks)
average = calculate_average(student_marks)
print("Subject Marks:", student_marks)
print("Total Marks:", total)
print("Average Marks:", average)
if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")

#create dictionary
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Hyderabad"
}
# Adding a new key-value pair
student["course"] = "Python"
# Updating an existing value
student["age"] = 23
print(student)

#combination of functions,lists,dictionaries
#student score details
students = []
def add_student(name, marks):
    student = {
        "name": name,
        "marks": marks
    }
    students.append(student)
def display_students():
    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])
def calculate_average():
    if not students:
        return 0
    total = 0
    for student in students:
        total += student["marks"]
    return total / len(students)
add_student("Rahul", 85)
add_student("Priya", 90)
add_student("Amit", 75)
display_students()
print("Average Marks:", calculate_average())

#loop through list
students = ["Rahul", "Priya", "Amit"]
for student in students:
    print(student)

#store location in tuple
location = (17.3850, 78.4867)
print("Latitude:", location[0])
print("Longitude:", location[1])

#list methods
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)

#set methods
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.discard(50)
print(numbers)

#dictionary methods
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Hyderabad"
}
print(student.keys())
print(student.values())
print(student.items())

#array operations
import array
numbers = array.array('i', [10, 20, 30])
numbers.append(40)
print(numbers)
numbers.insert(1, 15)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.pop()
print(numbers)
