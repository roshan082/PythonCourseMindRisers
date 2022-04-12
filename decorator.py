# Decorator
# --> Takes function as an arrgument, process and return the function
# --> adds additional functionality to the ordinary function

# 1. Must take function as parameter
# 2. Must define a nested inner function
# 3. Return inner function
#
# nested function --> function inside a function 
#  example
from logging.config import valid_ident
from unicodedata import name


def decorator_me(func):
    def inner():
        print("This is a decorator..")
        func()
        # print(func())  *same as above 
    return inner

# ordinary function
def ordinary():
    print("I am a ordinary function.")

# decorating ordinary function
demo = decorator_me(ordinary)
demo()

# here decorate_me is a decorator for function ordinary() which is decorating the function with inner() function and return the inner() function. the return output is referenced to a demo() function which is a function object of decorate_me()

# we can use @ symbol before the decorator function and place it above the ordinary function

# making decorator with annotation

@decorator_me
@decorator_me
@decorator_me

def i_am_ordinary():
    print("I am a Ordinary Function.......")

i_am_ordinary()
# power
def powerDecorator(func):
    list_of_typles = [(1,2), (3,4), (5,6)]
    def inner_func(lists):
        print("Inner function and its decoratoring")
        return [func(val[0], val[1]) for val in lists]
    return inner_func(list_of_typles)

# ordinary function
@powerDecorator
def powerOf(num, power):
    return num**power
print(powerOf)

# chaining decorator
def decorator_one(func):
    def inner_one():
        print("I am decorator one")
        func()
    return inner_one

def decorator_two(func):
    def inner_two():
        print("I am decorator two")
        func()
    return inner_two

def decorator_three(func):
    def inner_three():
        print("I am decorator two")
        func()
    return inner_three

# making ordainary function
@decorator_one
@decorator_two
@decorator_three

def show_func():
    print("This is a show function")

show_func()

# nonlocal variable 
#--> variable without scope global or local

def my_decorator(func):
    num = "Local"
    def inner(num):
        nonlocal num
        num = "Inner Local"
        print(num)
        func()
    return inner

@my_decorator
def test():
    print("Testing")
test()