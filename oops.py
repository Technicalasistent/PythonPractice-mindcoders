# class ThisIsMyFirstClass :
#     name="pratikshit"
#     age=19

#     def getname(self):
#         print(self.name)

# firstObject=ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getname()
# print(firstObject.name)

# class Student:
#     def __init__(self,name,age,gender,grade,place):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.grade=grade
#         self.place=place

#     def printDetails(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.grade)
#         print(self.place)

# Pratikshit=Student("Pratikshit Asthana",19,"male","final year","Bihar")
# print(Pratikshit)
# Pratikshit.printDetails()

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

# class ExampleClass:
#     def __init__(self,val=1):
#         self.first=val

#     def set_second(self,val):
#         self.second=val

# example_object_1=ExampleClass()
# example_object_2=ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3=ExampleClass(4)
# example_object_3.third=5

# print(example_object_1)
# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# class classy:
#     def method(self,par):
#         print("method",par)
# obj=classy()
# obj.method(1)

# class classy:
#     varia=2
#     def method(self):
#         print(self.varia,self.var)
# obj=classy()
# obj.var=3
# obj.method()

# class star:
#     def __init__(self,name,galaxy):
#         self.name=name
#         self.galaxy=galaxy
#     def __str__(self):
#         return self.name+ " in " +self.galaxy
# sun=star("sun","milky way")
# print(sun)

# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass

# for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
#     for cls2 in [Vehicle,LandVehicle,TrackedVehicle]:
#         print(issubclass(cls1,cls2), end="\t")
#     print()

# class super:
#     supVar=1
# class sub(super):
#     subVar=2
# obj=sub()
# print(obj.supVar)
# print(obj.subVar)

# class Super:
#     def __init__(self):
#         self.supVar=11
# class Sub(Super):
#     def __init__(self):
#         super().__init__()
#         self.subVar=12
# obj=Sub()
# print(obj.subVar)
# print(obj.supVar)

class Level1:
    variable_1=100
    def __init__(self):
        self.var_1=101
    def fun_1(self):
        return 102
    
class Level2(Level1):
    variable_2=200
    def __init__(self):
        super(). __init__()
        self.var_2=201
    def fun_2(self):
        return 202
    
class Level3(Level2):
    variable_3=300
    def __init__(self):
        super().__init__()
        self.var_3=301
    def fun_3(self):
        return 302
obj=Level3()

print(obj.variable_1,obj.var_1,obj.fun_1())
print(obj.variable_2,obj.var_2,obj.fun_2())
print(obj.variable_3,obj.var_3,obj.fun_3())



