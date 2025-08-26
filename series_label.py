import pandas as pd 

arr = [1,2,3,4,5]

data1 = pd.Series(arr) 
# print(data)
print(data1[0])
print("---------------------------------------------")

data2 = pd.Series(arr,index = ["a","b","c","d","e"])
print(data2)
print("----------------------------------------------")
print(data2["c"])