import pandas as pd
df = pd.read_csv("bank.csv")

print("First five Records :")
print(df.head())

print("Last five Records :")
print(df.tail())
print("Size of the dataset :", df.size)
print("\nDataset shape :", df.shape)

print(df.shape[0])
print(df.shape[1])
print("\nList of coloumns :", df.columns)

print("\nInfo about the dataset :", df.info())
print("\nStatistical Summary :", df.describe())
print("\nNumber of missing values: ",df.isnull().sum())
print("\nMemory used for each coloumn: ", df.memory_usage())