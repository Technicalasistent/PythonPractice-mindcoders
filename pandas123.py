import pandas as pd
data={
    'Name': ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age' : [22,21,23,20,24],
    'Marks':[85,92,78,83,73],
    'City':['Bhopal','Indore','Bhopal','Katni','Indore'],

}
df=pd.DataFrame(data)
print(df)

print(df.shape) #5 by 4 matrix created
print(df.head(3))#starting 3 row
print(df.dtypes)#data type of each column
print(df.describe())#statical summary