'''
Data Types
    --> Defines the nature of data or variables
1. Numbers
    a. Whole Number - int (integer)
    --> i.e whole number 0-9
    --> tinyint (3-4), int (11), bigint (20) -> (these are range of integers) !important

    b. Decimal Number - float (double)
    --> y = 45.256161
        print(type(y))

    c. Imaginary or Real Number - complex (X + Yi) see yourself.
    --> complex() -> takes two arguments 1. real number 2. imaginary number

    result = complex(x, y)
    print(result)
    print(type(result))

    --> we can sum two or more complex numbers

    complex_num_one = 22 + 78j
    complex_num_two = 33 + 22j
    result = complex_num_one + complex_num_two
    print(result)
    --> syntax:
        rn = 23  real number
        imn = 34  imaginary number
        result = complex(rn, imn)
        print(complex(rn, imn))
    --> to access real and imaginary part of the complex number
    - imaginary
        print(result.imag)
    - real
        print(result.real)
        result2 = 22 +25j
        -- when we sum two complex number
        -- real number is added with real number and imaginary with imaginary
        print(result + result2)

2. Text form or alphabetical letter or characters string repredented as (str)
    --> collection of sequences of unicode characters
    --> it can written as 2 types:
        - single quotation ' '
            name = 'Kathmandu'
        - double quatation " "
            name1 = "Kathmandu"
    --> String character can also be printed with index
        - print(name[0]) --> displays first character of variable name
        - print(name[1]) --> displays second character of variable name
    --> String Concatinate
        - use (+) sign to concatinate string
        FullName = Fname + Lname
        --> Note: 
            - if we want to concatinate int or float with string then first we have to convert then to string with (str()) method.
            - in case of string values are concatinate but in case of int and float values sum to each other
    --> Array
     - Collection of similar type of data.
     - Python don't have array instead it has annother datatype i.e list

3. List/ Array
    --> Collection of similar or different data
    --> list are mutable
    --> list are iterative object
    --> Syntax
        varname = list() --> to define empty list
        varname = ["item1", "item2", "item3,...."item n"] 
        - these both are correct syntax to define list in python
    --> Example
        - int
            even_number = [2, 4 , 6 , 8 , 10]
        - str
            names = list(("Roshan","Unish","Manish"))
        - all in one
            items_list = [12, "Biscuits", 45.33]
    --> we can call list item via index number as well
        print(names[0])
        print(names[1])
    --> list inside list
        print (["id", ["Hello", "HOW","Are"], "Morning"])
    
    --> int and float are non iterative object whereas  list, str, tuple, dict are iterative object
    
    --> int, float, tuple, str(depends) are immutable object whereas  dict, list, set are mutable object
    
    --> str - are immutable when they are declared and initialized
    
    --> mutable - changeable and can be altered or updated
    
    --> immutable - non-changeable and cannot be altered or updated
4. Tuple
    --> same as list but mostly we keep collection of constant limited data but are immuteable.
    --> Syntax
        variable_name = tuple()
            - list_orders = ("item1", "item2")
            - list_orders = "item1", "item2"
        example
            gender, days, months, country code, etc
            gender = ("Female", "Male", "Transgender", "Others")
            print(type(gender))
    --> question
        first_day = "Sunday", --> Tuple
        second_day = "Monday" --> String
        third_day = ("Sunday") --> String
        last_day = ("Saturday",) --> Tuple
5. dict
--> same as list but data structure is bit different because it stores data as key-value pair

--> syntax
    varname = {'key': 'value'}
    varname = {"key": "value"}

--> example
    order_details = {'id': 1, "odrcode': 'odr-01', 'price': 200, 'item': 'phone-case'}

6. set
--> same as list but are unordered and store unique items

--> syntax
    varname = {"item1", "item2",...,"item n"}

--> example
    set_even = {2, 4, 6, 8, 10}

--> duplicate
    set_name = {"KTM", "KTM", "KTM", "PKR", "DRN", "PKR"}

7. range

--> range(end) -> equivalent to range(0, end)
    -> eg: range(10)
    output: gives number from 0 to 9
--> range(start, end)
    -> eg: range(0, 10)
--> range(strat, end, step)
    -> eg: range(0, 10, 5)

'''

# a. whole numbers / int
from array import array
from dataclasses import replace
from hashlib import new


x = 45
print(x)
print(type(x))

# b. decimal numbers / float
num = 12.31
print(num)
print("Type of this number is: ",type(num))

# c. complex numbers (real numbers and imaginary numbers)

complex_num_one = 22 + 78j
complex_num_two = 33 + 22j
result = complex_num_one + complex_num_two
print(result)


# string / str()

latter_a = 'a'
name = "Kathmandu"
print(type(latter_a))
print(type(name))

print("Old name:", name.replace("Ka","Ca"))
new_name = name.replace("Ka", "Ca")
print("New Variable:", new_name)
print("Old Name: ", name)


# array
#syntax example
# int
int_list = [2, 4 , 6 , 8 , 10]
print(type(int_list))
print(int_list)

# float
float_list = [2.22, 4.45 , 6.46 , 8.464 , 10.121]
print(type(float_list))
print(float_list)

#string
str_list = ["roshan", "mohan" , "ram" , 'shyam' , 'hari']
print(type(str_list))
print(str_list)

#all in one
all_in_one_list = [1, "mohan" , 5.016, 'shyam' , 'hari']
print(type(all_in_one_list))
print(all_in_one_list)


# tuple

gender = ('male', 'female')
print(type(gender))

#complex number
rn = 23
imn = 34
result = complex(rn, imn)
print(complex(rn, imn))

print(result.imag)
print(result.real)
result2 = 22 +25j
print(result + result2)

# dict

order_details = {'id': 1, 'odrcode': 'odr-01', 'price': 200, 'item': 'phone case'}
print(order_details)
print(type(order_details))

# set
set_even = {2, 4, 6, 10, 8, 12, 6}
print(type(set_even))
print(set_even)

# \ this sign is line continuation
set_name = {"KTM", "KTM", "KTM", "PKR", "DRN", "PKR"}
print(type(set_name))
print(set_name)

#range 

print(*range(10))

print(*range(2, 24))

print(*range(0, 10, 3))


value = 5.36343
rounded_value = round(value, 2) # 5.34
print(rounded_value)