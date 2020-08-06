"""         ACCESSING FILE OBJECT ATTRIBUTES
    File pointer
Determines where any operation on a file starts
If the file is in default access r mode it is set to the start of the file.
tell() can show you current file pointer position
Seek() is used to set the position of the pointer




"""
# File pointer   29
# Deleting and renaming files   44
# 
# 
# 
# 

# f = open('Quotes.txt')

# print(f.name)  # Quotes.txt

# print(f.mode)  # r

# print(f.closed)  # False



# File pointer

# print(f.tell())  # 0

# print(f.read())  # Kindness is a universal language

#                 # Everyday is a gift. do not waste it 

#                 # Dream big and take action
# print(f.tell())  # 101
# print(f.seek(0))  # 0
# close()



#  Deleting and renaming files
# f = open('Rename.txt')
# f.close()

import os

# os.rename('Rename.txt', 'Rename2.txt')  # worked!

os.remove('Rename2.txt')

# os.remove('folder')