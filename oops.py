# class ThisIsMyFirstClass :
#     name="pratikshit"
#     age=19

#     def getname(self):
#         print(self.name)

# firstObject=ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getname()
# print(firstObject.name)

class Student:
    def __init__(self,name,age,gender,grade,place):
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade
        self.place=place

    def printDetails(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.grade)
        print(self.place)

Pratikshit=Student("Prarikshit Asthana",19,"male","final year","Bihar")
print(Pratikshit)
Pratikshit.printDetails()

# Pratikshit.name="Prarikshit Asthana"
# Pratikshit.age=19
# Pratikshit.gender="male"
# Pratikshit.grade="final year"
# Pratikshit.place="Bihar"

# print(Pratikshit.name)
# print(Pratikshit.age)
# print(Pratikshit.gender)
# print(Pratikshit.grade)
# print(Pratikshit.place)