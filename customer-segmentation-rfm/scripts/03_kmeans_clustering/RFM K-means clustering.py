import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# -------------------------------
# 1. Connect to MySQL and load data
# -------------------------------
engine = create_engine(
    "mysql+pymysql://root:newpassword@localhost:3306/customer_analysis")
df = pd.read_sql("SELECT * FROM normalized_rfm", engine)

# -------------------------------
# 2. Prepare data for clustering
# -------------------------------
X = df[['Recency', 'Frequency', 'Monetary']]

# -------------------------------
# 3. Elbow Method - Find best K
# -------------------------------
inertia = []
K_range = range(1, 10)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plot elbow chart
plt.plot(K_range, inertia, 'bo-')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Method for Optimal K")
plt.show()

# -------------------------------
# 4. Run KMeans with chosen K=4
# -------------------------------
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# -------------------------------
# Cluster summary (averages)
# -------------------------------
cluster_summary = df.groupby("Cluster").agg({
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean",
    "CustomerID": "count"
}).reset_index()

# Rename for readability
cluster_summary = cluster_summary.rename(columns={
    "Recency": "Avg_Recency",
    "Frequency": "Avg_Frequency",
    "Monetary": "Avg_Monetary",
    "CustomerID": "Num_Customers"
})

# Round to 2 decimals
cluster_summary = cluster_summary.round(2)

print("\nCluster Summary:")
print(cluster_summary)

# -------------------------------
# Save results back to MySQL
# -------------------------------
df.to_sql("customer_analysis", engine, if_exists="replace", index=False)
cluster_summary.to_sql("cluster_summary", engine,
                       if_exists="replace", index=False)

print("\nClustered data and summary saved to MySQL.")

# -------------------------------
# 7. Visualize clusters (2D scatter)
# -------------------------------
plt.scatter(df['Recency'], df['Monetary'], c=df['Cluster'], cmap='viridis')
plt.xlabel("Recency")
plt.ylabel("Monetary")
plt.title("Customer Clusters (Recency vs Monetary)")
plt.show()
