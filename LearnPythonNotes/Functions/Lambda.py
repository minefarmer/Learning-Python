"""Anonymous Functions(Lambda)
they are defined by using the lambda keyword
They can take several arguments, but can only have one expression

"""


# an anonymous functions
# a = lambda b: b + 4
# print(a(4))  # 8

# c = lambda d,e : d + e
# print(c(7,8))  # 15



# i can also use lambda function when an anonymous function is required for a short period inside another function
def ghost_number(n):
    return lambda f : f * n

double_num = ghost_number(2)

print(double_num(20))  # 40
