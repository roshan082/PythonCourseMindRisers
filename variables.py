''' 
--> Variables are piece or chunk of memory whose value can be change during time of execution.
example --> x = 15
            print(x)

--> variable declaration and variable initialization
    # x, y, z --> this is variable declaration
    # x, y, z = 12, 13, 14 --> this is variable initialization

Python Syntax
--> indentation - one (tab) or 4 (spaces)
--> define boundary in python:  def getDetails():   # def --> defination of function in python
                                    print(x)
                                    abc = 123
                                    print(abc)
                                    print("Hello World")
                                print(x)
                                print(abc) # throws error because abc is not defined. abc is defined inside a function.

--> Types of Variable --> We can differentiate variables on the basis of their scope.
1. Local Variable
    --> local variable is a variable which is defined inside a function.
    --> example:
    def getDetails():
        y = 11 #y is local variable 
        print(y)


2. Global Variable
    --> global variable is a variable which is defined outside a function and called inside a function
    --> we can define global variable with the use of global keyword.
    --> note: we cannot assign value to global variable while declaring
    --> example:
        global a 

        def showValue():
            a = 12
            print(a)
        def showSecoundValue():
            a = 35
            print(a)

3. Constant Variable
    --> those variable whose value cannot be change is called constant variable.
    --> Example: NAME = "Kathmandu"
                 PI = 3.14

                 print(NAME)
                 print(PI)


Garbage Collection -- release all the unused and unnecesary variables and objects.

--> Rules to follow while defining variable
1. Case Sensitive
    name = "Roshan"
    Name = "Roshan"
these are different variable due to ASCII value

2. Keywords are not allowed to use as variables

3. No white-spaces between two words.
    name of the place = "Kathmandu" --this is wrong, throws error
    name_of_the_place = "Kathmandu" -- this is correct

4. No use of special characters(@, #, -,... ) except underscore
    but it is not allowed in leading and trailing pr before and after variable naame (__name__) 

5. Numbers can be used but only after alphabetical letter
    example: num1, num
    but you can use (num_one, num_two) for better conding convention

6. Naming Convention
    - Sanke Case --> name_of_place - follow while nameing variables
    - Pascal Case --> NameOfPalce - follow while defining class name
    - Camel Case --> nameOfPlace - follow while defining function

 '''
##########################################################################################################################################

# from math import pi

# radius = 1.1
# area = pi * radius * radius
# print(f"The area of circle is: {area}. And the radius of the circle is: {radius}")


# employee_id = 1
# employee_name = "Roshan Shrestha"
# employee_address = "Kathmandu"
# employee_contact = 9860895652
# employee_fathername = "Raju Shrestha"
# print("Employee Full Name :", employee_name)

# print("This employee name is", employee_name, ".His home is in", employee_address, ".According to our company his id is", employee_id, ".His father name is", employee_fathername)

# print(f"This employee name is {employee_name}. His home is in {employee_address}. According to our company his id is {employee_id}. His father name is {employee_fathername}.")





a = 12

def showValue():
    print(a)
def showSecoundValue():
    secondValue = a - 5
    print(secondValue)

showValue()
showSecoundValue()
