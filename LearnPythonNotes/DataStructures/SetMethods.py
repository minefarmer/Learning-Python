# Built-in set methods   11
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Built-in set methods 
# Method      Description
# add()     Adds an element to a set
# Update()  Adds multiple elements to a set
# clear()   Removes all elements in a set
# discard() Removes a specified item item from the set
# del()     Deletes the set



fruits = {'grapes', 'apples', 'berries'}
animals = set(('lion', 'tiger', 'bear'))
fruits.add('oranges')
print(fruits)  # {'apples', 'berries', 'grapes', 'oranges'}
fruits.update(['mango', 'kiwi'])
print(fruits)  # {'grapes', 'berries', 'kiwi', 'oranges', 'apples', 'mango'}
fruits.remove('kiwi')
print(fruits)  # {'mango', 'berries', 'oranges', 'grapes', 'apples'}
fruits.clear()
print(fruits)  # set()
del animals
print(animals)  # Traceback (most recent call last):
                # File "/home/carl/Github/Learning-Python/LearnPythonNotes/DataStructures/SetMethods.py", line 32, in <module>
                #     print(animals)
                # NameError: name 'animals' is not defined