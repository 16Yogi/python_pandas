import pandas as pd 
import matplotlib.pyplot as plt 

def title():
    print("Ploting")
    print("---------------------")

def fun1(d1):
    d1.plot()
    plt.show()

if __name__ == "__main__":
    d1 = pd.read_csv('Dataset/data.csv')
    title()
    fun1(d1)