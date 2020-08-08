# Part 1   5
# Part 2  Changing data type   44
# Part 3  Implementing Basic Exception Handling   90
# 
# Part 1
# print(x)  # Traceback (most recent call last):
            # File "/home/carl/Github/Learning-Python/LearnPythonNotes/ExceptionsErrors/Error.py", line 1, in <module>
            #     print(x)
            # NameError: name 'x' is not defined



# try:
#     print(x)
# except:
#     print("Variable is not defined.")  # Variable is not defined.



# try:
#     print(x)
# except:
#     print("Variable is not defined.")  # Variable is not defined.
# else:
#     print("Hello")
# finally:
#     print("You may get an error if no variable is specified")  # You may get an error if no variable is specified



# x = 20
# try:
#     print(x)  # 20
# except:
#     print("Variable is not defined.")
# else:
#     print("Hello")  # Hello
# finally:
#     print("You may get an error if no variable is specified")  # You may get an error if no variable is specified




# Changing data type 
# b = "Hello"

# print(int(b))  # Traceback (most recent call last):
                # File "/home/carl/Github/Learning-Python/LearnPythonNotes/ExceptionsErrors/Error.py", line 47, in <module>
                #     print(int(b))
                # ValueError: invalid literal for int() with base 10: 'Hello'



# while True:
#     try:
#         n = int(input("Enter a whole number: "))  # Enter a whole number: 8.5
#         break
#     except ValueError:
#         print("No valid interger entered")  # No valid interger entered
        
# print("Great, You have entered an integer")



# while True:
#     try:
#         n = int(input("Enter a whole number: "))  # Enter a whole number: abc
#         break
#     except ValueError:
#         print("No valid interger entered")  # No valid interger entered
        
# print("Great, You have entered an integer")



# while True:
#     try:
#         n = int(input("Enter a whole number: "))  # Enter a whole number: 77
#         break
#     except ValueError:
#         print("No valid interger entered")
        
# print("Great, You have entered an integer")  # Great, You have entered an integer






# Implementing Basic Exception Handling
# c = 12 /0  # Traceback (most recent call last):
            # File "/home/carl/Github/Learning-Python/LearnPythonNotes/ExceptionsErrors/Error.py", line 88, in <module>
            #     c = 12 /0
            # ZeroDivisionError: division by zero
            
            
# print(x)  # Traceback (most recent call last):
#   File "/home/carl/Github/Learning-Python/LearnPythonNotes/ExceptionsErrors/Error.py", line 97, in <module>
#     print(x)
# NameError: name 'x' is not defined


# print(int*"HI")  # Traceback (most recent call last):
#   File "/home/carl/Github/Learning-Python/LearnPythonNotes/ExceptionsErrors/Error.py", line 103, in <module>
#     print(int*"HI")
# TypeError: can't multiply sequence by non-int of type 'type'


# try:
#     n = 12/ int(input("Enter a whole number: ")) # Enter a whole number: 5.5
#     print("The value of your number is ", n)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)  # invalid literal for int() with base 10: '5.5'

# finally:
#     print("Hope you entered a valid whole number. ")  # Hope you entered a valid whole number. 


# try:
#     n = 12/ int(input("Enter a whole number: ")) # Enter a whole number: a
#     print("The value of your number is ", n)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)  # invalid literal for int() with base 10: '5.5'

# finally:
#     print("Hope you entered a valid whole number. ")  # Hope you entered a valid whole number. 


try:
    n = 12/ int(input("Enter a whole number: ")) # Enter a whole number: 8
    print("The value of your number is ", n)  # The value of your number is  1.5
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)

finally:
    print("Hope you entered a valid whole number. ")  # Hope you entered a valid whole number. 
