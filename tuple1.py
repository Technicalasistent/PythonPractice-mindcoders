# tuple=(1,10,100)
# t1=tuple+(1000,10000)
# t2=tuple*3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in tuple)
# print(-10 not in tuple)

# tuple_1=(1,2,3)
# for elem in tuple_1:
#     print(elem)

# tuple_2=(1,2,3,4)
# print(5 in tuple_2)
# print(5 not in tuple_2)

# tuple_3=(1,2,3,4)
# print(len(tuple_3))
# print(5 not in tuple_3)

# tuple_4=tuple_1+tuple_2
# tuple_5=tuple_3*2
# print(tuple_4)
# print(tuple_5)

# my_tuple=tuple((1,2,"string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list=[2,4,6]
# print(my_list)
# print(type(my_list))
# tup=tuple(my_list)
# print(tup)
# print(type(tup))

# var=123
# t1=(1,)
# t2=(2,)
# t3=(3,var)
# t1,t2,t3=t2,t3,t1
# print(t1,t2,t3)
# print(type(t1),type(t2),type(t3))

# dictionary={
# "cat":"chat",
# "dog":"chien",
# "horse":"cheval"
# }
# phone_no={'boss':123456789,'suzy':452697853}
# empty_dictionary={}

# print(dictionary)
# print(type(dictionary))
# print(phone_no)
# print(type(phone_no))
# print(empty_dictionary)
# print(type(empty_dictionary))
# print(dictionary['cat'])
# print(phone_no['suzy'])

# words=['cat','lion','horse']
# for word in words:
#     if word in dictionary:
#         print(word,"-->",dictionary[word])
#     else:
#         print("----",word,"not in dictionary","----")
# print(dictionary.keys())

# for key in dictionary.keys():
#     print(key,"-->",dictionary[key])

# print(dictionary.items())
# for key,value in dictionary.items():
#     print(key,"-->",value)

# print(dictionary.values())

# for value in dictionary.values():
#     print(value)

dictionary_1={
    "zamek":"castle",
    "woda":"water",
    "gleba":"soil"
}
print("dictionary_1",dictionary_1)
copy_dictionary=dictionary_1.copy()
print("copy dictionary",copy_dictionary)
dictionary_1["zamek"]="thala"
item=dictionary_1["zamek"]
print(item)
print(dictionary_1)

phonebook={}
print(phonebook)
phonebook["adam"]=5655698868
print(phonebook)
del phonebook["adam"]
print(phonebook)

dict1={"kwiat":"flower"}
dict1.update(
    {
        "gleba":"soil"
    }
)
print(dict1)
dict1.popitem()
print(dict1)