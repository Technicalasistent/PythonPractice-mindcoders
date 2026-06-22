import matplotlib.pyplot as plt

# months=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
# sales=[45,52,48,61,58,72,69,75,68,82,90,95]

# plt.figure(figsize=(12,5))
# plt.plot(months,sales,marker='+',color='steelblue',linewidth=2,markersize=8)
# plt.fill_between(months,sales,alpha=0.15,color='steelblue')
# plt.title('monthly sales 2024(Rs. Thousands)',fontsize=14,fontweight='bold')
# plt.xlabel('months')
# plt.ylabel('sales (Rs. K)')
# plt.grid(True,alpha=0.3)
# plt.tight_layout()
# plt.show()


#bar graph
teams=['chennai','mumbai','rcb','kkr','hyderabad']
trophy=[5,5,2,3,1]
colors=["#DBF321","#4C57AF","#FF0000","#B05227","#F44336"]

# Bar Chart
plt.figure(figsize=(9,5))
bars=plt.bar(teams,trophy,color=colors,edgecolor='white',linewidth='1.5')
plt.title('IPL RECORDS')
plt.ylabel('Number of trophies')
plt.xlabel(teams)
for bar,val in zip(bars,trophy):
    plt.text(bar.get_x()+bar.get_width()/2,val+30,str(val),ha='center',fontweight='bold')
plt.tight_layout()
plt.show()

# plot chart
# import numpy as np
# #scatter plot
# study_hrs=np.random.uniform(2,10,50)
# marks=study_hrs*7+np.random.normal(0,8,50)
# marks=np.clip(marks,30,100)

# plt.figure(figsize=(8,5))
# plt.scatter(study_hrs,marks,c=marks,cmap='RdYlGn',s=100,alpha=0.8)
# plt.colorbar(label='Marks')
# plt.title('Study hours vs exam marks')
# plt.xlabel('Study hours/day')
# plt.ylabel('Exam Marks')
# plt.show()