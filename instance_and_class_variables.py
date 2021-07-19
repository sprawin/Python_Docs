class car:
    wheels = 4 # this is an class variable or static variable. It is common for all objts.
    def __init__(self):
        self.mileage = 10
        self.company = "BMW"


c1 = car()
c2 = car()

print("mileage: ",c1.mileage," Company: ",c1.company," wheels: ",c1.wheels)
print("mileage: ",c2.mileage," Company: ",c2.company," wheels: ",c2.wheels)

c1.mileage = 8
c1.wheels = 5

print("mileage: ",c1.mileage," Company: ",c1.company," wheels: ",c1.wheels)
print("mileage: ",c2.mileage," Company: ",c2.company," wheels: ",c2.wheels)

car.wheels = 5
print("mileage: ",c1.mileage," Company: ",c1.company," wheels: ",c1.wheels)
print("mileage: ",c2.mileage," Company: ",c2.company," wheels: ",c2.wheels)
