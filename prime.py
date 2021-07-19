print("Check For Prime Number \n")

num = 6
for i in range(2,num):
    if num % i ==0:
        print("Not Prime")
        break
else:
    print("Prime")
