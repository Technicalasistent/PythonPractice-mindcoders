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

# dictionary_1={
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
# }
# print("dictionary_1",dictionary_1)
# copy_dictionary=dictionary_1.copy()
# print("copy dictionary",copy_dictionary)
# dictionary_1["zamek"]="thala"
# item=dictionary_1["zamek"]
# print(item)
# print(dictionary_1)

# phonebook={}
# print(phonebook)
# phonebook["adam"]=5655698868
# print(phonebook)
# del phonebook["adam"]
# print(phonebook)

# dict1={"kwiat":"flower"}
# dict1.update(
#     {
#         "gleba":"soil"
#     }
# )
# print(dict1)
# dict1.popitem()
# print(dict1)

# if "zamek1" in dictionary_1:
#     print("yes zamek1 in dictionary 1")
# else:
#     print("no zamek1 is not in dictionary 1")

# print(dictionary_1)
# print(len(dictionary_1))

# del dictionary_1["zamek"]
# print(dictionary_1)
# print(len(dictionary_1))

# dictionary_1.clear()
# print(dictionary_1)
# print(len(dictionary_1))

# del dictionary_1
# print(dictionary_1)

sd={}

while True:
    name=input("enter student name ")
    if name=="":
        break
    score=int(input(f"enter {name}sore "))
    if score not in range(1,11):
        break
    if name in sd:
        sd[name]+=(score,)
    else:
        sd[name]=(score,)
    # for mark in sd:
    #     print(mark)

print(sd)
for name,mark in sd.items():
    sum=0
    for m in mark:
        sum+=m
        print(name,"-->",sum/len(mark))
