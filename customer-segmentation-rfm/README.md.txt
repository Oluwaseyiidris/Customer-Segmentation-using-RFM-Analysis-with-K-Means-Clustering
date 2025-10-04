Customer Segmentation Using RFM Analysis & K-Means Clustering

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-green)

📊 Project Overview

This project performs customer segmentation on e-commerce transaction data using **RFM (Recency, Frequency, Monetary)** analysis combined with **K-Means clustering**. By analyzing over 1 million transactions from 4,400+ customers, the system identifies four distinct customer segments that reveal critical business insights: 45% of customers (VIPs) generate 72.61% of revenue, while 23% are at high risk of churn.

*Key Technologies:* Python, MySQL, Pandas, Scikit-learn, Matplotlib, Seaborn, Pivot-table

*Business Impact:* Enables targeted marketing strategies, churn prevention, and resource optimization by identifying high-value customers and growth opportunities.


 Business Problem

E-commerce businesses struggle to identify which customers drive the most value and which are at risk of churning. This project uses *RFM (Recency, Frequency, Monetary) analysis combined with K-Means clustering* to segment customers into actionable groups, enabling:

- *Targeted marketing campaigns* based on customer behavior
- *Churn prevention* by identifying at-risk customers early
- *Revenue optimization* by focusing resources on high-value segments
- *Customer lifetime value maximization* through personalized strategies

This project demonstrates how data-driven segmentation can transform raw transaction data into strategic business insights.


 Project Structure

```
├── data/
│   └── README.md                    # Dataset information
├── datasets                                #Datasets used
├── sql/
│   ├── 01_load_data.sql            # Load data into MySQL
│   ├── 02_data_cleaning.sql        # Data cleaning and standardization
│   └── 03_rfm_calculation.sql      # RFM metrics calculation
├──scripts/
│   ├── 01_data_cleaning.py         # Date parsing and initial cleaning
│   ├── 02_rfm_normalization.py     # Normalize RFM values
│   ├── 03_kmeans_clustering.py     # K-Means clustering with elbow method
│   └── 04_visualizations.py        # Generate cluster visualizations
├── results/
│   ├── customer_segmentation.xlsx  # Final segmented customer list
│   ├── cluster_summary.xlsx        # Cluster statistics
│   └── visualizations/             # Charts and plots
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

Methodology

1. Data Collection & Cleaning
- Dataset: Online Retail II E-commerce Transaction Data (UCI Repository)
- Size: 1,067,371 transactions from 4,400+ unique customers
- Period: December 2009 - December 2011
- Cleaning Steps:
  - Removed transactions with null CustomerIDs (~25% of data)
  - Filtered negative quantities and zero prices
  - Standardized country names (EIRE → Ireland, RSA → South Africa)
  - Parsed and validated invoice dates using flexible datetime parsing
  - Final clean dataset: ~540,000 valid transactions

2. RFM Analysis
Calculated three key metrics for each customer:

| Metric | Definition | Formula |
|--------|------------|---------|
| Recency (R) | Days since last purchase | `DATEDIFF(CURRENT_DATE, MAX(InvoiceDate))` |
| Frequency (F) | Number of purchases | `COUNT(DISTINCT InvoiceNo)` |
| Monetary (M)| Total spending | `SUM(Quantity × UnitPrice)` |

3. Data Normalization
Applied Min-Max scaling to RFM values (0-1 range) to ensure equal weight in clustering.

4. K-Means Clustering
- Used Elbow Method to determine optimal number of clusters
- Selected K=4 based on inertia reduction
- Assigned customers to segments


📈 Results

CUSTOMER SEGMENTS IDENTIFIED

| Segment | Customer Distribution | Avg Spend | Revenue Contribution | Avg Recency | Avg Frequency |
|---------|---------------------|-----------|---------------------|-------------|---------------|
| VIP / Loyal Customers | 45% | $4,316 | 72.61% | 5,075 days | 8 purchases |
| Window Shoppers | 32% | $1,608 | 19.11% | 5,197 days | 4 purchases |
| At Risk | 18% | $1,053 | 7.05% | 5,325 days | 3 purchases |
| Dormant Customers | 5% | $651 | 1.23% | 5,606 days | 2 purchases |

 KEY BUSINESS INSIGHTS

1. Revenue Concentration Creates Both Opportunity and Risk
- 45% of customers (VIP segment) generate 72.61% of total revenue (- this is the Pareto principle in action)
- VIP customers spend 61% more than the overall average ($4,316 vs $2,682)
- *Business implication:* Heavy dependence on this segment means retention strategies are critical to business survival

2. Significant Portion of Customer Base is Disengaged
- 23% of customers (At Risk + Dormant) contribute only 8.28% of revenue
- Average recency of 5,325-5,606 days indicates these customers haven't purchased in over 14 years
- *Business implication:* Immediate win-back campaigns needed, but some may be unrecoverable

3. Window Shoppers Represent Untapped Growth Potential
- Nearly 1 in 3 customers (32%) falls into this moderate-engagement category
- Currently generating only 19.11% of revenue despite significant customer base
- Average frequency of 4 purchases shows engagement, but spend is 63% lower than VIPs
- *Business implication:* Strategic upselling, cross-selling, and loyalty programs could shift these customers toward VIP status and significantly boost revenue

4. VIP Loyalty Metrics Validate Segment Quality
- Highest purchase frequency (8 transactions) confirms sustained engagement
- Despite high recency values across all segments (artifact of historical data), VIPs show lowest recency relative to others
- *Business implication:* Current VIP retention strategies are working - double down on what's successful

DATA QUALITY NOTE
The high recency values across all segments (5,000+ days) suggest the dataset ends in 2011, and recency was calculated from a much later date. In a production environment, these values would be much lower, making recency a more discriminating factor between segments.

VISUALIZATIONS

*Cluster Distribution:*
- Recency vs Frequency scatter plot
- Frequency vs Monetary value plot
- RFM distribution by cluster (density plots)


TECHNOLOGIES USED

Languages & Libraries
- *Python 3.8+*
  - pandas: Data manipulation
  - scikit-learn: K-Means clustering
  - matplotlib & seaborn: Visualizations
  - SQLAlchemy: Database connection
  - pymysql: MySQL driver

- *SQL (MySQL 8.0)*
  - Data cleaning and transformation
  - RFM metric calculation
  - Result storage

Tools
- *Excel:* Final analysis and presentation
- *Git & GitHub:* web


🚀 Installation & Setup

Prerequisites
```bash
# Python 3.8 or higher
# MySQL Server 8.0+
```

1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

2. Database Setup
```sql
CREATE DATABASE customer_analysis;
```

Update database credentials in scripts:
```python
engine = create_engine(
    "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/customer_analysis"
)
```

3. Run the Pipeline

*Step 1: Load and Clean Data*
```bash
python scripts/01_data_cleaning.py
```

*Step 2: Execute SQL scripts*
```sql
source sql/02_data_cleaning.sql;
source sql/03_rfm_calculation.sql;
```

*Step 3: Normalize RFM values*
```bash
python scripts/02_rfm_normalization.py
```

*Step 4: Perform Clustering*
```bash
python scripts/03_kmeans_clustering.py
```

*Step 5: Generate Visualizations*
```bash
python scripts/04_visualizations.py
```



📝 Sample Output

Cluster Summary Statistics
```
Segment                  | Customers | Avg Recency | Avg Frequency | Avg Spend
------------------------|-----------|-------------|---------------|----------
VIP / Loyal Customers   |    1,980  |    5,075    |       8       |  $4,316
Window Shoppers         |    1,408  |    5,197    |       4       |  $1,608
At Risk                 |      792  |    5,325    |       3       |  $1,053
Dormant Customers       |      220  |    5,606    |       2       |    $651
------------------------|-----------|-------------|---------------|----------
Total                   |    4,400  |    5,185    |       5       |  $2,682
```

Revenue Distribution
```
Segment: VIP / Loyal Customers
- Revenue Share: 72.61%
- Customer Share: 45.00%
- Revenue per Customer: $4,316

Segment: Window Shoppers  
- Revenue Share: 19.11%
- Customer Share: 32.00%
- Revenue per Customer: $1,608

Segment: At Risk
- Revenue Share: 7.05%
- Customer Share: 18.00%
- Revenue per Customer: $1,053

Segment: Dormant Customers
- Revenue Share: 1.23%
- Customer Share: 5.00%
- Revenue per Customer: $651
```


💡 Business Recommendations

For VIP Customers (45% of base, 72.61% of revenue)
- *Priority:* Maximum retention - these customers are the business backbone
- Implement tiered loyalty programs with exclusive benefits
- Provide early access to new products and premium features
- Assign dedicated account managers for personalized service
- Create VIP-only events and experiences
- Send personalized thank-you messages and anniversary rewards

For Window Shoppers (32% of base, 19.11% of revenue)
- *Priority:* Convert to higher-value customers through engagement
- Implement nurture campaigns with educational content about products
- Offer bundle deals and volume discounts to increase basket size
- Use targeted cross-selling based on purchase history
- Simplify checkout process to reduce friction
- Create limited-time offers to encourage repeat purchases

For At-Risk Customers (18% of base, 7.05% of revenue)
- *Priority:* Prevent churn through re-engagement
- Deploy win-back email campaigns with compelling offers
- Survey customers to understand pain points and dissatisfaction
- Offer "We miss you" discounts (15-20% off next purchase)
- Highlight new products or improvements since last purchase
- Use retargeting ads with personalized messaging

For Dormant Customers (5% of base, 1.23% of revenue)
- *Priority:* Reactivation with aggressive incentives
- Send multi-channel win-back campaigns (email + SMS)
- Offer significant discounts (25-30%) as last-resort recovery
- Create urgency with limited-time reactivation offers
- Consider feedback surveys to understand why they left
- If no response after 2-3 attempts, move to suppression list to reduce costs


 🔮 Future Enhancements

- [ ] Implement customer lifetime value (CLV) prediction
- [ ] Add temporal analysis (seasonality trends)
- [ ] Build interactive dashboard with Tableau/Power BI
- [ ] Integrate with CRM for automated segmentation
- [ ] Apply deep learning for churn prediction


LICENSE 

This project is open source and available under the [MIT License](LICENSE).


 AUTHOR

OLUWASEYI IDRIS

- GitHub: @Oluwaseyiidris](https://github.com/Oluwaseyiidris
- LinkedIn: www.linkedin.com/in/oluwaseyi-idris
- Email: idris.seyifunmi@gmail.com


ACKNOWLEDGEMENTS

- Dataset: [UCI Machine Learning Repository - Online Retail II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
- Inspired by: RFM Analysis best practices in e-commerce


CALL

 If you found this project helpful, please consider giving it a star!
