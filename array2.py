# Array values from user.

from array import *

arr = array('i',[])
n =int(input("Enter length of the array: "))
for i in range(n):
    x = int(input("Enter value one by one: "))
    arr.append(x)

print(arr)

# To search for a number in the array
element = int(input("Enter value for seach: "))
i=0
for e in arr:
    if e == element:
        print("Element found at index ",i)
        break
    i = i+1
else:
    print("Element not found")

# To search for a number in the array
print("# To search for a number in the array\n")
print(arr.index(element))