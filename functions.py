def calculate(x,y):
    a = x + y
    s = x - y
    d = x/y
    m = x*y
    return a,s,d,m

a,b,c,d = calculate(10,2)
print(a,b,c,d)