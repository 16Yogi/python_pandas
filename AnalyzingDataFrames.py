import pandas as pd 

def fun1(file1):
    data1 = file1
    print(data1.head(10))

def fun2(file1):
    data1 = file1 
    print(data1.head())

def fun3(file1):
    data1 = file1 
    print(data1.tail())

def fun4(file1):
    data1 = file1
    print(data1.info())

if __name__ == "__main__":
    file1 = pd.read_csv("Dataset/ncr_ride_bookings.csv")

    # fun1(file1)
    # fun2(file1)
    # fun3(file1)
    fun4(file1)