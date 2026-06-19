# Libraries & import
from pathlib import Path
import pandas as pd
from functions import categorical_sanity_check
from functions import validate_dtypes
from functions import missing_value_report
from functions import plt_boxplot
from functions import plot_distribution

# Load Data
BASE_DIR = Path(__file__).resolve().parents[2]
FILE_NAME = "raw_data.xlsx"
DATA_PATH = BASE_DIR / "data" / "raw" / FILE_NAME
print(DATA_PATH)

SHEET_NAME = "Demographic"
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME)


# Categorical Sanity Check
categorical_sanity_check(df, "Gender", ["Female", "Male"])
categorical_sanity_check(df, "LocationId", [1, 2, 3, 4, 5, 6]),
categorical_sanity_check(df, "Churned", [0, 1])


# Data Typr Checking
expected_dtypes = {
    "Name": "str",
    "Gender": "str",
    "Age": "int64",
    "Salary": "float64",
    "LoactionId": "int64",
    "Churned": "int64",
}
validate_dtypes(df, expected_dtypes)


# Null value Checker
missing_value_report(df)


# Remove Columns
df = df.drop(["Name"], axis=1)


# Export file
OUTPUT_DIR = BASE_DIR / "data" / "processed"
file_name = "demographics.csv"
file_path = OUTPUT_DIR / file_name
df.to_csv(file_path, index=False)
