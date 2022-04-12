'''
Type casting or type conversion

--> converting into other datatype

    int -> float and vice versa
    int -> str
    float -> str
    str -> int, float - depends



'''

#int
from tokenize import Number


x = int(4)
print(type(x))
print(x)

# int - float
y = float(x)
print(type(y))
print(y)

# list - set
items = ["Box", "Tools", "Board", "Bin"]
print(items)
item_set = set(items)

print(item_set)
print(type(item_set))

# list - dict -- not possible

# item_dict = dict(items)
# print(type(item_dict))

# list - tuple
item_tuple = tuple(items)
print(type(item_tuple))


# str - int

myNumber = "12"
myInteger = int(myNumber)

# str - float
x = "45"
float_num = float(x)
print(float_num)
print(type(float_num))