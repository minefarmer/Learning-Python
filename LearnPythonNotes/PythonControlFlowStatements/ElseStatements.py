'''Else statements
Code that executes if conditions checked evaluates to False

'''

# if(Condition1):
#     # Indented statement block for Condition1
# elif(Condition2):
#     # Indented statement block for Condition2
# else:
#     # Alternate statement block if all condition checked above fails


a = 7
b = 8
c = 9

if a > b:
    print(a, ' is smaller than', b)

elif b >= c:
    print(b, ' is smaller than', c)
    
else:
    print(c, ' is larger than', b, 'and', a)  # 9  is larger than 8 and 7