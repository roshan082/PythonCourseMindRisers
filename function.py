# Function
# to reuse certain block of code for repeatative operation

# rules to follow while declaring function name
# 1. Keywords 
#       -- are not allowed
# 2. Special Character 
#       -- are not allowed except underscore.
# 3. Numbers 
#       -- they are allowed but its better not to use it
# 4. Built-in function are not allowed 

# Camel Case is best to use for defining function name (eg:- myResult )

# syntax
# def -> define keywork is use to define function name in python

# def <function name>():
#   function body

# note :- functions should be invoked or called by its name to perform its operation.



print("--------------------------------------")
print("Short example of function:")
def showMagic():
    print("Wollahhh its a magic......")
showMagic()  # invokeing or calling a function
showMagic()
print("--------------------------------------")


# types of function
# 1. Built-in function -- pre-defined function -- defined by python
#       eg: print(), type(), len(), help(), etc.......
# 2. User-defined function
#       eg: showMagic(), getDetails(), calculateArea()


# Types of User-defined function

# 1. with parameter and no return type
# parameter --> if certain variable are passed in the paranthesis while defining the variable
# eg: 
def myAddress(address, country):
    print(f"Country: {country} , Address: {address}" )
myAddress("Kathmandu", "Nepal")

# 2. with parameter and return type
def areaOfCircle(pi, radius):
    area = pi * radius**2
    # print(f"Area = {area}")
    return area
print("Area Calling: ", areaOfCircle(3.14, 5))

# we can simply store the output inside some variable and display the output
area = areaOfCircle(3.14, 5)
print(area)

print("--------------------------------------")
#argument vs parameter
# parameter -> variable that are passed ehile declaring function
# argument -> values passed inside the variabe while accessing or invoking the function

# 3. without parameter and return type
def getAddressDetail():
    place = "Butwal"
    region = "Terai"
    return f"Palce: {place}. Region: {region}"
print(getAddressDetail())

print("--------------------------------------")

# 4. without parameter and no return type
def sumOfTwoNumber():
    num_one = int(input("Enter a number: "))
    num_two = int(input("Enter a number: "))
    total = float(num_one + num_two)
    if total > 0:
        print(f"Sum of two number is {total}")
    else:
        print(f"Sum is less then zero.")
sumOfTwoNumber()

print("--------------------------------------")

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))

def areaOfCuboid(param_length, param_breadth, param_height):
    area = param_length * param_breadth * param_height
    print(f"Area of Cuboid = {area} cm3")
areaOfCuboid(length, breadth, height)

print("--------------------------------------")

# input inparameter
def areaOfTriangle(base = input("Enter base: "), height = input("Enter height: ")):
    area = (1 / 2) * float(base) * float(height)
    print(f"Area of Triangle = {area} cm2")
areaOfTriangle()
print("--------------------------------------")

def showRiders():
    print("Riders from KTM....")
showRiders()

print("--------------------------------------")
def userLogin(user_email):
    if user_email == "roshansth11@gmail.com":
        print("Matched..")
        return True
    else:
        return False
email =input("Enter your Email address: ")
print(userLogin(email))
