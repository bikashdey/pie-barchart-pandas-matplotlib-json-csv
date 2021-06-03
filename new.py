import matplotlib.pyplot as plt
import pandas as pd
import json

#json.load(open('json_data','r'))
#df = pd.read_json('json_data')



with open('json_data','r') as f:
	#df_list = pd.DataFrame(json.load(f))
	df = pd.DataFrame.from_dict(f, orient='index')


print(df)
df.plot(kind='bar')
df.plot.pie(subplots=True)


"""
x = df['Name']
y = df['Call']
z= df['Duration']

#for pie chart.....

plt.pie(y,labels=x,radius=1.2,autopct='%0.02f%%',shadow=True,explode = [.05,.2,.05,.2,.05,.2])

#for bar chart ..

plt.xlabel('Name',fontsize=18)
plt.ylabel('Duration',fontsize=16)
plt.bar(x,z)"""


plt.show()
#plt.show(