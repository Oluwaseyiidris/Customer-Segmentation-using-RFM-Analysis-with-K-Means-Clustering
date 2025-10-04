import pandas as pd
from sklearn.cluster import KMeans
from sqlalchemy import create_engine

# # Connect to MySQL
# engine = create_engine(
#     "mysql+pymysql://root:newpassword@localhost:3306/customer_analysis")

# # Load normalized RFM table
# df = pd.read_sql("SELECT * FROM normalized_rfm", engine)

# # Select only features for clustering
# X = df[['Recency', 'Frequency', 'Monetary']]
# # print(df.head())

# # Initialize KMeans
# # i choose to group them into 4 groups
# kmeans = KMeans(n_clusters=4, random_state=42)

# # Fit the model and assign clusters
# df['Cluster'] = kmeans.fit_predict(X)

# # # Save clustered table back into MySQL
# # df.to_sql("customer_analysis", engine, if_exists="replace", index=False)

# # # Check results in Python
# # print(df.head(10))
# # print(df['cluster'].value_counts())

cluster_summary = df.groupby("Cluster").agg({
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean",
    "CustomerID": "count"   # how many customers in each cluster
}).reset_index()

# Rename columns for readability
cluster_summary = cluster_summary.rename(columns={
    "Recency": "Avg_Recency",
    "Frequency": "Avg_Frequency",
    "Monetary": "Avg_Monetary",
    "CustomerID": "Num_Customers"
})

# print(cluster_summary)
df.to_sql("customer_analysis", engine, if_exists="replace", index=False)
