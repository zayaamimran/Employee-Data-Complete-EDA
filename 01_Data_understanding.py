import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv("Messy_Employee_dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)

print(df.dtypes)

#Dataset Dimensions
print(df.shape)
print(df.size) #11220 

#Dataset Inspection
print(df.head(5))
print(df.tail(5))
print(df.loc[500 : 510 : 1])
print(df['Join_Date'])
print(df['Join_Date'].loc[500 : 510 : 1])
print(df.sample(10))
print(df.dtypes)
print(df.info())

#Descriptive Analysis
print(df.describe())
print(df[['Age', 'Salary']].describe())
print(df.nunique())
print(df.nunique().idxmin())

cat_columns = ['Department_Region', 'Status', 'Performance_Score', 'Remote_Work']
print(df[cat_columns])
print(df[cat_columns].describe())
print(df[cat_columns].count())
print(df[cat_columns].nunique())

#Variable Classification
var_class = {
    'Numerical' : ['Age', 'Salary'],
    'Categorical' : ['Department_Region', 'Status', 'Performance_Score', 'Remote_Work'],
    'Datetime' : 'Join_Date',
    'Identifier' : ['Employee_ID', 'Phone', 'Email'],
    'Text' : ['First_Name', 'Last_Name']
}

print((df['Status']=='Active').sum())
print((df['Status']=='Pending').sum())
print((df['Status']=='Inactive').sum())
print((df['Remote_Work']==False).sum())
print((df['Remote_Work']==True).sum())
