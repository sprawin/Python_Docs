#Input values is given from cmd while executing "python inputs_from_cmd.py 6 5"

import sys

filename = sys.argv[0]
x = int(sys.argv[1])
y = int(sys.argv[2])

print("filename: ",filename)
print("x+y = ",x+y)
