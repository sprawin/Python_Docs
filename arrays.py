from array import *

vals = array('i',[5,9,-8,4,2])

# i in the above code refers to integer array.
print(vals)
#To get address and size of the array use buffer_info()
print(vals.buffer_info())
# To get type of the array
print(vals.typecode)
# To reverse the number
vals.reverse()
for i in vals:
    print(i)

# To Copy the array
newArr = array(vals.typecode,(a for a in vals))
print(newArr)