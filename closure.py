# Closure

# nonlocal

from ctypes.wintypes import PINT


def showHello():
    name = "Hello"
    def inner():
        nonlocal name  # this will replace the value of name of above variable name = "Hello" to "Delta"
        name = "Delta"
        return name
    inner()
    return name

print(showHello())
name = "Kathmandu"
def itsNoramal():
    name = "Palpa"
    return name
print(itsNoramal())


# closure

def print_msg(msg):
    # this is a enclosing function
    def printer():
        # this is a nested function
        print(msg)
    return printer

quote = print_msg("Have a nice day.")
quote()

# here print_msg() function is a enclosing function which was already executed but still quote() the refrenced function to the inner function printer() bound with the retirned output still remembers the message output from the inner function printer() on calling the function came quote()

# this type of technique where data are attached to the object is called closure in python

print(print_msg("Hello"))

del print_msg
try:
    print(print_msg("Hello"))
except:
    print("No function available.")

quote()

# Note:- To have a closure
# 1. must have a enclosing function
# 2. must have nested function
# 3. nested function must refer to the variable/properties of enclosing function
# 4. enclosing function must return nested function 
