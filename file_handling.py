# with open("data.txt","r") as file:
#     data=file.read()
# print(data)

# with open('students.txt','w') as f:
#     f.write('Rahul Sharma,85,Bhopal\n')
#     f.write('Priya Verma,92,indore\n')
#     f.write('Amit Kumar,90,Jabalpur\n')

# with open('students.txt','a') as f:
#     f.write('Sneha Joshi,88,Bhopal\n')

# with open('students.txt','r') as f:
#     content = f.read()
# print(content)

# with open('students.txt','r') as f:
#     for line in f:
#         name,marks,city=line.strip().split(',')
#         print(f'{name:<15}|{marks:>5}|{city}')
#         print("-----------")

# import csv
# records=[
#     ['Name','Marks','City','Grade'],
#     ['Rahul','85','Bhopal','B'],
#     ['Priya','90','Indore','A'],
#     ['Amit','73','Jabalpur','B'],    
# ]

# with open('student.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# with open('student.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}:{row["Marks"]} Marks({row["City"]})')

import csv
student_records=[
    ['Name','Age','Marks-1','Marks-2','Marks-3'],
    ['Vinod','18','85','90','75'],
    ['Sumit','28','65','80','95'],
    ['Mohit','22','50','70','80'],
]

with open('sd.csv','w',newline='') as f:
    csv.writer(f).writerows(student_records)

# with open('sd.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row["Name"]}:{row["Age"]}:({row["Marks-1"]} marks):({row["Marks-2"]} marks):({row["Marks-3"]} marks)')
name=input("enter name ")
found=False
with open('sd.csv','r') as f:
    for row in csv.DictReader(f):
        if row["Name"]==name:
            print(f'found {name}')
            print(f'{row["Name"]}:{row["Age"]}:({row["Marks-1"]})marks:({row["Marks-2"]})marks:({row["Marks-3"]})marks')
            found=True
            break
if not found:
    print("student not found")
