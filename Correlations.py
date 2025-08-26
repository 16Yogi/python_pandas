import pandas as pd 

def title():
    print("Correlations")
    print("-------------------------")

# def fun1(d1):
#     data = d1.corr()
#     print(data)

def fun1(d1):
    numeric_data = d1.select_dtypes(include=['number'])  
    data = numeric_data.corr()
    print(data)

if __name__ == "__main__":
    d1 = pd.read_csv('Dataset/data.csv')
    title()
    fun1(d1)