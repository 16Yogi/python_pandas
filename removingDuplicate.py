import pandas as pd 

def title():
    print("Removing Duplicate")
    print("---------------------------")

def fun1(d1):
    data = d1.to_string()
    print(data)

def fun2(d2,d1):
    data1 = d2.drop_duplicates(inplace=True)
    data2 = d1.drop_duplicates(inplace=True)
    print(f"{data1}  -   {data2}")

if __name__ == "__main__":
    d1 = pd.read_csv("Dataset/data.csv")
    d2 = pd.read_json("Dataset/iris.json")
    
    title()
    # fun1(d1)
    fun2(d2,d1)