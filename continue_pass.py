# CONTINUE
# Print values which are not divisible by 3 or 5
for i in range(1,10):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)

# PASS
# print only odd numbers
print("\nprint only odd numbers\n")
for i in range(1,11):
    if i%2 == 0:
        pass
    else:
        print(i)