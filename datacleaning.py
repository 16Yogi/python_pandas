import pandas as pd 

def fun1():
    print("Data cleaning")
    print("---------------------")

def removedata(d1):
    data = d1.dropna()
    print(data.to_string())   

def removenullval(d1):
    # data = d1.dropna(inplace = True)
    d1.dropna(inplace = True)
    print(d1.to_string())

def replaceemptyval(d1):
    data = d1.fillna(10000,inplace=True)
    print(data.to_string())

def replacespecificcol(d1):
    d1.fillna({"petalWidth":2000},inplace=True)
    print(d1.to_string())

def meanmedianmode(d1):
    data = d1["sepalLength"].mean()
    d1.fillna({"sepalLength":data,"sepalWidth":2000},inplace=True)
    print(d1.to_string())

def median(d1):
    me1 = d1["sepalLength"].mean()
    md1 = d1["sepalWidth"].median()
    d1.fillna({"sepalLength":me1,"sepalWidth":md1},inplace=True)
    print(d1.to_string())

def modefun(d1):
    me1 = d1["sepalLength"].mean()
    md1 = d1["sepalWidth"].median()
    mode1 = d1["petalLength"].mode()
    d1.fillna({"sepalLength":me1,"sepalWidth":md1,"petalLength":mode1},inplace=True)
    print(d1.to_string())

if __name__ == "__main__":
    d1 = pd.read_json('Dataset/iris.json') 
    fun1()
    # removedata(d1)
    # removenullval(d1)
    # replacespecificcol(d1)
    # meanmedianmode(d1)
    # median(d1)
    modefun(d1)