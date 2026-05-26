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

# list.reverse()
# print(list)

# list_1=[1]
# list_2=list_1[:]
# list_1[0]=2
# print(list_1)
# print(list_2)

my_list=[10,8,6,4,2]
my_list=my_list[1:3]
print(my_list)
new_list=my_list[1:-1]
print(new_list)
new_list=my_list[-5:2]
print(new_list)
del my_list[1:3]
print(my_list)
del my_list[0:]
print(my_list)
print(5 in my_list)
print(5 not in my_list)
print(8 in my_list)

row=[]
for i in range(8):
    row.append("white pawn")
print(row)

row=["white pawn"for i in range(8)]
squares=[x**2 for x in range(10)]
print(row)
print(squares)
twos=[2**i for i in range(8)]
print(twos)
odds=[element for element in squares if element%2!=0]
print(odds)

board=[]
for i in range(8):
    row=["empty"for i in range(8)]
    board.append(row)
for element in board:
    print(element)
print(len(board))

board[0][0]="ROOKS"
board[0][7]="ROOKS"
board[7][0]="ROOKS"
board[7][7]="ROOKS"
print("---------------")
for element in board:
    print(element)

board[0][1]="KNIGHT"
board[0][6]="KNIGHT"
board[7][1]="KNIGHT"
board[7][6]="KNIGHT"
print("---------------")
for element in board:
    print(element)

temp=[[0.0 for h in range(24)] for d in range(31)]
temp1=30
temp2=32
count=0
for days in temp:
    if count==0:
        days[11]=temp1
        count=1
    else:
        days[11]=temp2
        count=0
for element in temp:
    print(element) 
total=0.0
for days in temp:
    total+=days[11]
average=total/31
print("averge is ",average)
highest=-100
for days in temp:
    for temp in days:
        if temp>highest:
            highest=temp
print("highest temp is ",highest)
# hot_days=0
# for day in temp:
#     if days[11]>20.0:
#         hot_days+=1
# print("hotest days are ",hot_days)

rooms=[[[False for r in range(20)] for f in range(15)] for t in range(3)]
print(rooms)
rooms[1][9][13]=True
rooms[1][9][1]=True
vacancy=0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy+=1
print("vacany in 3rd 15th floor of 3rd building ",vacancy)





