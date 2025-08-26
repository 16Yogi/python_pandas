import pandas as pd 

df = pd.read_csv('Dataset/ncr_ride_bookings.csv')
data = df.to_string()
# # print(df)
# print(df.to_string())
print(data)