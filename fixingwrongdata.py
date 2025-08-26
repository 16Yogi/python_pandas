import pandas as pd 

def title():
    print("Fixing wrong Data")
    print("-----------------------------")

def fun1(d1):
    for i in d1.index:
        if d1.loc[i,"Duration"] > 60:
            d1.loc[i,"Duration"] = 60
            print(d1.to_string())

def fun2(d1):
    for i in d1.index:
        if d1.loc['Duration'] < 120:
            d1.drop(i,inplace=True)
            print(d1.to_string())
            
if __name__ == "__main__":
    # d1 = pd.read_json('./Dataset/iris.json')
    # print(d1.to_string())
    d1 = pd.read_csv('./Dataset/data.csv')
    # print(d1.to_string())
    title()
    fun1(d1)
