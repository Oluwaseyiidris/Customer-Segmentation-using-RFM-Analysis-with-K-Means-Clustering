from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    f"mysql+pymysql://{"root"}:{"newpassword"}@{"localhost:3306"}/{"customer_analysis"}")

df = pd.read_csv(
    r"c:\Users\DELL\Documents\project file 12-09\Online Retail II (E-commerce Transaction Data).csv", encoding="latin1")

df.to_sql("online_retail", con=engine, if_exists="replace", index=False)


# Path to your original CSV
file_path = r"C:\Users\DELL\Documents\project file 12-09\Online Retail II (E-commerce Transaction Data).csv"

# Read CSV
df = pd.read_csv(file_path, encoding="latin1")

# Inspect InvoiceDate column
print("Before cleaning:", df["InvoiceDate"].head(10))

# Try to parse dates flexibly (handles both dd/mm/yyyy and mm/dd/yyyy)
df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"], errors="coerce", dayfirst=True)

# Check which rows failed
bad_rows = df[df["InvoiceDate"].isna()]
print(f"Bad rows: {len(bad_rows)}")

# Save clean version with proper ISO datetime format
clean_path = r"C:\Users\DELL\Documents\project file 12-09\Online_Retail_Clean.csv"
df.to_csv(clean_path, index=False, date_format="%Y-%m-%d %H:%M:%S")

print("✅ Cleaned file saved:", clean_path)
