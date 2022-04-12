

from audioop import mul
from unicodedata import name


print("----------------------> Program 1 <----------------------")

# fname = input("Enter your First name: ")
# lname = input("Enter your Last name: ")
# print(f"Hello {fname.capitalize()} {lname.capitalize()}.")

print("----------------------> Program 2 <----------------------")

# num_one = float(input("Enter a number: "))
# num_two = float(input("Enter a number: "))

# print(f"Sum of given numbers is: {num_one + num_two}.")

print("----------------------> Program 3 <----------------------")

# import math

# enter_number = int(input("Enter a number: "))
# square_root = enter_number ** 0.5
# math.sqrt(enter_number)
# print(square_root)


print("----------------------> Program 4 <----------------------")

# base = input("Enter base of triangle: ")
# height = input("Enter height of triangle: ")
# area_of_triangle = (1/2) * float(base) * float(height)
# print(f"Area of Triangle is : {area_of_triangle}")


print("----------------------> Program 5 <----------------------")
# swap two variable

# x = input("Enter a number for x: ")
# y = input("Enter a number for y: ")

# swap_num = x
# x = y
# y = swap_num
# swap_num_x = y
# swap_num_y = x

# print(f"The value of x after swaping {swap_num_x}")
# print(f"The value of y after swaping {swap_num_y}")

print("----------------------> Program 6 <----------------------")

# display random numbers

# import random

# random_numbers = random.randint(1, 10)
# print(f"Random number is : {random_numbers}")


print("----------------------> Program 7 <----------------------")
# convert kilometer to miles

# distance_in_km = float(input("Enter distance in Kilometer : "))
# distance_in_mile = distance_in_km * 0.62
# print(f"{distance_in_km} km = {distance_in_mile} mile's")

print("----------------------> Program 8 <----------------------")
# convert celsius to fahrenheit

# temp_celsius = input("Enter Temperature in Celsius: ")
# temp_fahrenheit = float((float(temp_celsius) * (9/5)) + 32)
# print(f"{temp_celsius} °C = {temp_fahrenheit} °F")


print("----------------------> Program 9 <----------------------")

# check_number = float(input("Enter a number: "))
# if check_number == 0:
#     print(f"{check_number} is Zero.")
# if check_number > 0:
#     print(f"{check_number} is positive number.")
# if check_number < 0:
#     print(f"{check_number} is negative number.")

print("----------------------> Program 10 <---------------------")

# check number is odd or even

# check_number = float(input("Enter a number: "))
# if check_number%2 == 0:
#     print(f"{check_number} is even.")
# else:    
#     print(f"{check_number} is odd.")

print("----------------------> Program 11 <---------------------")

# find largest number amoung given three numbers

# num_one = float(input("Enter a First number: "))
# num_two = float(input("Enter a Second number: "))
# num_three = float(input("Enter a Third number: "))

# if (num_one >= num_two) and (num_one >= num_three):
#     print(f"{num_one} is greater then {num_two} and {num_three}")
# elif (num_two >= num_one) and (num_two >= num_three):
#     print(f"{num_two} is greater then {num_one} and {num_three}")
# else:
#     print(f"{num_three} is greater then {num_one} and {num_two}")

print("----------------------> Program 12 <---------------------")

# Check prime number

# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not valid to check for prime number.")



print("----------------------> Program 13 <---------------------")

# print prime numbers in an given intervals

# interval_from = int(input("Enter a number: "))
# interval_to = int(input("Enter a number: "))

# print(f"Prime Numbers between {interval_from} to {interval_to} are :")

# for num in range(interval_from, interval_to):
    # all prime numbers are greater than 1
    # if num > 1:
    #     # to check prime number first we start dividing with 2.
    #     for i in range(2, num):
    #         if num % i == 0:
    #             break
    #     else:
    #         print(num)
    # else:
    #     print("""Warning:
    #     To check a Prime Number.
    #     Number should be positive and greater than 1.
    #     Please Try again with correct numbers.
    #     """)
    #     break


print("----------------------> Program 14 <---------------------")

# find a factorial of a number

# num = int(input("Enter a number: "))

# print(f"Factorial Numbers of {num} are: ")
# if num < 0 :
#     print("Sorry, Factorial does not exist for negative numbers.")
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)


print("----------------------> Program 15 <---------------------")

# display multiplication table of numbers given by user
# user_numbers = input("Enter a number: ")
# print("Multiplication table of", user_numbers, "is: ")
# print("")
# for i in range(1, 11):
#     table = int(user_numbers) * i
    
#     print(f"{user_numbers} X {i} = {table}")

print("----------------------> Program 16 <---------------------")

# make a calculator

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

# def mode(mode_numb):
#     print("""
#     Choose Mode:
#     1. Add
#     2. Substract
#     3. Multiply
#     4.Divide
#     """)
#     mode_numb = input("Enter Mode 1 / 2 / 3 / 4 :")
#     return mode_numb
    
# def calc(mode_numb, x, y):
#     mode(mode_numb)
#     if mode(mode_numb) == 1:
#         print(add(x, y))
#     elif mode(mode_numb) == 2:
#         print(subtract(x,y))
#     elif mode(mode_numb) == 3:
#         print(multiply(x, y))
#     elif mode(mode_numb) == 4:
#         print(divide(x, y))
#     else:
#         print("Enter a valid number....


# set_1 = {1, 2, 3, 4, 4, 3}
# print(set_1)
# print(type(set_1))
