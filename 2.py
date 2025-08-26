import pandas as pd 

arr = {
    "1":["hello","hi","helo"],
    "2":[11,22,33]
}

for i in arr:
    print(i)

print("-------------------------------")

data = pd.DataFrame(arr)
print(data)

print("-------------------------------")

print(pd.__version__)