"""INHERITANCE
Inheritance is basically the process that allows us to create a new class and reusing the code from the existing parent class
The parent class (superclass or base class) is the class being inherited from
The child class (subclass or derived) is the class that inherits from another class

If I create a child class without an __init__()method it inherits all methods and attributes of the parent class













"""
# Basic class   31
# Creating a child class   45
# Adding an __init__ to a child class   53
# Adding a call to the parent __init__ method   67
# Adding attributer to the child class   82
# 
# 
# 
# 

# Basic class
class Person:
    def __init__(self,fname,lname):
        self.firstname  = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
florist = Person('Jane', 'Flowers')  # I've instanciated the class called Person
florist.printname()  # Jane Flowers



# Creating a child class
class Lawyers(Person):  # Inheriting the methods and variables from the parent class
    pass
happy_lawyers = Lawyers('Jack','Smiley')  # this will inherit the methods and variables of the parent class
happy_lawyers.printname()  # Jack Smiley



# Adding an __init__ to a child class
# class Lawyers(Person):
#     def __init__(self,fname,lname):  # This overrides th init of the parent function
#         self.firstname  = fname
#         self.lastname = lname
        
#     def printinfo(self):
#         print(self.firstname,self.lastname)
        
# happy_lawyers = Lawyers('Jack','Smiley')
# happy_lawyers.printinfo()  # Jack Smiley



#  adding a call to the parent __init__ method
# class Lawyers(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
#         # self.firstname  = fname
#         # self.lastname = lname
        
#     def printinfo(self):
#         print(self.firstname,self.lastname)
        
# happy_lawyers = Lawyers('Jack','Smiley')
# happy_lawyers.printname()  # Jack Smiley



# Adding attributer to the child class 
class Lawyers(Person):
    def __init__(self,fname,lname,casetype):
        Person.__init__(self,fname,lname)
        self.casetype = casetype
        
        # self.firstname  = fname
        # self.lastname = lname
        
    def printinfo(self):
        print('Hello my name is ',self.firstname,self.lastname)

happy_lawyers = Lawyers('Jack','Smiley','criminal')
happy_lawyers.printinfo()  # Jack Smiley

print(happy_lawyers.casetype)  # criminal
