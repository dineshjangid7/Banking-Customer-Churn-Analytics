# End-to-End Banking Customer Churn Analytics & Predictive Modeling

## Overview

This project is an end-to-end Customer Churn Analytics and Predictive Modeling project built as part of my learning journey in Data Analytics, Machine Learning and Business Intelligence.

The objective of this project is to analyze customer churn behavior in a banking system, identify factors affecting customer retention, and build machine learning models capable of predicting whether a customer is likely to churn.

The project covers the complete analytics pipeline:

* Data Ingestion using SQL Server
* Data Cleaning and Preprocessing using Python
* Exploratory Data Analysis (EDA)
* Statistical Hypothesis Testing
* Machine Learning Model Development
* Interactive Dashboard Development using Tableau

---

## Business Problem

Customer churn is a major challenge for banks because acquiring a new customer is often more expensive than retaining an existing one.

Using historical customer, demographic and account information, the goal is to:

* Understand why customers leave the bank.
* Identify customer groups with high churn probability.
* Build predictive models to estimate churn risk.
* Create an interactive dashboard for business decision making.

---

## Dataset

The project uses banking customer data divided into three relational tables:

### 1. Accounts Table

Contains:

* CustomerId
* Balance
* Tenure
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary
* Exited (Churn Flag)

### 2. Demographics Table

Contains:

* CustomerId
* Age
* Gender
* Credit Score

### 3. Locations Table

Contains:

* Geography
* Continent

---

## Project Workflow

Raw Excel Data

↓

SQL Server Database

↓

Data Cleaning & Validation

↓

Exploratory Data Analysis

↓

Statistical Hypothesis Testing

↓

Feature Engineering

↓

Machine Learning Models

↓

Tableau Dashboard

↓

Business Insights

---

## Technologies Used

### Database

* Microsoft SQL Server
* SQL

### Programming

* Python
* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* Logistic Regression
* Random Forest
* Support Vector Machine
* XGBoost

### Visualization

* Tableau
* Matplotlib

### Statistical Analysis

* T-Test
* Chi-Square Test
* ANOVA

---

## Repository Structure

```bash
BANKCUSTOMERCHURN/

├── data/

│   ├── raw/

│   └── processed/

│

├── Scripts/

│   ├── data_ingestion/

│   └── data_cleaning/

│

├── eda_queries/

│

├── predictive-modelling/

│   ├── processed_data/

│   └── experiments/

│

├── Notebook/

│   └── statistical_testing/

│

├── data_visualisation/

│

└── README.md
```

---

## Machine Learning Models Implemented

I experimented with multiple machine learning models and compared their performance:

* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (Polynomial Kernel)
* Support Vector Machine (RBF Kernel)
* XGBoost Classifier

The goal was to understand how different algorithms perform on customer churn prediction and identify the best-performing model.

---

## Tableau Dashboard

The project includes an interactive Tableau Dashboard that provides:

* Churn by Country
* Churn by Continent
* Churn by Account Status
* Churn by Tenure
* Financial Information Analysis
* Interactive Filtering across all charts

### Dashboard Preview

Add your dashboard screenshot here.

```markdown
![Dashboard](data_visualisation/dashboard_main.png)
```

