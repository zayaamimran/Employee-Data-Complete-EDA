import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Employee_Dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)

#Descriptive Statistics
Num_Data = df[['Age', 'Salary']]
print("Mean :\n", Num_Data.mean())
print("Median :\n", Num_Data.median())
print("Mode :\n", Num_Data.mode())
print("Variance :\n", Num_Data.var())
print("Standard deviation :\n", Num_Data.std())
print("Skewness :\n", Num_Data.skew())
print("Kurtosis :\n", Num_Data.kurtosis())

#Correlation Analysis
print("Pearson correlation :")
print(Num_Data.corr(method='pearson'))

print("Spearman correlation :")
print(Num_Data.corr(method='spearman'))
