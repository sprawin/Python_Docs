# key word arguments
def person(**data):
    for i,j in data.items():
        print(i,j)

person(name = "Praveen", age = 23, mobile = 9486185751)