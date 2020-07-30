"""VARARGS PARAMETERS
lets me define variable number of arguments for a function
this is done using the asterisk. *

"""
# 
# 
# 
# 
# 
def total_numbers(a=7, *numbers, **phonebook):  # one(numbers) * = a tuple,  two(phonebook) ** = dictionary
    print('My favorite number is ', a)  # My favorite number is  7

# The arguments for the tuple will be supplied when the function is called
    for num in numbers:
        print('num', num)
# When the function is called the names supplied will be assigned a phone number  
    for name, phone_number in phonebook.items():
        print(name, phone_number)
        
total_numbers(7,1,2,3,Jane=2222,John=4444,Angela=5555)  # num 1
                                                        # num 2
                                                        # num 3
                                                        # Jane 2222
                                                        # John 4444
                                                        # Angela 5555