"""POLYMORPHISM
Polymorphism means the ability to take or have various forms  ===  Smartphone








"""
# Polymorphic class   22
# Polymorphic class with methods   30
# 
# 
#
# 
# 
# 
# 
 
# def addNumbers(a,b,c=1):
#     return a + b + c

# print(addNumbers(8,9))  # 18   ***I'm passing arguments for the function parameters.

# print(addNumbers(8,9,4))  # 21


# Polymorphic class with methods 
def addNumbers(a,b,c=1):
    return a + b + c

# print(addNumbers(8,9))  # 18   ***I'm passing arguments for the function parameters.

# print(addNumbers(8,9,4))  # 21
# Create Polymorphism by using existing method on a new function
class UK():
    def capital_city(self):
        print('London is the capital of UK')  # London is the capital of UK

    def language(self):
        print('English is the primary language ')  # English is the primary language


class Spain():
    def capital_city(self):
        print('Madrid is the capital of Spain')  # Madrid is the capital of Spain

    def language(self):
        print('Spainish is the primary language ')  # Spainish is the primary language 
        
def europe(eu):
    eu.capital_city()
    
        
        
queen = UK()
# queen.capital_city()

zara = Spain()

europe(queen)  # London is the capital of UK
europe(zara)  # Madrid is the capital of Spain
# zara.capital_city()
'''
for country in (queen,zara):
    country.capital_city()
    country.language()
'''