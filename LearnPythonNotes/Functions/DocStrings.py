"""DOCSTRINGS(Document Strings)
Allows me to display code documentation when code executes
They are accessed by using double underscore with attribute name

"""
# help() and pydoc() functions can provide more information about docstrings.
# 
# 
# 
# 
def add_numbers(d,e):
    '''Adding two numbers.
    
    The values must be intergers'''
    
    print(d + e)
    
add_numbers(8,4)  # 12

print(add_numbers.__doc__)  # Adding two numbers.
    
                                # The values must be intergers

