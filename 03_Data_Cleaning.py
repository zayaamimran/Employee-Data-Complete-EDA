import numpy as np
import pandas as pd

df = pd.read_csv("Messy_Employee_dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)
print(df.shape)

#Handle missing values
#Age
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'].isna().sum())
#Salary 
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df['Salary'].isna().sum())

#Splitting Department_Region into two columns 
df[['Department', 'Region']] = df['Department_Region'].str.split('-', expand=True)
df = df.drop(columns='Department_Region')

#Confirmation
print(df)
print(df.isna().sum())
print(df.dtypes)
print(df.shape)

#Saving 
df.to_csv("Cleaned_Employee_Dataset.csv", index=False)