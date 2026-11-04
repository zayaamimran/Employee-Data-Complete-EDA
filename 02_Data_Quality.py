import numpy as np
import pandas as pd

df = pd.read_csv("Messy_Employee_dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)

#Missing Values
print((df.isna()).sum())
print((df.isna()).mean()*100)
print((df.isna().sum().sum()/df.size)*100)

#Duplicate Investigation 
print(df.duplicated())
print("Duplicated rows :",(df.duplicated().sum()))
print(df['Employee_ID'].duplicated().sum())
print(df['Email'].duplicated().sum())
print(df['Phone'].duplicated().sum())
print(df['Email'].duplicated().mean()*100)
print(df.groupby('Employee_ID').nunique())

#Numerical Data Validation
Num_Data = ['Age', 'Salary']
print(df[Num_Data].min())
print(df[Num_Data].max())
print((df[Num_Data]<0).sum())
print((df[Num_Data] == 0).sum())
q1, q3 = df['Salary'].quantile([0.25, 0.75])
iqr = q3 - q1
lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr

df['salary_outlier'] = (df['Salary'] < lower) | (df['Salary'] > upper)

print(df['salary_outlier'].sum(), "potential outliers")
df[df['salary_outlier']].sort_values('Salary')

#Categorical Data Investigation 
cat_columns = ['Department_Region', 'Status', 'Performance_Score', 'Remote_Work']
print(df[cat_columns].nunique())
print(df[cat_columns].describe())
# Summary of space counts per column
space_counts = df.select_dtypes(include='object').apply(lambda x: (x.str.strip() != x).sum())
print(space_counts)
print(df.value_counts())

#Date Investigation 
print("Missing dates : ", df['Join_Date'].isna().sum())
Invalid_date = df['Join_Date'].isna().any()
print(Invalid_date)
today = pd.Timestamp.today()
future_dates = df[df["Join_Date"] > today]
print("Suspicious future dates:", len(future_dates))
print(future_dates)
