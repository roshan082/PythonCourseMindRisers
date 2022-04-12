'''
    Flow Control
-->  to control the flow of the program.
1. if statement

--> single condition or statement syntax.
    if condition:
        expression or block of code
eg:
name = "Kathmandu"
if name is "Kathmandu":
    print("true")

2. if else statement
syntax:


3. if elif statement (else if --in other language)
4. nested if statement (if inside if statement)
-- switch case statement
    --> there is no switch case statement in python


'''
# if statement


name = "Kathmandu"
if name is "Kathmandu": # sometimes is operator does't work and gives us warning. for solving this warning we can use ==
    print("true", name)

# if else statement
day = "Sunday"

if "din" in day:
    print("Found")
else:
    print("Please try again")

# using identity operator
days = "5"
print("flowcontrol")
if days == str(5):
    print("True")
else:
    print("False")


# using logical operator
if "sday" not in day and "day" in day:
    print("Found")
else:
    print("try again")


#  if elif statement
# if we need multiple if statement we can use elif
obtainedMarks = int(input("Enter your Marks:"))
if obtainedMarks >= 0 and obtainedMarks < 39.99:
    print("Fail")
elif obtainedMarks >= 40 and obtainedMarks < 59.99:
    print("Second Division")
elif obtainedMarks >= 60 and obtainedMarks < 79.99:
    print("First Divison")
elif obtainedMarks >=80 and obtainedMarks <= 100:
    print("Distinction")
else:
    print("Absent")


#  nested if statement
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")



items = ["Books", "Bag", "Laptops", "Desktop"]
inputItems = input("Enter Items: ")
if inputItems in items:
    print(inputItems, "Available")
elif inputItems in items:
    print(inputItems, "Also available")
elif inputItems in items:
    print(inputItems, "Also available")
else:
    print(inputItems, "Not available")


# simple emai and password check
phoneNumber = input("Enter your valid Number: ")
# emailAddress = input("Enter your Email Address: ")


if phoneNumber == "9860895073":
    otp = 987452
    print("Correct Phone Number")
    otpInput = int(input("Enter a valid OTP sent on your number:"))
    if otp == otpInput:
        password = input("Enter your password: ")
        if password == "pass123":
            print("Login Successfull")
        else:
            print("Enter correct password")
    else:
        print("Wrong OTP. Re-Inter OTP.")
else:
    print("Phone number is not yet registered...")

# example 2
fruits = ["Banana", "Apple", "Mango"]
fruit = input("Enter fruit name: ")
if fruit in fruits:
    if "A" in fruit:
        print("A for ", fruit)
    else:
        print("Noting")
elif fruit in fruits:
    if "B" in fruit:
        print("B for ", fruit)
    else:
        print("Noting")
else:
    print("please enter proper fruit name. ")



# task
# use if statement, modulas to check prime number

