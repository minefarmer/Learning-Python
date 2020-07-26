"""Operator Precedence
This determines the order in which operators should be evaluated if there are multiple operators used in a statement or expression.
3 + 4 * 2 = 11  # in this expression the multiplication has a higher precedence than the addition operator

Operator Precedence hierarchy and the name of the operator
Operator Precedence         Name
()                          Parenthesis
**                          Exponent(Power)(Pow)
~x                          Bitwise NOT
*, /, //,   %               Multiplication, Division, Floor Division, Modulus
+, -                        Addition, Subtraction
<<, >>                      Bitwise shift operators
&                           Bitwise AND
^                           Bitwise XOR
|                           Bitwise OR
==,!=,>,>=,<,<=,is,is not, in,not in    Comparisions,Identity,Membership
not                         LOGICAL not
and                         Logical AND
or                          Logical OR

"""