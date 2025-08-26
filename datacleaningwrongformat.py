import pandas as pd
def title():
    print("Data cleaning with wrong format")
    print("-------------------------------")

def datetimeformat(d1):
    d1['Date'] = pd.to_datetime(d1['Date'],format='mixed')
    print(d1.to_string())

def removerows(d1):
    d1.dropna(subset=['Date'],inplace=True)
    print(d1.to_string())

if __name__ == "__main__":
    d1 = pd.read_csv('Dataset/ncr_ride_bookings.csv')
    title()
    # datetimeformat(d1)
    removerows(d1)