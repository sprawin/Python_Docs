from numpy import *
from numpy.matrixlib.defmatrix import matrix

m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('6 4 8; 5 5 2; 7 2 8')

# Matrix Multiplication
m3 = m1*m2
print(m3)

print("\n",diagonal(m3))

# Array to matrix

arr = (
    [
        [4,5,6],
        [2,3,8]
    ]
)
print("Array: \n",arr)
m = matrix(arr)
print("\nMatrix: \n",m)