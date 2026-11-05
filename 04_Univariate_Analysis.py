import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Employee_Dataset.csv", delimiter=',', parse_dates=['Join_Date'], date_format={'Join_Date' : '%m/%d/%Y'})
print(df)

Num_Analysis = df[['Age', 'Salary']]
print(Num_Analysis.describe())
print(Num_Analysis.mode())

# ---Histplot for Age and Salary---
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

#Age distribution 
sns.histplot(data=df, x='Age', kde=True, ax=axes[0], color='blue')
axes[0].set_title("Age distribution")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Count")
#Salary distribution
sns.histplot(data=df, x='Salary', kde=True, color='red', ax=axes[1])
axes[1].set_title("Salary distribution")
axes[1].set_xlabel("Salary ($)")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.show()

# ---Boxplot for Age and Salary---
sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

#Age distribution
sns.boxplot(data=df, x='Age', color='blue', ax=axes[0])
axes[0].set_title("Age distribution")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Count")
#Salary distribution
sns.boxplot(data=df, x='Salary', color='red', ax=axes[1])
axes[1].set_title("Salary distribution")
axes[1].set_xlabel("Salary ($)")
axes[1].set_ylabel("Count")

plt.tight_layout()
plt.show()

# ---Categorical Analysis---
Cat_Analysis = df[['Department', 'Region', 'Status', 'Performance_Score', 'Remote_Work']]
print(Cat_Analysis.describe())

sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.countplot(data=df, x='Department', ax=axes)
axes.set_title("Department")
axes.set_xlabel("Departments")
axes.set_ylabel("Count")
plt.show()

sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.countplot(data=df, x='Region', ax=axes)
axes.set_title("Region")
axes.set_xlabel("Regions")
axes.set_ylabel("Count")
plt.show()

sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.countplot(data=df, x='Status', ax=axes)
axes.set_title("Status")
axes.set_xlabel("Status")
axes.set_ylabel("Count")
plt.show()

sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.countplot(data=df, x='Performance_Score', ax=axes)
axes.set_title("Performance Score")
axes.set_xlabel("Performance Score")
axes.set_ylabel("Count")
plt.show()

sns.set_theme(style='whitegrid')
fig, axes = plt.subplots(figsize=(7, 5))
sns.countplot(data=df, x='Remote_Work', ax=axes)
axes.set_title("Remote Work")
axes.set_xlabel("Remote Work")
axes.set_ylabel("Count")
plt.show()

#Analysis 
"""
1. Employee Age: The workforce is concentrated around age 30, with more than 400 employees recorded at this age. The most frequently represented age group is 30-35.
2. Salary Distribution: The average employee salary is approximately $85,155.06. Most salaries appear concentrated within the $60,000-$100,000 range.
3. Department Distribution: DevOps is the largest department, with 189 employees.
4. Regional Distribution: California is the most represented region, with 187 employees.
5. Employment Status: Pending is the most common employment status, accounting for 356 employees.
6. Performance Distribution: Good is the most frequent performance category. The distribution should be examined further before concluding that overall employee performance is strong.
7. Work Arrangement: The dataset contains 513 remote employees and 506 on-site employees, indicating an almost equal distribution between the two arrangements. One record remains unaccounted for in these counts.
"""