'''SYNTAX TO OPEN FILE
f = open('myfile.txt)
f = open('myfile.txt','rt')
f = open(c:\\myfolders\myfile.txt)  # if not in the same directory
'''
# 
# 
# 


# f = open("Quotes.txt")

# print(f.readable())  # True

# print(f.read())  # Kindness is a universal language

                    # Everyday is a gift. do not waste it 

                    # Dream big and take action


# f.close()
# print(f.readable())  # Traceback (most recent call last):
#   File "/home/carl/Github/Learning-Python/OpenReading.py", line 23, in <module>
#     print(f.readable())
# ValueError: I/O operation on closed file

# print(f.read(11))  # Kindness is

# print(f.readlines())  # ['Kindness is a universal language\n', '\n', 'Everyday is a gift. do not waste it \n', '\n', 'Dream big and take action']

# for quote in f:
    # print(quote)  # Kindness is a universal language
# Everyday is a gift. do not waste it 
# Dream big and take action


# f = open("Quotes.txt", 'a')  # this adds lines to an existing file

# f.write("\nHappiness is from within")


f = open("Quote.txt", 'w')  # This will delete all existing words

f.write("\nHappiness is from within")

f.close()