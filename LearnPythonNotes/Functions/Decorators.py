"""WHAT ARE DECORATORS
Decorators are used to add new functionality to existing objects like functions, methods and classes without modifying it's structure

Decorators are usually called before the defination of the object (Function, Method, Class) we want to decorate

They can be represented by @ followed by name of the decorated object
"""
# 
# # Easier way to create a decorator   29
# 
# ###  https://www.python.org/dev/peps/pep-0318/    ^^^^^^^^^^^  much more information!!!!!!!!!!
#  
# Creating a decorator
# def my_decorator(function):
#     def wrapper():
#         myfunc = function()
#         convert_uppercase = myfunc.upper()
#         return convert_uppercase
#     return wrapper

# def say_hello():
#     return 'hello world'
# decorate = my_decorator(say_hello)
# print(decorate())  # HELLO WORLD





# Easier way to create a decorator
def my_decorator(function):
    def wrapper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wrapper
@my_decorator
def say_hello():
    return 'hello world'
print(say_hello())  # HELLO WORLD