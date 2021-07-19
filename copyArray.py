# Shallow Copy

from numpy import *

arr1 = array([5,4,3,2,1])
arr2 = arr1

# The above is shallow copy. here if you change arr1[4] value to something else, arr2 will also get updated

arr1[3] = 15
print(id(arr1))
print(arr1)
print(id(arr2)) 
print(arr2) 

# In the above case the address is also same for both the arrays
# If you want different address go for .view()

arr3 = array([5,4,3,2,1])
arr4 = arr3.view()
arr3[3] = 15
print(id(arr3))
print(arr3)
print(id(arr4)) 
print(arr4) 

# if you want to copy the array without affecting the other one even upon updating one of the array go for .copy()

arr5 = array([5,4,3,2,1])
arr6 = arr5.copy()
arr5[3] = 15
print(id(arr5))
print(arr5)
print(id(arr6)) 
print(arr6) 
