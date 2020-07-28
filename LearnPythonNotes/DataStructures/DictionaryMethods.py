# how to create a dictionary   18
# how to create a dictionary with a constructor()   28
# built-in dictionary methods   35
# count key:value pairs   46
# updating key:value pairs   51
# get()   58
# add new key:value pair   63
# 
# 
# 
# a dictionary is a collection of key value pairs
# the values can e changed (mutable)
# the values have unique Keys
# I can store mixed data types



# how to create a dictionary
mycar = {
    'brand': 'Range Rover Sports',
    'model': 'HSE',
    'year': 2017
}
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2017}



# # how to create a dictionary with a constructor()
# mygreens = dict(fruit='green apples',vegetables='kale')

# print(mygreens)  # {'fruit': 'green apples', 'vegetables': 'kale'}



# built-in dictionary methods
# Method        Description
# get()         Returns the value of the specified key
# Update()      Inserts specified key:value pair in dictionary
# clear()       Removes all key:value pairs in dictionary
# keys()        Returns a list of dictionary keys
# values()      Returns a list of dictionary values
# del()         Deletes the dictionary



# # count key:value pairs
# print(len(mycar))  # 3



# # updating key:value pairs
# mycar['year'] = 2019
# print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2019}




# # get()
# print(mycar.get('year'))  # 2019



# # add new key:value pair
mycar.update({'color': 'silver'})
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2017, 'color': 'silver'}
# b = mycar.keys()
# print(b)  # dict_keys(['brand', 'model', 'year'])
# b = mycar.values()
# print(b)  # dict_values(['Range Rover Sports', 'HSE', 2017])
mycar.pop('color')
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2017}
# mycar.clear()
# print(mycar)  # {}
del mycar
print(mycar)  # Traceback (most recent call last):
                # File "/home/carl/Github/Learning-Python/LearnPythonNotes/DataStructures/DictionaryMethods.py", line 75, in <module>
                #     print(mycar)
                # NameError: name 'mycar' is not defined
