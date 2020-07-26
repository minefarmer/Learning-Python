'''CASTING
Casting is the process of converting the value of a variable from one data type to another.
This is done using various built-in Python functions.
int() converts value to an integer (whole number).
float() converts value to floating point number(decimal),
str()converts value to string(text)

'''

x = '70'
y = '-20'
print(x + y)  # 70-20 ** Treating the values as a string

# using casting to  convert the values into an integer
print(int(x) + int(y))  # 50

# converting to a float
c = 7
d = 8
print(float(c) + float(d))  #15.0

# converting to a str
e = 9
f = 8.5
print(str(e), "and", str(f), "are strings")  # 9 and 8.5 are strings
