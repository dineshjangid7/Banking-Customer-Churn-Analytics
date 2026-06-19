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

SHEET_NAME = "Account"
df = pd.read_excel(DATA_PATH, sheet_name=SHEET_NAME)


# Categorical Sanity Check
categorical_sanity_check(df, "HasCreditCard", [0, 1])
categorical_sanity_check(df, "IsActive", [0, 1])


# Data Typr Checking
expected_dtypes = {
    "Tenure": "int64",
    "Balance": "float64",
    "NumProducts": "int64",
    "HasCreditCard": "int64",
    "IsActive": "int64",
}
validate_dtypes(df, expected_dtypes)


# Null value Checker
missing_value_report(df)


# Dealing with missing values
df["Balance"] = df["Balance"].fillna(df["Balance"].mean(), inplace=True)


# Recheking
missing_value_report(df)


# Remove Columns
df = df.drop(["AccountId"], axis=1)


# Export file
OUTPUT_DIR = BASE_DIR / "data" / "processed"
file_name = "accounts.csv"
file_path = OUTPUT_DIR / file_name
df.to_csv(file_path, index=False)
