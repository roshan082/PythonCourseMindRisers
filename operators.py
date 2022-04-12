'''
Operators
--> Operators are used to perform operations on variables and values.

--> In the example below, we use the + operator to add together two values:

1. Arithmetic Operator
    --> Mathmatics Operations
        - Addition
            -> sum of numbers (int, float, complex number)
            -> eg: result = 15 + 30
            -> str -> if we use + between two string then they are concatinated instead of sum
                    -> eg: numOne = "23"
                            numTwo = "12"
                            print(numOne + numTwo)
                        output : 2312

            -> eg: print("roshan"+ "Shrestha")
                    float_add = 2.1 + 5.2
                    complex_add = (15 + 22j) + (45 + 22j)
            
        - Subtraction
            -> subtrac of numbers (int, float, complex number)
            -> eg: result = 15 - 30
                    float_minus = 5.1 - 6.3
                    complex_minus = (15 + 22j) - (45 + 22j)

        - Multiplication
            -> multiplication of numbers (int, float, complex number)
            -> eg: result = 15 * 30
                    float_multiply = 2.1 * 2.1
                    complex_multiply = (15 + 22j) * (45 + 22j)

        - Division ( / )
            -> division of numbers (int, float, complex number)
            -> eg: result = 15 / 30
                    float_division = 2.1 / 2.1
                    complex_multiply = (15 + 22j) / (45 + 22j)

        - Floor Division ( // )
            -> returns the riminder value while dividing two numbers.
            -> eg: numOne = 5
                    numTwo = 37
                    resultFloorDivision(numOne // numTwo)

        - Exponential ( ** )
            -> to to the power
            -> x = 5
                y = 6
                result = ( x ** y ) 

        - Modulas ( % )
            -> eg: numOne = 5
                    numTwo = 37
                    resultModulas = numTwo%numOne
2. Assignment Operator
    --> ( = ) --> equals to
        eg: num = 45
            num += 45
            print(num)

    --> ( += ) --> equals to sum
        eg: num = 45
            num -= 45
            print(num)
    --> ( -= ) --> equals to subtract
    --> ( *= ) --> equals to multiplication
    --> ( /= ) --> equals to division
    --> ( //= ) --> equals to floor division
    --> ( %= ) --> equals to modulas
    --> ( **= ) --> equals to exponential

3. Logical Operator
    --> and, or, not
    - and -> if there are two or more condition then all conditions must be true
    - or -> if any of the condition is true returns true or operate the instruction
    - not -> if we want to make the true condition false then we use not infront o the condition and vice versa.

    eg: name = "Nepal"
        capital = "Kathmandu"
        # and
        print(name == "India" and capital == "Delhi")
        
        # or
        print(name == "India" or capital == "Delhi")
        
        # not
        print(not name == "India" and capital == "Delhi")
        print(not name == "India" or capital == "Delhi")
        print(not name == "Nepal" and capital == "Kathmadnu")


4. Comparative Operator

    ==   -->  is equals to
    !=   -->  is not equals to
    <   -->  is less then
    >   -->  is greater then
    <=   -->  is less or equals to (=< nowadays this doesn't work)
    >=   -->  is greater or equals to (=> nowadays this doesn't work)


5. Identity Operator
    --> to check the identical value of the variable or object
    --> is , is not
    --> it doesn't work with iterative objects.

    eg; nameOne = "Hello"
        nameTwo = "hello"
        nameThree = "Hello"

        print(nameOne is nameTwo)
        print(nameOne is nameThree)


6. Membership Operator
    --> in, not in
    --> eg: places = ["Pokhara", "Kathmandu", "Hile", "Okhalghunga"]
    even_set = {2, 4, 6, 8, 10}
    gender = ("male", "Female", "Others")

7. Bitwise Operator 



'''
print(5 -8)
# Arithmetic Operators
# complex add
complex_add = (15 + 22j) + (45 + 22j)
print(complex_add)

# complex subtract
complex_minus = (15 + 22j) - (45 + 22j)
print(complex_minus)

# complex multiply
complex_multiply = (15 + 22j) * (45 + 22j)
print(complex_multiply)

# complex division
complex_division = (15 + 22j) / (3 + 2j) # point to be noted
print("division:",complex_division)  # using division in complex number is not prefered... it doesn't give accurate answer....

# add string
numOne = "23"
numTwo = "12"
print(numOne + numTwo)

# Floor Division
numOne = 5
numTwo = 37
resultFloorDivision = ( numTwo // numOne)
print(resultFloorDivision)

# Modulas
numOne = 5
numTwo = 37
resultModulas = numTwo%numOne
print(resultModulas)


# Exponential
x = 5
y = 6
print( x ** y )

# 2. Assignment Operator
    # (=)
num = 45
num += 45
print(num)

    # (-)
num = 45
num -= 5
print(num)

# Logical Operator
name = "Nepal"
capital = "Kathmandu"

# and
print(name == "India" and capital == "Delhi")
print(name == "Nepal" and capital == "Kathmandu")

# or
print(name == "Nepal" or capital == "Kathmandu")

#not
print(not name == "India")


# 3. Comparative operator
name = "KTM"
num = 45
print("equals to", name == "PKR")
print("not equals to", name != "PKR")
print("less then", num < 44.55)
print("grater then", num > 44.55)
print("les or equals to", num <= 44.55)
print("greater or equals to", num >= 44.55)

items = ["Sandle", "Lipstick", "Hand Bag",]
print("not equals to", items[0] !="Sandle")
print("not equals to", items[1] !="Eye Lasher")

set_even = (2, 4, 6, 8)
print("less then", set_even[2] < 3)
print("greater then", set_even[2] > 3)
# print("less or equals to", set_even[5] <= 34) # this gives IndexError if index is out of range


# 4. identity operator
nameOne = "Hello"
nameTwo = "hello"
nameThree = "Hello"
print("identity operator")
print(nameOne is nameTwo)
print(nameOne is nameThree)
print("is not")
print(nameOne is not nameTwo)
print(nameOne is not nameThree)

# case iterative objects - list, set, tuple, and dict
print("lists results for iterative objects")
orderedItems = ["Hand Bag", "Lipstick", "Nail Polish"]
orderedPlaced = ["Hand Bag", "Lipstick", "Nail Polish"]

print(orderedItems is orderedPlaced)
print(orderedItems is not orderedPlaced)


print("check by index")
print(orderedItems[0] is "Hand Bag")
print(orderedItems[1] is "Lipstick")


print(orderedItems[0] is orderedPlaced[1])
print(orderedItems[1] is orderedPlaced[0])



# Iterative Objects
# identity does't work on iterative objects

x = [1, 2, 3]
y = [1, 2, 3]

print("iterative:", x is not y)

# but if we check wirh index it works
print("iterative:", x[0] is y[0])

# items = {"box", "tools", "tables"}
# furniture = {"box", "tools", "tables"}
# print("box: ", items[0] is furniture[0])



places = ["Pokhara", "Kathmandu", "Hile", "Okhalghunga"]
even_set = {2, 4, 6, 8, 10}
gender = ("male", "Female", "Others")


print("in example: ","Hile" in places)
print("in example: ","Biratnager" in places)
print("not in example: ","Hile" not in places)
print("not in example: ","Biratnager" not in places)

print("in example: ",2 in even_set)
print("in example: ",3 in even_set)
print("not in example: ",2 not in even_set)
print("not in example: ",3 not in even_set)

print("in example: ","Male" in gender)
print("in example: ","trans" in gender)
print("not in example: ","Male" not in gender)
print("not in example: ","Male" not in gender)

# dict - it check key as variable/member not value
# dict syntax
# variableName = {"Key: Value} --> interger
# variableName = {"Key: "Value"} --> string


item_details = {"id": 12, "name": "Muna", "address": "Birtamode"}
print (" ")
print("id" in item_details)
print(12 in item_details) # 12 is value in variable that is why it prints flase.

print("id" not in item_details)
print(12 not in item_details)

print("name" in item_details)
print("Muna" in item_details)
print("name" not in item_details)
print("Muna" not in item_details)


# Bitwise Operator
# to manipulate the binary digit in the memory

# &  -->  AND 
    # --> returns 1 if both value  are 1
print(10&7)
# |  -->  OR
    # --> returns 0 if one of the bits vaue is 1 or 0.
print(10|7)
# ^  -->  X-OR
print(10^7)
# ~  -->  NOT
# print(10~7)

# << -->  Right Shift
print(10 << 2)
# >> -->  Left Shift
print(10 >> 2)
