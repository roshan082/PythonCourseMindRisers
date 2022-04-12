# Class and Object

# Class
    #  --> blue print of object 
    #  --> class define the state of the object

# Object
    # --> Car, House, Dog , Table, etc 
    # --> instance of class and simply a collection of data/attributes (variables) and methods (functions) which is derived from a class thats why object is a instance of class

# syntax
# class ClassName(): --> Noun
#   attributes
        # --> characters --> Adjective

#   methods
        # --> behaviour --> Verb


# Naming rules for declaring class name or attributes
# 1. Keywords are not allowed
# 2. Special characters are not allowed except underscore ( _ )
# 3. No white space between two or more combine name class
# 4. Class name should not be repeated
# 5. Class name should be singular
# 6. First letter should be in uppercase 

# Trick for naming convention
# Class Name -> Pascal Case i.e: AddressDetail
# Attributes/Variables -> snake case i.e: name_of_address
# Methods -> CamelCase i.e: showAddress()


# creating class named as Person


class Person:
    # attributes
    name = "Roshan"
    contact = "9860895073"
    email = "roshansth11@gmail.com"
    # methods
    def showDetails(self):
        print(f"Details : , Name : {self.name}, Contact : {self.contact}, Email : {self.email}")
# self --> keyword that is use to indicate the attributes and methods belong to that specific class they are declared or defined 

# creation of object
    # object_name = ClassName()
# accessing attributes and method with object creation
person_one = Person()
print(person_one.name)
person_one.showDetails()

# accessing attributes and methods with class name
print(Person.name)
# print(Person.showDetails)

# function vs method

# function -> free agent, is called by its name and can be define anywhere and is callable anywhere

# method -> it is bind within the class and object and is callable via object or class only

# Constructor --> special type of function which builds or creates objects
# attributes are initialized inside constructor

# if we do not define any constructor inside class inside class then default constructor is created by the interpreter

# __init__() --> this method is use to define constructor

# constructor example
# example 1

class Robot:
    # attributes
    varsion = ""
    model = ""
    specification = ""

    # Constructor
    def __init__(self):
        self.version = "4.1.1"
        self.model = "Vyakur"
        self.specification = "Imba Model"
    
    # method
    def getRobotModel(self):
        print(self.model)

r1 = Robot()
print(r1.version)
r1.getRobotModel()

# we can also assign value to attributes of class

r1.version = "5.0.1"
print(r1.version)

# example 2
class Mic:
    # constructor
    def __init__(self):
        # initializing attribute
        self.brand = "BOYA"
        self.price = "2500"
    
    # method
    def getInfo(self):
        print(f"Brand : {self.brand}")

print("")
m1 = Mic()
m1.getInfo()
print(m1.brand)


# types of constructor
# 1. non-parameterized constructor

class Sport:
    name = ""
    team = ""

    # parameterized constructor
    def __init__(self, param_name, param_team):
        self.name = param_name
        self.team = param_team
    
    # method
    def getSport(self):
        print(f"Name : {self.name}")

s1 = Sport("Football", "Uruguay")
print(s1.name)
s1.getSport()

# Destructor -> use to destroy object or release object from memory
# del -> function is use as destructor

# del s1 # destroy the object s1
# s1.getSport()

"""
Java --> same name as class name
PHP --> __contruct()
Python --> __init__()
"""


# 2. parameterized constructor
