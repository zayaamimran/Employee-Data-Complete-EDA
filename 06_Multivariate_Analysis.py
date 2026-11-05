import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Employee_Dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)

# ---Correlation heatmap---
#Age and Salary
corr = df[['Age', 'Salary']].corr(method='spearman')
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.heatmap(data=corr, annot=True, ax=axes, fmt='.2f', vmin=-1, vmax=1, center=0)
axes.set_title("Spearman Correlation: Age vs Salary")
plt.show()

# ---Salary across Department and Performance Score---
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='Department', y='Salary', hue='Performance_Score', ax=axes)
axes.set_title("Salary across Department and Performance Score")
axes.set_xlabel("Department")
axes.set_ylabel("Salary")
plt.show()

# ---Age vs Salary across Departments---
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', ax=axes)
axes.set_title("Age vs Salary across Departments")
plt.show()

# ---Department, Region and Employment Status---
sns.set_theme(style='whitegrid')
sns.catplot(data=df, x='Department', col='Region', hue='Status', kind='count', height=5, aspect=1.2, col_wrap=3)
plt.show()
