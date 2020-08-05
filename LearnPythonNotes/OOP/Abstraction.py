from abc import ABC, abstractmethod

'''ABSTRACTION
Abstraction refers to providing only essential information about the data to the outside world, thereby hiding the background details or impli=ementation
Abstraction hides the internal details and shows only functionalities


ABSTRACT CLASSES
They are classes that contain one or more abstract methods
They cannot be instantiated
They require subclasses to provide implementation for the abstract methods

ABC => Abstract Base Classes

In order to implement abstraction I am going to use a decorator with the module
A decorator allows me to add new functially to an existing object (classes, methods functions) without modifying it's atructure



'''
# Part one   31
# Part 2 @abstractmethod  ** can create an error   47
# Part 2 @abstractmethod 
# 
# 
# 
# 
# 
# 
# 
# Part one
# class Shape:        # Parent or base class
#     def area(self):
#         pass
#     def perimeter(self):
#         pass

# class Squere(Shape):
#     def __init__(self,side):
#         self.side = side
# 
# myshape = Shape()   # a variable  **  also an object




 #  Part 2   @abstractmethod 
# class Shape(ABC):        # Parent or base class
#     @abstractmethod     # this will create abstraction in this class
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass

# class Squere(Shape):
#     def __init__(self,side):
#         self.side = side
# 
# myshape = Shape()   # Traceback (most recent call last):
#                     # File "/home/carl/Github/Learning-Python/LearnPythonNotes/OOP/Abstraction.py", line 63, in <module>
#                     #     myshape = Shape()   # a variable  **  also an object
#                     # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter







#  Part 2  @abstractmethod 
class Shape(ABC):        # Parent or base class
    @abstractmethod     # this will create abstraction in this class
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Squere(Shape):
    def __init__(self,side):
        self.__side = side
        
    def area(self):
        return self.__side* self.__side     # What this is saying basically is that when these values return they will be multiplyed by itself

    def perimeter(self):
        return 4* self.__side
        
# myshape = Shape()

mysquare = Squere(5)
   # let us calculate the area and perimeter of the square class instance(object) called mysquare
print(mysquare.area())  # 25
print(mysquare.perimeter())  # 20
