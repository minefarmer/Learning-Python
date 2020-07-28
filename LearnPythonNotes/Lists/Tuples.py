# What is a tuple?
# a tuple is a list that can not be changed. {immutable}
# can be created using parentheses. () and with a constructor
# elemente in a tuple can be accessed by thier index
# creating a tuple   16
# accessing elements in a tuple   25
# Can't change   42
# delete   58
# 
# 
# 
# 
# 
# 
# 
# creating a tuple with parenthesis
# fruits = ('grapes', 'apples', 'berries')
# for x in fruits:
#     print(x)  # grapes
#                 # apples
#                 # berries
                
                
                
# # Accessing elements in a tuple
# print(fruits[2])  # berries



# creating a tuple with a tuple constructor
# animals = tuple(('lion', 'tiger', 'bear'))
# # print(animals)  # ('lion', 'tiger', 'bear')
# print(len(animals))  # 3
# animals.add('dog')
# print(animals)  # Traceback (most recent call last):
#                 # File "/home/carl/Github/Learning-Python/LearnPythonNotes/Lists/Tuples.py", line 34, in <module>
#                 #     animals.add('dog')
#                 # AttributeError: 'tuple' object has no attribute 'add'



animals = tuple(('lion', 'tiger', 'bear'))
# # print(animals)  # ('lion', 'tiger', 'bear')
# print(len(animals))  # 3
# # animals.add('dog')
# # print(animals)  # Traceback (most recent call last):
# #                 # File "/home/carl/Github/Learning-Python/LearnPythonNotes/Lists/Tuples.py", line 34, in <module>
# #                 #     animals.add('dog')
# #                 # AttributeError: 'tuple' object has no attribute 'add'
# animals[0] ='cheetah'
# print(animals)  # Traceback (most recent call last):
#                 # File "/home/carl/Github/Learning-Python/LearnPythonNotes/Lists/Tuples.py", line 50, in <module>
#                 #     animals[0] ='cheetah'
#                 # TypeError: 'tuple' object does not support item assignment
                
                
                
del animals
print(animals)  # Traceback (most recent call last):
                # File "/home/carl/Github/Learning-Python/LearnPythonNotes/Lists/Tuples.py", line 59, in <module>
                #     print(animals)
                # NameError: name 'animals' is not defined