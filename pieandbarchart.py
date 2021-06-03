import matplotlib.pyplot as plt
import pandas as pd
import csv


plt.style.use('bmh')
df = pd.read_csv('new_agent.csv')
print(df)

x = df['Name']
y = df['Call']
z= df['Duration']

#for pie chart.....

plt.pie(y,labels=x,radius=1.2,autopct='%0.02f%%',shadow=True,explode = [.05,.2,.05,.2,.05,.2])

#for bar chart ..

plt.xlabel('Name',fontsize=18)
plt.ylabel('Duration',fontsize=16)
plt.bar(x,z)


plt.show()
#plt.show()






