"""CREATING A CLASS
Directory   27
Created with the keyword class folled by a name.
Common practice is to make the names Pascl Casing: Example:MyFirstCar.
A class consists of variables(Attributes) and functions (Methods)

__init__() is a built-in function. Also known as the initializer. Used to initialize objects with initial values. All classes should have them. It is called automatically when a new object is created from a class.

















"""
# Instantiating a class   56
# Accessing Methods   63
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
class Instructors:  # all classes should have the uderscore underscore in it, as shown below.
    companyName = "BlueLime"   # this is a variable
    
    def __init__(self,course):  # this is a method   **** this method __init__ is a built in function == it is called the initializer, The initial value can be changed later.
        self.course = course  # this is a variable
        # The self paremeter is basically a reference to the current instance of the class
    
    def printinfo(self):  # this is a method
        print('My Company name is ', Instructors.companyName)  # this is a variable that grabs the var 'Bluelime'
        
# class Pets:
#     pass  # a class that has no methods



# Instantiating a class
elearning = Instructors('Python for Beginners')  # on line 45 [course] refers to 'Python for Beginners' here.

bls = Instructors('Django for beginners')  # on line 45 [course] refers to 'Django for Beginners' here.



# Accessing Methods
# ObjectName.Method  ** so I can call the method on a new object I have instantiated.

bls.printinfo()  # My Company name is  BlueLime  *** calls method on line 47
