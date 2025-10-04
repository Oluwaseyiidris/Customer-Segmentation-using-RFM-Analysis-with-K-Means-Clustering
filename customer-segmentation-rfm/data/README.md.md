Dataset Information



Source

Online Retail II Dataset

UCI Machine Learning Repository



Link: \[https://archive.ics.uci.edu/ml/datasets/Online+Retail+II](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)



Description

This dataset contains all transactions occurring for a UK-based online retail company between 01/12/2009 and 09/12/2011. The company mainly sells unique all-occasion gift-ware.



Dataset Characteristics



| Attribute | Details |

|-----------|---------|

| Size | 1,067,371 transactions |

| Features | 8 columns |

| Period | December 2009 - December 2011 |

| Industry | E-commerce / Retail |



Schema



| Column | Type | Description |

|--------|------|-------------|

| InvoiceNo | String | 6-digit invoice number. If starts with 'C', it's a cancellation |

| StockCode | String | 5-digit product code |

| Description | String | Product name |

| Quantity | Integer | Number of items per transaction |

| InvoiceDate | DateTime | Date and time of transaction |

| UnitPrice | Float | Product price in GBP (£) |

| CustomerID | String | 5-digit unique customer identifier |

| Country | String | Country where customer resides |



Data Quality Issues (Addressed in Cleaning)



1\. Missing CustomerIDs: ~25% of transactions lack customer information

2\. Negative Quantities: Returns/cancellations marked with negative values

3\. Zero Prices: Some items have 0.00 unit price

4\. Date Format Inconsistencies: Mixed date formats requiring standardization

5\. Country Name Variations: 'EIRE' vs 'Ireland', 'RSA' vs 'South Africa'



###### Data Cleaning Steps



```sql

-- Removed records with missing CustomerID

-- Filtered out negative quantities and prices

-- Standardized country names

-- Validated and parsed invoice dates

```



After cleaning: ~541,909 valid transactions from ~4,372 unique customers



File Note



⚠️*The raw CSV file is NOT included in this repository due to its size (~45 MB).*



To replicate this analysis:

1\. Download the dataset from the UCI link above

2\. Place it in this `data/` folder

3\. Run the cleaning scripts in sequence



###### Citation



If you use this dataset, please cite:



```

Daqing Chen, Sai Liang Sain, and Kun Guo, 

Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining, 

Journal of Database Marketing and Customer Strategy Management, Vol. 19, No. 3, pp. 197-208, 2012.

```

