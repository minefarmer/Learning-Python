'''Keyword argument
Allows me to specify what parameters to use from a list of parameters
I do not need to worry about the order of the arguments
Allows me to give values only to parameters I want provided the other parameters have default values
'''

def more_num(a,b=7,c=10):
    print('a is ',a, 'and b is ',b,'while c is ',c)
    
more_num(3,7)  # a is  3 and b is  7 while c is  10
more_num(23,c=17)  # a is  23 and b is  7 while c is  17
more_num(c=40,a=80)  # a is  80 and b is  7 while c is  40