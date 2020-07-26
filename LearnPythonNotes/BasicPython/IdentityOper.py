"""  Python Identity operators
They are used to compare if objects are the same.

Operator    Discription 
is          Returns True if of same object.
is not      Returns True if not same object.
"""

my_fruits =['grapes', 'berries']
fruits = ['grapes', 'berries']
fav_fruits = fruits
print(fruits is fav_fruits)  # True
print(fruits is my_fruits)  # False  ** fruits and my_fruits are two differient objects
print("apples" not in fruits)  # True

