import pandas as pd 

arr = [1,2,3,4,5]
data = pd.Series(arr)

print(data)
print("------------------------")
for i in data:
    print(i)