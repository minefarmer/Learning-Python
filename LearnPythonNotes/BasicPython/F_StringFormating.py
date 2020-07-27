# STRING FORMATTING
# Multiline f -strings  25
# Using f -string
# F- string is a string literal prefixed with f.  ***  can be upper or lower case.
# contains expressions inside curly braces which are replaced with values.
# F string is an expression that is evaluated at runtime and then formated,
# they are not a constant value.
# 
# 
# 
name = 'Bluelime'
age = 4
# print(f'Hello, {name}. You are 4 years old .')  # Hello, Bluelime. You are 4 years old .

# print(f'{ 7 + 7} ')  # 14

# print(f'{name.upper()} is 247 online learning, ')  # BLUELIME is 247 online learning, 







#  Multiline f -strings   ******************************************************

# print(f'{name.upper()} is 247 online learning, ')  # BLUELIME is 247 online learning, 
# profession = "developer"
# message = (
#     f"Hi {name} . "
#     f" You are a{profession}. "
#     f" You have been teaching online for {age} years. "
# )
# print(message)  # Hi Bluelime .  You are adeveloper.  You have been teaching online for 4 years.


car = {'brand': 'Range Rover', 'model': 'HSE'}
print(f"The car I like is {car['brand']} sports {car['model']}. ")  # The car I like is Range Rover sports HSE.
