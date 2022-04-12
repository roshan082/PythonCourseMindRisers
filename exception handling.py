# Exception Handling
# --> process of handling the errors or exception that are raised during compile time or execution time due to programatical error or syntax error

# 1. try clause
# --> block of code which might raise exceptions are kept


# 2. except clause
# --> handles the raised exceptions from the try clause

# syntax
# try:
#   block of code
# except:
#   exception message


# exception class
'''
NameError
ValueError
KeyError
IndexError
FileNotFoundError
FileNotExistError
SyntaxError
SystemExit
OverflowError
ZeroDivisionError
'''


# example
from audioop import add
from termios import ECHOE
from traceback import print_tb


address = "Sindhuli"
print("address is : ", address)
try:
    print(name)
    print(address)
except:
    print("Must Pass value to name.")
print("Hello World")

# catching specific exception
print(" ")
try:
    print(name)
except NameError:
    print("Must pass value to name")

# catching specific exception and other exception at the same time
print(" ")
try:
    print(100/0)
except NameError:
    print("Must pass value to name.")
except:
    print("Cannot be divisible by zero.")

# catching specific exception with specific error
print(" ")
try:
    print(100/0)
except ZeroDivisionError as error:
    print(error)
except:
    print("Nothing")

# else with try-except

print("")
try:
    name = "Sandesh"
    print(name)
except:
    print("Value not defined")
else:
    print("No exception raised")

# we can also raise exception with raise keyword if we wanted to raise KeyError

# catching multiple specific exception
print(" ")
try:
    items = [1, 2]
    print(items[4])
    print(100/0)
except (ZeroDivisionError, KeyError, IndexError) as error:
    print(error)
except:
    print("Error Occured")

# finally
# --> not matter what happens in try-except clause this cause runs the code of its block

print("")
try:
    file = open("C:\Users\Heisenberg\Desktop\python.txt", "r")
    print(file.read())
except:
    print("File ot Found")
finally:
    try:
        file.close()
        print("File Closed")
    except:
        print("File Not Found")





