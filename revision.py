# Revision

# 1. Keywords and identifier

    # keywords are predefined words in python

    # indentifier are those who indentifies the nature of the variables. weither they are string, integer, float, boolean, etc.

# 2. Satements & Comments

    # Statement is prase of code which gives information to the program.

    # Comment are those which helps us to write the explaination of code and they donot interfear the program. They are ignored by interpreter

# 3. Variables

    # Variables are those who store information/data so that it can be used in the program.

# example
# string variable

name = "Roshan"
print(f"My name is : {name}")

# integer variable

number = 5
print(f"The number is : {number}")

# float variable

float_number = 4.5
print(f"The Float number is : {float_number}")

# Boolean variable

condition = True
print(f"What is the condition ? \n--> {condition}")


# types of variable 

# 1.  Global variable
# a = 15

# def Main():
#     print(a)

# def End():
#     print(a)

# Main()
# End()

# 2. Local variable

def Start():
    b = 60
    print(f"value of b : {b}")

def End():
    b = 40
    print(f"value of b : {b}")

Start()
End()