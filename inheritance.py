# OOP

# 1. Inheritance
# --> if the child class is derived from the base or parent class with the properties of parent/base class

# syntax
# class ClassName(ParentClass):
    # constructor
    # attributes
    # methods

# example

class Person:
    def getDetail(self):
        print(f"Person Details : ")
    
class Boy(Person):
    def boyInfo(self):
        self.getDetail()
        print(f"Boy Details : ")

boy_one = Boy()
boy_one.boyInfo()
boy_one.getDetail()
print("----------------------------------------")

# example with constructor

class Gadget:
    def __init__(self):
        self.name = "Redmi Note 10 pro"
        self.brand = "MI"
        self. price = "20000"
    
    def __init__(self, param_name, param_brand, param_price):
        self.name = param_name
        self.brand = param_brand
        self.price = param_price

gadget_one = Gadget("Band", "MI", "6000") # 
print(gadget_one.brand)
print(gadget_one.name)
print(gadget_one.price)

# if multiple contructor is defined inside a class then the last defined constructor is only treated as actual contructor

# if the constructor is defined inside a child class then he parent class contructor must be defined inside the child class constructor

# Parent class properties can be accessed by two method
# 1. by class

class Band(Gadget):
    def __init__(self, param_name, param_brand, param_price):
        Gadget.__init__(self, param_name, param_brand, param_price)
        self.diameter = 23
print("----------------")
b1 = Band("Redmi", "Mi NOte 10 pro", "35000")
print(b1.name)
print(b1.brand)
print(b1.price)
print("----------------")

# 2. by super() method
# in super method we should not pass self

class Shoes(Gadget):
    def __init__(self, param_name, param_brand, param_price):
        super().__init__(param_name, param_brand, param_price)
        self.name = param_name
        self.brand = param_brand
        self.price = param_price
s1 = Shoes("Jordan", "Nike", "100000")
print(s1.name)
print(s1.brand)
print(s1.price)

# types of inheritance
# 1. Single Inheritance

class Jug:
    def getJug(self):
        print("This is a jug.")

class PlasticJug(Jug):
    def getPlasticJug(self):
        self.getJug()
        print("This is a Plastic Jug.")

p1 = PlasticJug()
p1.getPlasticJug()


# 2. Multiple Inheritance

class Shape:
    def getShape(self):
        print("This is a Shape.")

class Area:
    def getArea(self):
        print("Area of a Shape.")

class Rectangle(Shape, Area):
    def getRectangle(self):
        self.getShape()
        self.getArea()
        print("Rectangle.")

r1 = Rectangle()
r1.getRectangle()

# 3. Multi-level ingeritance or hierarchical

class GranfFather:
    def grand(self):
        print("Grand Father.")

class Father(GranfFather):
    def father(self):
        print("Father")

class Son(Father):
    def son(self):
        print("Son")

print("---------------------------------------------")
s1 = Son()
s1.son()
s1.father()
s1.grand()

print("-----------------------------------------------------")
# Method Overriding
# --> Child class overrides or change the functionality of base class method by declaring same name function inside child class

class Area:
    def getArea(self):
        self.area = 0

class Rectangle(Area):
    def getArea(self):
        self.len = 12
        self.breadth = 14
        self.area = self.len * self.breadth
        print(self.area)

class Triangle(Area):
    def getArea(self):
        self.height = 13
        self.base = 13
        self. area = 1/2 * self.base * self.height
        print(self.area)

t1 = Triangle()
t1.getArea()

r1 = Rectangle()
r1.getArea()

