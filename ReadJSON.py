import pandas as pd 

def fun1(file1):
    data1 = file1.to_string()
    print(data1)

if __name__ == "__main__":
    file1 = pd.read_json('Dataset/iris.json') 
    fun1(file1)