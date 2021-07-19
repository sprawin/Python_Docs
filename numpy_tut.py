# Numpy is used to deal with multi-dimensional arrays
# by using array module we cannot work with multi-dimensional array

from numpy import *
my_array = array([[1,2,3,4], [5,6,7,8]])
arr = array([1,2,3,4,5.0])
print(my_array)
print(arr.dtype)
print(arr)

# linspace()

arr_lin = linspace(0,16,5)
print(arr_lin)
arr_lin_2 = linspace(0,16,16)
print(arr_lin_2)

arr_2 = arange(1,15,2)
print(arr_2)

# zeros

arr_0 = zeros(5)
arr_1 = ones(5)
print(arr_0)
print(arr_1)