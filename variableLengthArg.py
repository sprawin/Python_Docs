def sum(*b):
    # b will be a tuple
    c = 0
    for i in b:
        c = c+i
    return c

print(sum(3,4,5,6))