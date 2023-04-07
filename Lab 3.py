# Question 1
n = int(input("Enter a number: "))
if n == 0:
    print("The number is zero.")
else:
    print("The number is nonzero.")

# Question 2
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print(a, "is the largest number.")
else:
    print(b, "is the largest number.")

# Question 3
num = float(input("Enter a number: "))

if num > 0:
    print(num, "is a positive number.")
elif num == 0:
    print("The number is zero.")
else:
    print(num, "is a negative number.")

# Question 4
ch = input("Enter a character: ")

if ch in 'aeiouAEIOU':
    print(ch, "is a vowel.")
else:
    print(ch, "is a consonant.")

  

# Question 5
grade = float(input("Enter your grade: "))

if grade >= 90:
    print("Excellent performance")
elif grade >= 80:
    print("Very Good performance")
elif grade >= 70:
    print("Good performance")
elif grade >= 60:
    print("Average performance")
else:
    print("Poor performance")

# Question 6
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
z = float(input("Enter the third number: "))

if x >= y and x >= z:
    print(x, "is the largest number.")
elif y >= x and y >= z:
    print(y, "is the largest number.")
else:
    print(z, "is the largest number.")

# Question 7
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
num3 = eval(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3:
    print(num1, "is the smallest number.")
elif num2 <= num1 and num2 <= num3:
    print(num2, "is the smallest number.")
else:
    print(num3, "is the smallest number.")

# Question 8
input_num = int(input("Enter a number: "))

if input_num > 0:
    if input_num % 2 == 0:
        print(input_num, "is positive and even.")
    else:
        print(input_num, "is positive and odd.")
elif input_num < 0:
    if input_num % 2 == 0:
        print(input_num, "is negative and even.")
    else:
        print(input_num, "is negative and odd.")
else:
    print(input_num, "is zero.")

# Question 9
marital_status = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if marital_status == "married":
    print("The driver is insured.")
elif marital_status == "unmarried":
    if gender == "male" and age > 30:
        print("The driver is insured.")
    elif gender == "female" and age > 25:
        print("The driver is insured.")
    else:
        print("The driver is not insured.")
else:
    print("Invalid marital status.")

# Question 10
marital_status = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")

try:
    age = int(input("Enter age: "))
    if marital_status == "married":
        print("The driver is insured.")
    elif marital_status == "unmarried":
        if gender == "male" and age > 30:
            print("The driver is insured.")
        elif gender == "female" and age > 25:
            print("The driver is insured.")
        else:
            print("The driver is not insured.")
    else:
        print("Invalid marital status.")
except ValueError:
    print("Age must be integer")
