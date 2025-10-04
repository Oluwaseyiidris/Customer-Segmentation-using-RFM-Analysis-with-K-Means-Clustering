from sqlalchemy import create_engine
import pandas as pd

file_path = r"C:\Users\DELL\Documents\project file 12-09\Online Retail II (E-commerce Transaction Data).csv"
df = pd.read_csv(file_path, encoding="latin1")

# Try flexible parsing: this catches both dd/mm/yyyy and mm/dd/yyyy
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce", dayfirst=True)

# Find rows that failed to parse
bad_rows = df[df["InvoiceDate"].isna()]
print("Bad rows:", len(bad_rows))

# Save cleaned data
clean_path = r"C:\Users\DELL\Documents\project file 12-09\Online_Retail.csv"
df.to_csv(clean_path, index=False, date_format="%Y-%m-%d %H:%M:%S")


df = pd.read_csv("online_retail.csv", encoding="latin1")
engine = create_engine(
    "mysql+pymysql://root:newpassword@localhost:3306/customer_analysis")
df.to_sql("online_Retail", engine, if_exists="replace", index=False)
