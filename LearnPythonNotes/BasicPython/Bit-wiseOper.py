"""Bit-wise operators  Part 1
    Bit-wise operators  Part 2   65
they are used to compare binary numbers.

BIT-WISE AND &
sets each bit to matching value. Otherwise sets to zero.

    X           Y           X&Y
    o           0           0
    0           1           0
    1           0           0
    1           1           1
    
    
    5 & 4
Convert to binary

5 = 1 0 1

4 = 1 0 0
  _______
    1 0 0  =  4




BIT-WISE OR |

SETS EACH BIT TO MATCHING VALUE. oTHERWISE SETS TO 1. 

    X           Y           X&Y
    o           0           0
    0           1           1
    1           0           1
    1           1           1

    5 | 4
  Convert to Binary
  5 = 1 0 1
  4 = 1 0 0
  __________
      1 0 1  =  5
  
  
BIT-WISE XOR ^

SETS EACH MATCHING BIT TO ZERO.  oTHERWISE TO ONE

    X           Y           X&Y
    o           0           0
    0           1           1
    1           0           1
    1           1           0

     8 ^ 4
    Convert to Binary
    5 = 1 0 1
    4 = 1 0 0
    __________
        0 0 1  =  1
        
        
        
        
Part 2

BIT-WISE NOT ~
Invert the bits.

X becomes-(x+1)

~7=-8

BIT-WISE LEFT SHIFT <<
Returns x with the bits shifted to the left by y places.
3 << 2
11+00 => 1100 => 12

BIT-WISE RIGHT SHIFT >> 
Returns x with the bits shifted to the  RIGHT by y places.
tHE y PLACES DELETES BITS.
3 >> 1
11 - 1 => 1=>1


Operator    Name
   &        AND
   |        OR
   ^        XOR
   ~        NOT
   <<       Left shift
   >>       Right shift

"""