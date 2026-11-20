#conditional statements
#if statement
age = 20
if age >= 18:
    print("Eligible to vote")

#if-else statement
num = 9
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#if-elif-else statement
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#nested if statement
age = 25
salary = 30000
if age >= 18:
    if salary >= 20000:
        print("Eligible for loan")
    else:
        print("Salary is too low")
else:
    print("Age is not eligible")

#short-hand if-else statement
age = 16
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)

#loops in python
#for loop
for i in range(1, 6):
    print(i)

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1

#break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

#continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#pass statement
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

#nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)