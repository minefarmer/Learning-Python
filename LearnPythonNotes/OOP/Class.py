"""CREATING A CLASS
Directory   27
Created with the keyword class folled by a name.
Common practice is to make the names Pascl Casing: Example:MyFirstCar.
A class consists of variables(Attributes) and functions (Methods)

__init__() is a built-in function. Also known as the initializer. Used to initialize objects with initial values. All classes should have them. It is called automatically when a new object is created from a class.

Modifying a Class
Add new attributes
Modify existing attribute values
Delete attributes


Importing Classes
Once I have created a class you can also reuse the code you have created for that class, I can use it in other programs that you're writing by importing the classes
I can import them into another program that I are working on == just like importing a module


Class Vs Instance (Object) Variables

Class Variables                                 Instance (Object) Variables
Defined outside any method                      Defined inside class methods
Accessed outside with className                 Accessed outside class with object name
Not Prefixed                                    Prefixed with self keyword
Modifications affwcts all classes instances     Modifications to object local
Classes indented                                Instances are not indented

"""
# Instantiating a class   58
# Accessing Methods   65
# Accessing Atribute   71
# Modifying a Class   79
# Change the value of an attribute   90
# Importing classes   108
# 
# 
# 
# 
# 
# 
class Instructors:  # all classes should have the uderscore underscore in it, as shown below.
    companyName = "BlueLime"   # this is a variable
    
    def __init__(self,course, duration):  # this is a method   **** this method __init__ is a built in function == it is called the initializer, The initial value can be changed later.
        self.course = course  # this is a variable
        self.duration = duration
        # The self paremeter is basically a reference to the current instance of the class
    
    def printinfo(self):  # this is a method
        print('My Company name is ', Instructors.companyName)  # this is a variable that grabs the var 'Bluelime'
        
# class Pets:
#     pass  # a class that has no methods



# Instantiating a class
elearning = Instructors('Python for Beginners',7)  # on line 45 [course] refers to 'Python for Beginners' here.

bls = Instructors('Django for beginners',8)  # on line 45 [course] refers to 'Django for Beginners' here.



# Accessing Methods
# ObjectName.Method  ** so I can call the method on a new object I have instantiated.

bls.printinfo()  # My Company name is  BlueLime  *** calls method on line 47



# Accessing Atribute
# ObjectName.Attribute

print(bls.course)  # My Company name is  BlueLime
                    # Django for beginners
                    
                    
                    
# Modifying a Class
# Adding a new attribute
# Changes made to the init   44
    # def __init__(self,course, duration):  # (duration) added
    #     self.duration = duration  # this line added
    # changes on 58, 7:  60, 8

print(bls.duration)   # 8   ***  from line 60



# Change the value of an attribute   ***  bls on line 60

bls.course = "HTML"

print(bls.course)    # HTML


# Delete an attribute

del bls.duration

print(bls.duration)  # Traceback (most recent call last):
                    # File "/home/carl/Github/Learning-Python/LearnPythonNotes/OOP/Class.py", line 101, in <module>
                    #     print(bls.duration)
                    # AttributeError: 'Instructors' object has no attribute 'duration'
                    
                    

