list=[8,10,6,2,4]
# list=[1,2,3,4,5]
# swapped=True
# count=0
# index=0
# while swapped:
#     swapped=False
#     for i in range(len(list)-1-index):
#         index=i
#         count+=1
#         if list[i]>list[i+1]:
#             swapped=True
#             list[i],list[i+1]=list[i+1],list[i]
# print(list)
# print(count)

# list.sort()
# print("sorted list ",list)

list.reverse()
print(list)

list_1=[1]
list_2=list_1[:]
list_1[0]=2
print(list_1)
print(list_2)

my_list=[10,8,6,4,2]
# my_list=my_list[1:3]
# print(my_list)
# new_list=my_list[1:-1]
# print(new_list)
# new_list=my_list[-5:2]
# print(new_list)
# del my_list[1:3]
# print(my_list)
# del my_list[0:]
# print(my_list)
print(5 in my_list)
print(5 not in my_list)
print(8 in my_list)
