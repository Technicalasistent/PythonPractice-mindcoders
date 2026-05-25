# def message():
#     print("enter a value ")
#     temp=int(input())
#     return temp

# print("step 1")
# a=message()
# print("step 2")
# b=message()
# print("step 3")
# c=message()

# print("a: ",a)
# print("b: ",b)
# print("c: ",c)

# def hello(n):
#     print("hello ",n)
# name=input("enter your name ")
# hello(name)

# def message(num):
#     print("enter a num ",num)
# num=12345
# message(1)
# print(num)

# def message(what,number):
#     print("enter",what,"number",number)
# message("telephone",11)
# message(15,"price")
# message("number","number")

# def intro(first_name,last_name):
#     print("my name is ",first_name,last_name)
# intro("pratikshit","asthana")
# intro("sonal","singh")
# intro("sohan","kumar")
# intro(first_name="pratikshit",last_name="asthana")
# intro(last_name="asthana",first_name="teshu")
# intro(last_name="mohan",first_name="geet")

def adding(a,b,c):
    print(a,"+",b,"+",c,"=",a+b+c)
adding(1,2,3)
adding(c=1,b=2,a=3)
adding(3,b=2,c=1)
# adding(3,a=1,b=2)

def happy_new_year(wishes=True):
    print("three...")
    print("two...")
    print("one...")
    if not wishes:
        return
    print("happy new year")
happy_new_year(True)

def boring_func():
    print("boaring mode on")
    return 123
print("the lesson is interesting")
boring_func()
print("the lesson is boaring")

def check_my_var(variable):
    if variable==10:
        print("variable is 10")
    else:
        print("variable is not upto the mark")
check_my_var(5)
print()

def list_sum(lst):
    s=0
    for elem in lst:
        s+=elem
    return s
print(list_sum([5,7,3]))

def strange_list_func(n):
    strange_list=[]
    for i in range(0,n):
        # strange_list.insert(0,i)
        strange_list.append(i+1)
    return strange_list
print(strange_list_func(5))