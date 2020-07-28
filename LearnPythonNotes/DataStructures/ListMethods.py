# extend()  11
# append()  20
# sort()   26
# count()   35
# index()   40
# insert()   45
# pop()   53
# remove()   62
# del()   68
# 
# extend adds two lists together
fruits = ['berries', 'apples', 'grapes', 'oranges']
vegetables = ['kale', 'broccoli', 'lettuce']

fruits.extend(vegetables)
print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli, lettuce']



# adds an item ti the end of the list
vegetables.append('bean')
print(vegetables)  # ['kale', 'broccoli', 'lettuce', 'bean']



#  Orders list items. Ascending or decending
vegetables.sort()
print(vegetables)  # ['bean', 'broccoli', 'kale', 'lettuce']

vegetables.sort(reverse=True)
print(vegetables)  # ['lettuce', 'kale', 'broccoli', 'bean']



# counts the occurance of a list item
print(fruits.count('berries'))  # 1



# returns the index position of a list item
print(fruits.index('grapes'))  # 2



# adds item to the list
#  takes two parameters: Index and item
fruits.insert(0, 'banana')
print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettuce']



# removes the last item from the list if none is specified
# I can specify what to remove as a parameter
print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettuce']
fruits.pop()
print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli']
fruits.pop(0)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli']
print(fruits) 



# removes a specified item from the list
vegetables.remove('kale')
print(vegetables)  # ['lettuce', 'broccoli', 'bean']



# delets list
del vegetables
print(vegetables)  #  File "/home/carl/Github/Learning-Python/LearnPythonNotes/Lists/ListMethods.py", line 70, in <module>
                    # print(vegetables)
                    # NameError: name 'vegetables' is not defined
