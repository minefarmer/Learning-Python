# collection of lists. each list is a item
# each list is a row with columns within the collection
fruits = [
    ['apples', 'berries', 'kiwi'],
    ['oranges', 'berries', 'plums'],
    ['mangoes', 'bananas', 'coconuts'],
    ["pineapples"]
]
# elements can be accessed by their index
print(fruits[1][1])  # berries

for row in fruits:
    for col in row:
        print(col)  # apples
                    # berries
                    # kiwi
                    # oranges
                    # berries
                    # plums
                    # mangoes
                    # bananas
                    # coconuts
                    # pineapples
