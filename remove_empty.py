import pandas as pd 

def fun1(file1):
    data1 = file1
    newData = data1.dropna()
    print(newData.to_string())

def fun2(file2):
    data1 = file2 
    data1.dropna(inplace=True)
    print(data1.to_string())

def fun3(file2):
    data1 = file2
    data1.fillna(130,inplace=True)
    print(data1.to_string())

def fun4(file2):
    data1 = file2 
    data1.fillna({"Calories": 130}, inplace=True)
    print(data1.to_string())

if __name__ == "__main__":
    file1 = pd.read_csv("Dataset/ncr_ride_bookings.csv")
    file2 = pd.read_json("Dataset/iris.json")
    # print("Hello")
    # fun1(file1)
    # fun2(file2)
    # fun3(file2)
    fun4(file2)

