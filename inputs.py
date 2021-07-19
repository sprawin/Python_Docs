# Inputs from user

x = input("Enter a number ")
y = input("Enter second number ")

# By default input function will convert the input entered by user into integer

int_x = int(x)
int_y = int(y)
print(int_x+int_y)

# To fetch only one character

ch = input("Enter a char ")[0]
print(ch)

# Eval function

result = eval(input("Enter your expression "))
print(result)