
import pandas as pd 

def object1(arr):    
    data1 = pd.Series(arr)
    print(data1)
    print(data1["a"])

def object2(arr):
    data1 = pd.Series(arr,index=["a","b","c"])
    print(data1)

def dataFrame(arr2):
    # print(arr)
    data = pd.DataFrame(arr2)
    print(data)

if __name__ == "__main__":
    arr = {"a":11,"b":22,"c":33,"d":44}
    arr2 = {
        "aa":["hello","hi","hihi"],
        "bb":[111,222,333]
    }
    # object1(arr)
    # object2(arr)
    # dataFrame(arr2)