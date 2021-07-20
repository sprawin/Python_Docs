class Student:
    def __init__(self,**data):
        for i,j in data.items():
            if(i == "name"):
                self.name = j
            if(i=="age"):
                self.name = j
            if(i=="mobile"):
                self.mobile = j
            if i not in {"name","age","mobile"}:
                print("contact your developer. Only name, age and mobile are available.")
                
        
    def show(self):
        print(self.name, self.mobile)
            

            
s1 = Student(name = "Praveen", age = 23, mobile = "9486185751")
s1.show()