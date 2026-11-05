import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Employee_Dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)

# ---Numerical vs Numerical analysis---
#Age vs Salary
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.scatterplot(data=df, x='Age', y='Salary', ax=axes)
axes.set_title("Age vs Salary")
axes.set_xlabel("Age")
axes.set_ylabel("Salary")
plt.show()

# ---Categorical vs Numerical analysis---
#Department vs Salary
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='Department', y='Salary', ax=axes)
axes.set_title("Department vs Salary")
axes.set_xlabel("Department")
axes.set_ylabel("Salary")
plt.show()
#Region vs Salary
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='Region', y='Salary', ax=axes)
axes.set_title("Region vs Salary")
axes.set_xlabel("Region")
axes.set_ylabel("Salary")
plt.show()
#Performance Score vs Salary
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='Performance_Score', y='Salary', ax=axes)
axes.set_title("Performance Score vs Salary")
axes.set_xlabel("Performance Score")
axes.set_ylabel("Salary")
plt.show()
#Remote Work vs Salary
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='Remote_Work', y='Salary', ax=axes)
axes.set_title("Remote Work vs Salary")
axes.set_xlabel("Remote Work")
axes.set_ylabel("Salary")
plt.show()
#Status vs Salary
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.boxplot(data=df, x='Status', y='Salary', ax=axes)
axes.set_title("Status vs Salary")
axes.set_xlabel("Status")
axes.set_ylabel("Salary")
plt.show()

# ---Categorial vs Categorical analysis---
#Department vs Status
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
ds = pd.crosstab(df['Department'], df['Status'])
sns.heatmap(data=ds, annot=True, ax=axes)
axes.set_title("Department vs Status")
plt.show()
#Department vs Performance Score
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
dp = pd.crosstab(df['Department'], df['Performance_Score'])
sns.heatmap(data=dp, annot=True, ax=axes)
axes.set_title("Department vs Performance Score")
axes.set_xlabel("Performance Score")
plt.show()
#Remote Work vs Status
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.countplot(data=df, x='Remote_Work', hue='Status', ax=axes)
axes.set_title("Remote Work vs Status")
axes.set_xlabel("Remote Work")
axes.set_ylabel("Count")
plt.show()
