import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

df=pd.DataFrame({
    'marks' :       np.random.randint(40,100,100),
    'study_hours' : np.random.uniform(2,10,100),
    'city'        : np.random.choice(['Bhopal','Indore','Jabalpur'],100),
    'gender' : np.random.choice(['Male','Female'],100)
    })
# histogram
# plt.figure(figsize=(10,4))
# sns.histplot(df['marks'],bins=20,kde=True,color='steelblue')
# plt.title('Distribution of student marks')
# plt.show()

# Box Plot
# sns.boxplot(data=df,x='city',y='marks',palette='Set1')#palette is used for color
# plt.title('marks distribution by city')
# plt.show()

#corelation heat map
# plt.figure(figsize=(5,4))
# sns.heatmap(df[['marks','study_hours']].corr(),annot=True,cmap='prism',vmin=-1,vmax=1)
# plt.title('correlation matrix')
# plt.show()

#pair plot
sns.pairplot(df[['marks','study_hours']],diag_kind='kde')
plt.show()