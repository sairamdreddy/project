import pandas as pd
df = pd.read_csv("employee_salary.csv")

'''Q1'''
print("\n1.First 5 Records:")
print(df.head())
print("\n2.Last 5 Records:")
print(df.tail())
print("\n3.Dataset Shape:", df.shape)
print("4.Number of Records:", df.shape[0])
print("5.Number of Features:", df.shape[1])

'''Q2'''
print("\n6.Column Names:")
print(df.columns)
print("\n7.Data Types:")
print(df.dtypes)
print("\n8.Dataset Information:")
df.info()
print("\n9.Descriptive Statistics:")
print(df.describe())
print("\n10.Average Employee Salary:")
print(df["Salary"].mean())
print("\n11.Standard Deviation:")
print(df.std(numeric_only=True))

'''Q3'''
print("\n12.Number of Missing Values:")
print(df.isnull().sum())
print("\n13.Percentage of Missing Values:")
print((df.isnull().sum() / len(df)) * 100)
print("\n14.Number of Duplicate Records:")
print(df.duplicated().sum())
print("\n15.Dataset Size Before Cleaning:", len(df))
df_cleaned = df.drop_duplicates()
print("16.Dataset Size After Cleaning:", len(df_cleaned))
print("\n17.Column with Highest Missing Values:")
print(df.isnull().sum().idxmax())