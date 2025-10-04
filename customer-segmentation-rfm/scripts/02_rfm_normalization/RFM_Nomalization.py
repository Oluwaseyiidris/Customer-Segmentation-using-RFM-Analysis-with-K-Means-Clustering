import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sqlalchemy import create_engine

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:newpassword@localhost:3306/customer_analysis")
# Load Data
df = pd.read_sql("SELECT * FROM R_F_M", engine)
# print(df.head(10))
# Clean numeric columns (remove commas, convert to float)
df['Recency'] = df['Recency'].astype(str).str.replace(",", "").astype(float)
df['Frequency'] = df['Frequency'].astype(
    str).str.replace(",", "").astype(float)
df['Monetary'] = df['Monetary'].astype(str).str.replace(
    ",", "").astype(float)
# Select RFM columns
RFM = df[['Recency', 'Frequency', 'Monetary']]
# Initialize scaler
scaler = MinMaxScaler()
# Fit & transform
RFM_Scaled = scaler.fit_transform(RFM)
# Convert back to a DataFrame with the same column names
RFM_Normalized = pd.DataFrame(RFM_Scaled,
                              columns=['Recency', 'Frequency', 'Monetary'])
# Add back CustomerID
RFM_Normalized = pd.concat([df[['CustomerID']], RFM_Normalized], axis=1)
# print(RFM_Normalized.head(10))
# Round to 2 decimal places
RFM_Normalized = RFM_Normalized
# Check table in Python
# print(RFM_Normalized.head(10))
# Save normalized table back into MySQL
RFM_Normalized.to_sql("customer_analysis", engine,
                      if_exists="replace", index=False)
