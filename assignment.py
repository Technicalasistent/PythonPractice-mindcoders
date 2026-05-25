name1="sohan"
name2="mohan"
name3="vinod"
course1="b.tech"
course2="mbbs"
course3="ca"
age1=20
age2=23
age3=24
print("name of first student ",name1,"\ncourse of first student ",course1,"\nage ",age1)
print("name of second student ",name2,"\ncourse of second student ",course2,"\nage ",age2)
print("name of third student ",name3,"\ncourse of third student ",course3,"\nage ",age3)

# a=int(input("enter 1st num "))
# b=int(input("enter 2nd num "))
# print(a/b)

# ch=input("enter a ch ")
# print(ord(ch))

# a=int(input("enter 1st num "))
# b=int(input("enter 2nd num "))
# print(a**b)

print(("*")*10)
print(("*"+" "*8+"*\n")*5 ,end="")
print(("*")*10)

print(("########\n")*10)

print(" "*4+"*"+" "*4)
print(" "*3+"*"" ""*"+" "*3)
print(" "*2+"*""   ""*"+" "*2)
print(" "*1+"*""     ""*"+" "*1)
print("*"*3+" "*3+"*"*3)
print(" "*2+"*"+"   "+"*"+" "*2)
print(" "*2+"*"+"   "+"*"+" "*2)
print(" "*2+"*"*5+" "*2)

print("1"+" "*5)
print("2"*2)
print("3"*3)
print("4"*4)
print("5"*5)
print("6"*6)

print("#"*10)
print(("#"+" "*8+"#\n")*5,end="")
print("#"*10)

print("*******\n"*5)

# for i in range(1,51):
#     print(i,end=" ")

# for i in range(1,51):
#     if i==50:
#         print("50")
#     elif i%2==0:
#         print("t",end=" ")
#     elif i%2!=0:
#         print(i,end=" ")
    
# for i in range(1,51):
#         if i%3==0:
#             print("t",end=" ")
#         else:
#             print(i,end=" ")

for i in range(1,51):
    if i==50:
        print("50")
    elif i%3==0 and i%5==0:
        print("fizbuz",end=" ")
    elif i%3==0:
        print("fiz",end=" ")
    elif i%5==0:
        print("buz",end=" ")
    else:
        print(i,end=" ")

# income=float(input("enter income "))
# if income<0:
#     tax=0
# elif income<=85528:
#     tax=0.18*income-556
# else:
#     tax=14839+(income-85528)*0.32
# print("total tax ",round(tax))

# year=int(input("enter year "))
# if year<1582:
#     print("Not within the Gregorian calendar period.")
# elif year%4!=0:
#     print("common year")
# elif year%100!=0:
#     print("leap year")
# elif year%400!=0:
#     print("common year")

# else:
#     print("leap year")

for i in range(1,6):
    print(i,"mississippily")
print("Ready or not, here I come!")
    
user_word=input("enter word ")
user_word = user_word.upper()
word_without_vowels=""
for letter in user_word:
    if letter=='A':
        continue
    elif letter=='E':
        continue
    elif letter=='I':
        continue
    elif letter=='O':
        continue
    elif letter=='U':
        continue
    word_without_vowels+=letter
print(word_without_vowels)