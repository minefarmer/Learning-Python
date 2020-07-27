# len()  15
# index()  18
# capitalize()  21
# upper()  23
# lower()  25
# islower()  27
# isupper()  29
# find()   31
# count()  33
# split()  35
# \n  37
# Concatenation +  40
# replace()  43

g = "hello world."
print(len(g))  # 12

#  This method returns the position of a string or charactor
print(g.index('world')) # 6

print(g.capitalize())  # Hello world.

print(g.upper())  # HELLO WORLD.

print(g.lower())  # hello world.

print(g.islower())  # True

print(g.isupper())  # False

print(g.find('world')) #  6

print(g.count('l'))  # 3

print(g.split())  # ['hello', 'world.']

print('show\n d money')  # show
                         # d money
                         
# Concatenation adds two strings together.
print(g +' Hope you are doing ok. ')  # hello world. Hope you are doing ok.

# Replaces strings or characters.
# takes two parameters What to replace and what with.
print(g.replace('world', 'people'))  # hello people.