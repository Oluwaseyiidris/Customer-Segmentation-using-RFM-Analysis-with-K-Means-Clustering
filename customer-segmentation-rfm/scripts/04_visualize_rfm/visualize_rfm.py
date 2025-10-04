import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:newpassword@localhost:3306/customer_analysis")

# Load clustered RFM table
df = pd.read_sql("SELECT * FROM customer_rfm_clustered", engine)

# ---------------------------
# 1. Histograms per cluster
# ---------------------------
features = ['Recency', 'Frequency', 'Monetary']

for feature in features:
    plt.figure(figsize=(8, 5))
    for cluster in df['Cluster'].unique():
        sns.kdeplot(df[df['Cluster'] == cluster][feature],
                    label=f'Cluster {cluster}', fill=True, alpha=0.3)
    plt.title(f"Distribution of {feature} by Cluster")
    plt.xlabel(feature)
    plt.ylabel("Density")
    plt.legend()
    plt.show()

# ---------------------------
# 2. Scatter plots
# ---------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Frequency', y='Monetary',
                hue='Cluster', data=df, palette='tab10')
plt.title("Clusters: Frequency vs Monetary")
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Recency', y='Frequency',
                hue='Cluster', data=df, palette='tab10')
plt.title("Clusters: Recency vs Frequency")
plt.show()
