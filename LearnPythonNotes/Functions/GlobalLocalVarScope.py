'''GLOBAL VS LOCAL VARIABLE SCOPE
Variavles defined inside a function body have a loval scope
Variables defined outside a function have a global scope
Global variables can be access anywhere in your python file
Local variables can only be accessed inside the function it belongs to

'''
# Global var not changed   12
# changing the original global var   26 
# 
# 
# x = 10

# def my_numbers(x):
#     print(x)
#     x = 7
#     print('My fav number is ', x)

# my_numbers(x)  # 10   ** global var
#                 # My fav number is  7   ** local variable

# print(x)  # 10   ** global var



# changing the original global var
x = 10

def my_numbers():
    global x
    print(x)
    x = 7
    print('My fav number is ', x)

my_numbers()  # 10
              # My fav number is  7   ** local variable

print(x)  # 7   ** global var changed