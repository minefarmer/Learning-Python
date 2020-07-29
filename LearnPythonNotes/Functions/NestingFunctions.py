# Nested functions   11
# Nested functions accessing Variable Scope   20
# Pass Statement   34
# 
# 
# 
# 
# 
# 
# 
# def mynum(a):
#     def num(a):
#         return a + 1
#     result = num(a)
#     return result
# print(mynum(4))  # 5



# Nested functions accessing Variable Scope
# Python allows a nested function to access the outer scope of the enclosing function
#  This concept of pattern is referred to as closure
def display_message(message):
    'hello'
    def message_sender():
        'nested function'
        print(message)
    message_sender()

display_message('Show me the money!')



# Pass Statement
def dream_home():
    pass
