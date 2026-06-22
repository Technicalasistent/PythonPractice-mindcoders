# def messaage():
#     print("enter a value ")
# messaage()
# a=int(input())
# messaage()
# b=int(input())
# messaage()
# c=int(input())

# def message():
#     print("enter a value ")

# print("we start here")
# print(message)
# message()
# print("we end here")
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

# def adding(a,b,c):
#     print(a,"+",b,"+",c,"=",a+b+c)
# adding(1,2,3)
# adding(c=1,b=2,a=3)
# adding(3,b=2,c=1)
# # adding(3,a=1,b=2)

# def happy_new_year(wishes=True):
#     print("three...")
#     print("two...")
#     print("one...")
#     if not wishes:
#         return
#     print("happy new year")
# happy_new_year(True)

# def boring_func():
#     print("boaring mode on")
#     return 123
# print("the lesson is interesting")
# boring_func()
# print("the lesson is boaring")

# def check_my_var(variable):
#     if variable==10:
#         print("variable is 10")
#     else:
#         print("variable is not upto the mark")
# check_my_var(5)
# print()

# def list_sum(lst):
#     s=0
#     for elem in lst:
#         s+=elem
#     return s
# print(list_sum([5,7,3]))

# def strange_list_func(n):
#     strange_list=[]
#     for i in range(0,n):
#         # strange_list.insert(0,i)
#         strange_list.append(i+1)
#     return strange_list
# print(strange_list_func(5))

# def scope_test():
#     x=123
# scope_test()
# print(x)

# def my_func():
#     print("do i know that variable? ",var)
# var=1
# my_func()
# print(var)

# def multi(x):
#     var=7
#     return x * var
# var=3
# print(multi(7))

# def my_func():
#     global var
#     var=2
#     print("di i know that variable?",var)
# var=1
# my_func()
# print(var)

# var=2
# print(var)

# def return_var():
#     global var
#     var=5
#     return var
# print(return_var())
# print(var)

# def my_func(n):
#     print("i got",n)
#     n+=1
#     print("i got",n)

# var=1
# my_func(var)
# print(var)

# def my_func(list1):
#     print("print 1",list1)
#     print("print 1",list2)
#     list1=[0,1]
#     print("print 3",list1)
#     print("print 4",list2)
# list2=[2,3]
# my_func(list2)
# print("print 5",list2)

# def my_func(list1):
#     print("print 1",list1)
#     print("print 2",list2)
#     del list1[0]
#     print("print 3",list1)
#     print("print 4",list2)
# list2=[2,3]
# my_func(list2)
# print("print 5",list2)


# def func(n):
#     print(n)
#     if n==0:
#         return
#     else:
#         print("going to recursion",n)
#         func(n-1)
#         print("out of rec",n)
# print("starting rec")
# func(5)
# print("finished rec")

# def fact(n):
#     if n<=0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact)

tuple=(1,10,100)
t1=tuple+(1000,10000)
t2=tuple*3

print(len(t2))
print(t1)
print(t2)
print(10 in tuple)
print(-10 not in tuple)


