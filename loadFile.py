import pandas as pd 

def fun1(file1):
    data = file1.to_string()
    print(data)

def fun2(file2):
    data = pd.options.display.max_rows
    print(data)

def fun3(file2):
    pd.options.display.max_rows = 9999
    df = file2
    # df = pd.read_csv(file3)
    print(df)

if __name__ == "__main__":
    file1 = pd.read_csv('Dataset/ncr_ride_bookings.csv')
    file2 = pd.read_csv('Dataset/Hearingwell-beingSurveyReport.csv')
    # fun1(file1)
    # fun2(file2)
    fun3(file2)