import pandas as pd
data={
    'Name': ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age' : [22,21,23,20,24],
    'Marks':[85,92,78,83,73],
    'City':['Bhopal','Indore','Bhopal','Jabalpur','Indore'],

}
df=pd.DataFrame(data)
print(df)

# print(df.shape) #5 by 4 matrix created
# print(df.head(3))#starting 3 row
# print(df.dtypes)#data type of each column
# print(df.describe())#statical summary

#select columns
print("df['Name']:\n ",df['Name'])
print(df[['Name','Marks']])#multi column

# Filter rows
print(df[df['Marks']>=85])
print(df[df['City']=='Bhopal'])

print(df[(df['Marks']>=80) & (df['City']=='Indore')])

#make function
def get_grade(x):
    if x>=90:
        return 'A'
    elif x>= 75:
        return 'B'
    else:
        return 'C'
    
df['Grade']=df['Marks'].apply(get_grade)
print(df['Grade'])
print("--------------")
print(df)

city_avg=df.groupby('City')['Marks'].mean()
print(city_avg)

#read real csv file
df2=pd.read_csv('student.csv')
#cleanning
df2['Name'] = df2['Name'].str.strip()
df2.to_csv('clean_output.csv',index=False)
print(df2)

