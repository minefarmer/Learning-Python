#  A list is a collection of data which can be of mixed type.
#  Items in a list are ordered by their index and changeable.
#  Lists are created with square brackets. []
#  Items in a list can be assessed by thier index
#  Each item is a list is separated by a comma




#  I can create a list using a constructor which is a function used to create objects
animals = ['bear', 'tiger','lion','panda','elephant']
# for x in animals:
#     print(x)  # bear
#                 # tiger
#                 # lion
#                 # panda
#                 # elephant
                
# print(animals)  # ['bear', 'tiger', 'lion', 'panda', 'elephant']



#  Accessing Elemente of the lists.  *****************************************
#  can be accesses using thier index or position in the list
#  the index is zero based. First element has a position of zero

print(animals[0])  # bear
print(animals[-1])  # elephant
print(animals[1:])  # ['tiger', 'lion', 'panda', 'elephant']
print(animals[1:3]) # ['tiger', 'lion']

animals[0] = 'dog'
print(animals)  # ['dog', 'tiger', 'lion', 'panda', 'elephant']

