'''NESTED LOOPS
Nested loops are a loop inside a loop

'''
# 
# 
# 
colors = ['green','yellow','purple']

fruits = ['apple', 'banana', 'berries']

for x in colors:
    for y in fruits:
        print(x,y)  # green apple
                    # green banana
                    # green berries
                    # yellow apple
                    # yellow banana
                    # yellow berries
                    # purple apple
                    # purple banana
                    # purple berries
        
