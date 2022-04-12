# Encapsulation 
# data hiding or data binding
# public --> Can be access throughout the system
# private --> Can be access inside a class only
# protected--> can be access inside the package only


class Employee:
    def __init__(self, name, contact, email):
        self.__name = name
        self.__contact = contact
        self.__email = email

    # we need public method
    # accessor and mutator to access and store data to private attributes
    # getter --> to access data -> return type
    # setter --> to store data -> takes parameter

    def getName(self):
        return self.__name

    def setName(self, param_name):
        self.__name = param_name

    def getContact(self):
        return self.__contact
    def setContact(self, param_contact):
        self.__contact = param_contact
    
    def getEmail(self):
        return self.__email
    def setEmail(self, param_email):
        self.__email = param_email

e1 = Employee("Roshan", 98608950723, "roshansth11@gmail.com")
e1.setName("Roshan")
e1.setContact("98608950723")
e1.setEmail("roshansth11@gmail.com")
print(e1.getName(), e1.getContact(), e1.getEmail())


# we cannot assign value directly to the private attributes we need pubic methods to do so