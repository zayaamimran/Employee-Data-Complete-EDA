# Employee Data Analysis — Complete Exploratory Data Analysis (EDA)

## Overview

This project presents a complete Exploratory Data Analysis (EDA) of an employee dataset using Python. The objective is to understand employee information, identify data-quality issues, clean the dataset, explore variable distributions, and discover relationships and patterns through statistical analysis and data visualization.

The project follows a structured EDA workflow, starting with raw data inspection and preprocessing and progressing through univariate, bivariate, and multivariate analysis.

## Dataset

The original dataset contains **1,020 employee records and 12 columns**, covering different aspects of employee information.

Key attributes include:

- Employee demographics
- Department and geographical region
- Employment status
- Joining date
- Salary
- Performance score
- Remote-work status

The raw dataset contains missing values and a combined department-region column, which are addressed during data cleaning.

## Project Workflow

### Data Understanding
- Inspect dataset dimensions and structure.
- Examine column data types.
- Generate descriptive statistics.
- Identify unique values across columns.

### Data Quality
- Identify missing values.
- Check for duplicate records.
- Examine duplicate employee IDs.
- Inspect data types and potential inconsistencies.

### Data Cleaning
- Handle missing age values using median imputation.
- Handle missing salary values using mean imputation.
- Separate department and region into individual columns.
- Export the cleaned dataset for further analysis.

### Univariate Analysis
- Analyze numerical variable distributions.
- Explore age and salary using histograms and boxplots.
- Examine categorical frequencies and percentages.
- Visualize employee distributions across categories.

### Bivariate Analysis
- Explore the relationship between age and salary.
- Compare salary distributions across departments, regions, performance scores, remote-work status, and employment status.
- Examine relationships between categorical variables using cross-tabulations and heatmaps.

### Multivariate Analysis
- Explore relationships involving multiple employee attributes.
- Examine age and salary correlation using Spearman's rank correlation.
- Compare salary distributions across departments and performance scores.
- Visualize employee distributions across departments, regions, and employment status.

### Statistical Analysis
- Calculate mean, median, and mode.
- Examine variance and standard deviation.
- Analyze skewness and kurtosis.
- Calculate Pearson and Spearman correlation coefficients.

## Tools and Technologies

- **Python** — Core programming language
- **NumPy** — Numerical operations
- **Pandas** — Data manipulation and analysis
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical data visualization
- **Jupyter Notebook** — Interactive analysis environment

## Repository Structure

```text
Employee-Data-Analysis/
│
├── Employee_Data_Analysis.ipynb
├── Messy_Employee_dataset.csv
├── Cleaned_Employee_Dataset.csv
└── README.md
```

*File names in the repository may differ depending on the uploaded notebook and datasets.*

## How to Run

Clone the repository:

```bash
git clone https://github.com/zayaamimran/Employee-Data-Complete-EDA
```

Navigate to the project directory:

```bash
cd Employee-Data-Complete-EDA
```

Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn jupyter
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the EDA notebook and execute the cells.

## Conclusion

This project demonstrates a structured approach to Exploratory Data Analysis, covering data inspection, quality assessment, cleaning, statistical analysis, and visualization.

It provides practical experience in using Python data-analysis libraries to prepare raw data, investigate patterns, and communicate findings through statistical summaries and visualizations.

## Limitations

- Missing values were handled through imputation, which may influence statistical summaries and distributions.
- The analysis focuses primarily on age and salary as numerical variables.
- Correlation indicates association, not causation.
- The findings describe the available dataset and should not automatically be generalized to a wider employee population.