import pandas as pd 

def fun1(data1):
    d1 = pd.DataFrame(data1)
    print(d1)

def fun2(data1):
    d1 = pd.DataFrame(data1)
    # print(d1.loc[1])
    print(d1.loc[[1,2]])

def fun3(data1):
    d1 = pd.DataFrame(data1,index=["aa","bb","cc","dd"])
    print(d1)

def fun4(data1):
   d1 = pd.DataFrame(data1,index=["aa","bb","cc","dd"])
   print(d1.loc["aa"])
   print(d1.loc["bb"])
    

if __name__ == "__main__":
    data1 = {
        "a":["hello","hi","how","what"],
        "b":[1,2,3,4]
    }
    # fun1(data1)
    # fun2(data1)
    # fun3(data1)
    fun4(data1)