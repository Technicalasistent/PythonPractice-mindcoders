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

# class Level1:
#     variable_1=100
#     def __init__(self):
#         self.var_1=101
#     def fun_1(self):
#         return 102
    
# class Level2(Level1):
#     variable_2=200
#     def __init__(self):
#         super(). __init__()
#         self.var_2=201
#     def fun_2(self):
#         return 202
    
# class Level3(Level2):
#     variable_3=300
#     def __init__(self):
#         super().__init__()
#         self.var_3=301
#     def fun_3(self):
#         return 302
# obj=Level3()

# print(obj.variable_1,obj.var_1,obj.fun_1())
# print(obj.variable_2,obj.var_2,obj.fun_2())
# print(obj.variable_3,obj.var_3,obj.fun_3())


# class Exampleclass:
#     counter=0
#     a=1
#     def __init__(self,val=1):
#         self.__first=val
#         Exampleclass.counter+=1
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1
# example_object=Exampleclass(3)
# example_object_1=Exampleclass()
# example_object_2=Exampleclass(2)
# example_object_3=Exampleclass(4)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)
# print(example_object.a)
# try:
#     print("a = ",example_object.a)
# except AttributeError:
#     try:
#         print("b = ",example_object.b)
#     except AttributeError:
#         print("the error has occured!silently pass")

# if hasattr(example_object,'a'):
#     print("a = ",example_object.a)
# if hasattr(example_object,'b'):
#     print("b = ",example_object.b)

# print(hasattr(Exampleclass,'b'))
# print(hasattr(Exampleclass,'a'))


# class Python:
#     population=1
#     victim=0
#     def __init__(self):
#         self.length_ft=3
#         self.__venomous=False
# myObj=Python()
# print("myObj.population ",myObj.population)
# print("myObj.victim ",myObj.victim)
# print("myObj.length_ft ",myObj.length_ft)
# print("myObj.__venomous ",myObj._Python__venomous)
# # print("myObj.venomous ",myObj.venomous)

# print(hasattr(myObj,'constructor'))

# name mangling 
# class Classy:
#     def visible(self):
#         print("visible")
#     def __hidden(self):
#         print("hidden")

# obj=Classy()
# obj.visible()
# try:
#     obj. __hidden()
# except:
#     print("failed")
#     obj._Classy__hidden()

# print(type(obj))
# print(type(obj).__name__)


# class vehicle:
#     pass
# class landvehicles(vehicle):
#     pass
# class trackedvehicle(landvehicles):
#     pass

# my_vehicle=vehicle()
# my_land_vehicle=landvehicles()
# my_tracked_vehicle=trackedvehicle()

# for obj in [my_vehicle,my_land_vehicle,my_tracked_vehicle]:
#     for cls in [vehicle,landvehicles,trackedvehicle]:
#         print(isinstance(obj,cls),end="\t")
#     print()

# class sampleclass:
#     def __init__(self,val=1):
#         self.val=val
# object_1=sampleclass(0)
# object_2=sampleclass(2)
# object_3=object_1
# object_3.val+=1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val ,object_2.val , object_3.val)

# string_1="mary had a little "
# string_2="mary had a little lamp"
# string_1+="lamp"

# print(string_1==string_2,string_1 is string_2)

# class Super:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return "my name is "+self.name+"."
    
# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)
# obj=Sub("andy")
# print(obj)

# class SuperA:
#     var_a=10
#     def fun_a(self):
#         return 11
# class SuperB:
#     var_b=20
#     def fun_b(self):
#         return 21
    
# class Sub(SuperA,SuperB):
#     pass
# obj=Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())

# class Level1:
#     var=100
#     def fun(self):
#         return 101
    
# class Level2(Level1):
#     var=200
#     def fun(self):
#         return 201
    
# class Level3(Level2):
#     pass

# obj=Level3()
# print(obj.var,obj.fun())

# class Left:
#     var="L"
#     var_left="LL"
#     def fun(self):
#         return "Left"
# class Right:
#     var="R"
#     var_right="RR"
#     def fun(self):
#         return "right"
    
# class Sub(Left,Right):
#     pass
# obj=Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun())

# class One:
#     def do_it(self):
#         print("do it from one")
#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do it from two")
# one=One()
# two=Two()
# one.doanything()
# two.doanything()

# def reciprocal(n):
#     try:
#         n=1/n
#     except ZeroDivisionError:
#         print("division failed")
#         return None
#     else:
#         print("everything went fine") 
#     finally:
#         print("its time to say good bye")
#         return n
    
# print("-----------")
# print("reciprocal(2) ",reciprocal(2))
# print("-----------")
# print("reciprocal(0) ",reciprocal(0))  

# try:
#     i=int("hello")
# except Exception as e:
#     print(e)
#     print(e.__str__())

class MyZeroDivision(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivision("some worse news")
    else:
        raise ZeroDivisionError("some bad news")

do_the_division(False)
do_the_division(True)

