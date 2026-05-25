# num1=int(input("first number "))
# num2=int(input("second number "))
# if num1>num2:
#     large_num=num1
# else:
#     large_num=num2
# print("large no. is " ,large_num)

# num1=int(input("first number "))
# num2=int(input("second number "))
# num3=int(input("third number "))
# large_num=num1
# if num2>large_num:
#     large_num=num2
# if num3>large_num:
#     large_num=num3
# large_num=max(num1,num2,num3)
# small_num=min(num1,num2,num3)
# print("largest no. is ",large_num)
# print("smallest no. is ",small_num)

# str1=input("enter the name of plant ")
# if(str1=="spathiphellum"):
#     str1="No, I want a big Spathiphyllum"
# elif(str1=="SPATHIPHELLUM"):
#     str1="Yes - Spathiphyllum is the best plant ever!"
# elif(str1=="input"):
#     str1="spethiphellum"
# print(str1)

# num=int(input("enter num "))
# count=1
# even=0
# odd=0
# while count<=num:
#     if count%2==0:
#         even+=1
#     else:
#         odd+=1
#     count+=1
# print("total even no. is " ,even)
# print("total odd no. is " ,odd)


# for counter in range(100):
#     print("counter ", counter)

# for counter in range(2,8,3):
#     print("counter ",counter)

# power=1
# for expo in range(16):
#     print("2 to the power of " ,expo ,"is ",power)
#     power*=2

# print("the break statement ")
# for counter in range(1,6):
#     if counter==3:
#         break
#     print("inside the loop ",counter)
# print("outside the loop")

# print("the continue statement ")
# for counter in range(1,6):
#     if counter==3:
#         continue
#     print("inside the loop ",counter)
# print("outside the loop")

# var=10
# print(var>0)
# print(not(var<=0))

# print(var!=0)
# print(not(var==0))

# num=[10,15,15,12,7]
# print(num)
# print(type(num))

# print("first element content ",num[0])
# print("secodn element content ",num[1])
# print("third element content ",num[2])
# print("fourth element content ",num[3])
# print("fifth element content ",num[4])

# num[0]=50
# print("new num[0] ",num[0])
# print(num)
# num[1]=num[4]
# print(num)

# print(len(num))
# del num[1]
# print(num)
# print(len(num)) 

# print("from last ",num[-1])
# print("from second last ",num[-2])
# print("from third last ",num[-3])

# str1=[1,2,3,4,5]
# print(str1)
# print(len(str1))

# del str1[-1]
# print(str1)
# # x=int(input("enter number "))

# # str1[x]=x
# # print(str1[x])
# # print(str1)

# str1[len(str1//2)]=int(input("enter num "))
# print(str1)

# list=[1,2,3,4,5]
# print(list)
# list.append(10)
# print(list)
# list.insert(0,6)
# print(list)
# del list[1]
# print(list)

# name="pratikshit"
# age=18
# course="b.tech"
# print("my name is ",name,"\nmy age is ",age,"\nand my course is ",course)

# for temp in range(1,7):
#     print(str(temp)*temp)

#     my_list=[1,2,3,4,5,6,7,8,9,10]
#     for iterator in range (len(my_list)):
#         print(my_list[iterator])

# list = []
# for iterator in range (10):
#     list.append(iterator+1)
# print(list)

# list=[10,20,30,40,50,60,70,80,90,100]
# for index in range(len(list)):
#     list[index]+=1
# print(list)

# sum=0
# for index in range(len(list)):
#     sum+=list[index]
# print(sum)

# sum=0
# for element in list:
#     sum += element
# print(sum)

variable1=1
variable2=2
print("variable 1 " ,variable1)
print("variable 2 ",variable2)
variable1,variable2=variable2,variable1
print("variable 1 " ,variable1)
print("variable 2 ",variable2)
    
list=[10,20,30,40,50,60,70,80,90,100]
print(list)
list[4],list[1]=list[1],list[4]
print(list)
