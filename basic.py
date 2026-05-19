print("Hello Praatikshit")
#print("hello")
# bfsldn
# jnflsdn
# kfksdkmd
# vknfdkn.
# jfkdnv
'''guldzshj
vjklzdsvn
ldznv
jndfkzn'''
#age="four"
# print(age)

name="pratikshit"
profession="engineering"
experiance=100
print("i am ",name,"and my profession is",profession,"and","i have", experiance,"years of experiance")
x=5
print(type(x))
x="hello"
print(x)
x=["hello","teshu",18]
print(x)
x=20
print(x)

x=20.5
print(x)

x=("apple","mac","window")
print(x)
x=range(0,4)

print(x)
x={"name" : "teshu","age":18}
print(x)

x={"apple","fruit","mango"}
print(x)

x=frozenset({"apple","mango"})
print(x)

x=True
print(x)

x=b"hello"
print(x)

x=bytearray(5)
print(x)

x=memoryview(bytes(5))
print(x)

x=None
print(x)

x=10
y=10
print(x<5 and x>1)
print(x>5 or x>10)
print(x<5 or x>5)
print(not(x>3 or x>10))
print(x is y)

x=["land cruiser","BMW"]
y=["land cruiser","BMW"]
z=x
print(x is y)
print(x is z)

print(x is not y)
print(x is not z)

x="maruti"
y=x
print(y in x)
print(y not in x)

name=input("please enter your name ")
print("hello",name)

x=input("enter first no. ")
y=input("enter second no. ")
z=int(x)+int(y)
print(x+y)
print(z)

a=int(input("enter first side "))
b=int(input("enter second side "))
h=(a**2+b**2)**0.5
print("hypotenious = ", h)

print("+"+"-"*10+"+")
print(("|"+" "*10+"|\n")*5, end="")
print("+"+"-"*10+"+")

num1=int(input("first number "))
num2=int(input("second number "))
if num1>num2:
    large_num=num1
else:
    large_num=num2
print("large no. is " ,large_num)

num1=int(input("first number "))
num2=int(input("second number "))
num3=int(input("third number "))
# large_num=num1
# if num2>large_num:
#     large_num=num2
# if num3>large_num:
#     large_num=num3
large_num=max(num1,num2,num3)
small_num=min(num1,num2,num3)
print("largest no. is ",large_num)
print("smallest no. is ",small_num)

str1=input("enter the name of plant ")
if(str1=="spathiphellum"):
    str1="No, I want a big Spathiphyllum"
elif(str1=="SPATHIPHELLUM"):
    str1="Yes - Spathiphyllum is the best plant ever!"
elif(str1=="input"):
    str1="spethiphellum"
print(str1)

largest_num=-99999999
number=int(input("enter a number or type -1 to stop "))
while number != -1:
    if number>largest_num:
        largest_num = number
    number=int(input("enter a number or type -1 to stop "))

print("the largest no. is ",largest_num)

num=int(input("enter num "))
count=1
while count<=num:
    print(count ,end=" ")
    count+=1




