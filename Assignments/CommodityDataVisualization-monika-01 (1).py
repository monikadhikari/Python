
"""
Program : Program to replicate commodity data visualization document
Author : Monika Adhikari
Description : In this code, we are reading a csv file converting into the appropriate format so we can easily perform some visualization and filtering task
on it. The reference of this source code is from commodity.docx. This code is running successfully on jupiter notebook and spyder IDE.

"""

import csv
from datetime import datetime


## Reding the Data from CSV using csv module
with open("produce_csv.csv","r") as csvfile:
  reader=csv.reader(csvfile)
  data=[row for row in reader]


## create a modified Data replace $ values and convert date in proper format
modData=[]
for row in data:
  newRow=list()
  for item in row:
    if '$' in item:
      newRow.append(float(item.replace('$',''))) ## Replacing $ symbol from Price 
    elif '/' in item:
      newRow.append(datetime.strptime(item,'%m/%d/%Y')) #converting string in datetime object
    else:
      newRow.append(item)
  modData.append(newRow)


##convert data in tabular format
locations=modData.pop(0)[2:]
records=list()
for row in modData:
  newRow=row[:2]
  for loc, price in zip(locations,row[2:]):
    records.append(newRow+[loc,price])



### Filtering Data for Text Graph
select=list(filter(lambda x:x[0]=="Oranges" and x[2]=="Chicago",records)) # filter Orange Commodity for Chicago state
dates=[x[1] for x in select] ## selecting date from filtered data
prices=[x[3] for x in select] ## selecting price from filtered data

dpMerge= [[d,p] for d,p in zip(dates,prices)]
dpMerge.sort(key=lambda a:a[0])

for x in dpMerge:
  print(f'{datetime.strftime(x[0],"%m-%d-%Y")} {int(25*x[1])*"="}')


#### Visualization of DATA
'''
for this task we will use matplotlib.pyplot
'''
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot()
ax.plot(dates,prices,label="Oranges in Chicago")
ax.set_xlabel('data')
ax.set_ylabel('price in dollars')
plt.legend()
plt.show()


## Formating the yaxis price in $<price>

import matplotlib.ticker as mtick
fig=plt.figure()
ax=fig.add_subplot()
ax.plot(dates,prices,label="Oranges in Chicago")
ax.set_xlabel('data')
ax.set_ylabel('price in dollars')
fmt='${x:,.2f}'
tick=mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
plt.legend()
plt.show()