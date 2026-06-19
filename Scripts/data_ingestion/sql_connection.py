# Libraries and Packages
from pathlib import Path
import pandas as pd
import pyodbc

# load data
BASE_DIR = Path(__file__).resolve().parents[2]
FILE_NAME = "demographics.csv"
FILE_NAME = "accounts.csv"
FILE_NAME = "locations.csv"
DATA_PATH = BASE_DIR / "data" / "processed" / FILE_NAME

df = pd.read_csv(DATA_PATH)

# Create Connection
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=BankChurn;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# push data in database
cursor.execute("SET IDENTITY_INSERT demographics ON")

cursor.execute("SET IDENTITY_INSERT locations ON")
conn.commit()

for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO demographics(
            CustomerId,
            Gender,
            Age,
            Salary,
            LocationId,
            Churned
        )
        VALUES (?,?,?,?,?,?)
    """,
        int(row.CustomerId),
        row.Gender,
        int(row.Age),
        float(row.Salary),
        int(row.LocationId),
        int(row.Churned),
    )

for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO accounts(
            CustomerId,
            Tenure,
            Balance,
            NumProducts,
            HasCreditCard,
            IsActive
        )
        VALUES (?,?,?,?,?,?)
    """,
        int(row.CustomerId),
        int(row.Tenure),
        float(row.Balance),
        int(row.NumProducts),
        int(row.HasCreditCard),
        int(row.IsActive),
    )

for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO locations(
            LocationId,
            Geography
        )
        VALUES (?,?)
    """,
        int(row.LocationId),
        row.Geography,
    )

conn.commit()
