'''
Program : Final Project
Author : Monika Adhikari

Description: Commodity data analysis using plotly
'''



import csv
from datetime import datetime

print("==============================================")
print("Analysis of commodity Data")
print("==============================================")
print()

## Reding the Data from CSV using csv module
with open("produce_csv.csv","r") as csvfile:
  reader=csv.reader(csvfile)
  data=[row for row in reader]
### First 8 rows of datafile without modify
print("THE FIRST 8 ROWS FROM THE DATA FILE ...")
for index,item in enumerate(data):
  if index==8:
    break
  print(data[index])


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


print() # For new Line
### First 8 rows of datafile without modify
print("THE FIRST 8 ROWS FROM THE CONVERTED DATA ...")
for index,item in enumerate(modData):
  if index==8:
    break
  print(modData[index])


##convert data in tabular format
locations=modData.pop(0)[2:]
records=list()
for row in modData:
  newRow=row[:2]
  for loc, price in zip(locations,row[2:]):
    records.append(newRow+[loc,price])
   
print() # For new Line
print("THE FIRST 20 DATA RECORDS ...")
for index,item in enumerate(records):
  if index==20:
    break
  print(records[index])



## List of products
productList=[item[0] for item in records]
uproductList=list(set(productList))

## print Product Menu

print("SELECT PRODUCTS BY NUMBER ...")
countPrint=0
for index,item in enumerate(uproductList):
  if countPrint==3:
    countPrint=0
    print()
  print(f'<{index}> {uproductList[index]}',end="\t")
  countPrint+=1


print() # For new Line
chooseProductIndex=[int(i) for i in input("Enter product numbers separated by spaces: ").split()]
chooseProductList=[ uproductList[item] for item in chooseProductIndex ]

print("Selected products: ",end="")
for product in chooseProductList:
  print(product,end=" ")


#=================================================
## List of Date
print() # For new Line
dateList=[item[1].strftime("%Y-%m-%d") for item in records]
udateList=list(set(dateList))
udateList.sort(key = lambda date: datetime.strptime(date, '%Y-%m-%d')) 


print("SELECT Date BY NUMBER ...")
countPrint=0
for index,item in enumerate(udateList):
  if countPrint==3:
    countPrint=0
    print()
  print(f'<{index}> {udateList[index]}',end="\t")
  countPrint+=1


print() # For new Line
print(f'Earliest available date is: {udateList[0]}')
print(f'Latest available date is: {udateList[-1]}')

chooseDateIndex=[int(i) for i in input("Enter start/end date numbers separated by a space: ").split()]

chooseDateList=[ udateList[item] for item in chooseDateIndex ]

print("Selected products: ",end="")
print(f'Dates from {chooseDateList[0]} to {chooseDateList[1]}')
for index,item in enumerate(chooseDateList):
  chooseDateList[index]=datetime.strptime(item,'%Y-%m-%d')
print("\n") # For new Line
#=================================================
## List of Locations
locationList=[item[2] for item in records]
ulocationList=list(set(locationList))
print("SELECT Locations BY NUMBER ...")
for index,item in enumerate(ulocationList):
  print(f'<{index}> {ulocationList[index]}')



print() # For new Line
chooseLocationIndex=[int(i) for i in input("Enter location numbers separated by spaces: ").split()]
chooseLocationList=[ ulocationList[item] for item in chooseLocationIndex ]
print("Selected locations: ",end="")
for loc in chooseLocationList:
  print(loc,end=" ")
print("\n") # For new Line




dataFilter=[item for item in records if item[0] in chooseProductList and (item[1]>= chooseDateList[0] and item[1]<= chooseDateList[1])  and item[2] in chooseLocationList ]


for index,item in enumerate(dataFilter):
  print(f'<{index}> {item}')


### print stats of data
for pro in chooseProductList:
  for loc in chooseLocationList:
    print()
    counter=0
    for item in dataFilter:
      if item[0]==pro and item[2]==loc:
        counter+=1
    if counter>0:
      print(f'{counter} pieces for {pro} in {loc}')




## DATA Visualization 
import plotly.offline as py
import plotly.graph_objs as go

datadict={}
for pro in chooseProductList:
  for loc in chooseLocationList:
    counter=0
    sum=0
    for item in dataFilter:
      if item[0]==pro and item[2]==loc:
        counter+=1
        sum+=item[3]
    if counter>0:
      datadict[(pro,loc)]=sum/counter



## Generating Bar Graph
data=[]
for loc in chooseLocationList:
  x=[]
  y=[]
  name=loc
  for pro in chooseProductList:
    x.append(pro)
    y.append(datadict[(pro,loc)])
  trace=go.Bar(x=x,y=y,name=name)
  data.append(trace)

graphTitle=f'Product prices from {chooseDateList[0].strftime("%Y-%m-%d")} through {chooseDateList[1].strftime("%Y-%m-%d")}'
layout=go.Layout(barmode='group',title= graphTitle)
fig=go.Figure(data=data,layout=layout)
py.plot(fig,filename="graph-visual.html")

