from operator import index
import pandas as pd
with open("iris.data") as f:
 data=f.read()
 print(data)
 #data split
 data=data.split("\n")
# print the line
newData= []
#print data in the form of list
for line in data:
     newData.append(line.split(","))
     print(newData)
     print(newData[0][0])

#how to print data in excel
df=pd.DataFrame(newData,columns=['c1','c2','c3','c4','Type'])
#df.to_csv("py.csv", index=False)
df.to_excel("py.xlsx",index=False)