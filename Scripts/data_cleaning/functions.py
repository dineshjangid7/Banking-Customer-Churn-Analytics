# Libraries & Packages:
import seaborn as sns
import matplotlib.pyplot as plt


# Function: Categorical Sanity Check
def categorical_sanity_check(df, column, valid_values):
    invalid = df[~df[column].isin(valid_values)]
    return invalid[column].value_counts()


# Function: Data Typr Checking
def validate_dtypes(df, expected_dtypes: dict):
    mismatch = {}
    for col, dtype in expected_dtypes.items():
        if col in df.columns and df[col].dtype != dtype:
            mismatch[col] = (df[col].dtype, dtype)
    return mismatch


# Function: Null value Checker
def missing_value_report(df):
    return (
        df.isnull()
        .sum()
        .to_frame("missing_count")
        .assign(missing_pct=lambda x: x.missing_count / len(df))
        .query("missing_count > 0")
    )


# Function: Outlier Detection and Distribution
def plot_distribution(df, col):
    sns.histplot(df[col], kde=True)
    plt.title(f"distribution of {col}")
    plt.show()


def plt_boxplot(df, col):
    sns.boxplot(x=df[col])
    plt.title(f"outliers in {col}")
    plt.show()
