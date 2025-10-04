SELECT COUNT(*) FROM online_retail_ii;

SELECT Country
 FROM online_retail_ii
GROUP BY Country;

-- cleaning the data up!
UPDATE online_retail_ii
SET country = 'Ireland'
WHERE country = 'EIRE';

UPDATE online_retail_ii
SET country = 'South Africa'
WHERE country = 'RSA';

-- standardize the data
SELECT DISTINCT InvoiceDate
FROM online_retail_ii
ORDER BY InvoiceDate
LIMIT 20;

ALTER TABLE clean_retail_data
MODIFY COLUMN CustomerID VARCHAR(20);

ALTER TABLE clean_retail_data
MODIFY COLUMN UnitPrice DECIMAL(10, 2);

ALTER TABLE clean_retail_data
MODIFY COLUMN Quantity INT;

ALTER TABLE clean_retail_data
MODIFY COLUMN InvoiceNo VARCHAR(20);

ALTER TABLE clean_retail_data
MODIFY COLUMN StockCode VARCHAR(20);

ALTER TABLE clean_retail_data
MODIFY COLUMN Country VARCHAR(20);

-- create a clean table 
CREATE TABLE clean_retail_data
SELECT InvoiceNo, StockCode, Description,
       Quantity, InvoiceDate,
       UnitPrice, CustomerID, Country
FROM online_retail_ii
WHERE CustomerID IS NOT NULL
AND CustomerID <> ''
AND Quantity > 0
AND UnitPrice > 0;

SELECT *
FROM clean_retail_data;

CREATE TABLE R_F_M
   SELECT CustomerID,
    DATEDIFF(CURRENT_DATE(), MAX(InvoiceDate)) AS Recency,
     COUNT(DISTINCT InvoiceNo) AS Frequency,
     FORMAT(SUM(quantity * unitprice), 0) AS Monetary
   FROM clean_retail_data
 GROUP BY CustomerID
ORDER BY Monetary DESC;

SELECT * FROM R_F_M;
SELECT * FROM cluster_summary; 

SELECT * 
FROM customer_rfm_clustered
WHERE Cluster = 2 ;


CREATE TABLE cluster_labels (
    Cluster INT,
    Label VARCHAR(50)
);

INSERT INTO cluster_labels (Cluster, Label) VALUES
(0, 'Window Shoppers'),
(1, 'At Risk'),
(2, 'VIP / Loyal Customers'),
(3, 'Dormant Customers');

SELECT * FROM cluster_labels;
SELECT * FROM cluster_summary;
SELECT * FROM customer_clustered_label;
SELECT * FROM normalized_rfm;
SELECT * FROM r_f_m;

CREATE TABLE cluster_label
SELECT 
    s.Cluster,
    Label,
    Num_Customers,
    Avg_Recency,
    Avg_Frequency,
    Avg_Monetary
FROM cluster_summary s
JOIN cluster_labels l
    ON s.Cluster = l.Cluster;
    
SELECT * FROM cluster_label;

CREATE TABLE Customer_segmentation
SELECT DISTINCT r.CustomerID, r.Recency, r.Frequency, r.Monetary, cl.Cluster
FROM R_F_M r
JOIN customer_clustered_label cl
 ON r.CustomerID = cl.CustomerID;
 
SELECT * FROM cluster_labels;
SELECT * FROM cluster_label;
SELECT * FROM cluster_summary;
SELECT * FROM normalized_rfm;
SELECT * FROM r_f_m;
SELECT * FROM customer_segmentation;
SELECT * FROM customer_clustered_label;


-- export the file to excel
SELECT 'CustomerID','Recency','Frequency','Monetary','Cluster'
UNION ALL
SELECT CustomerID, Recency, Frequency, Monetary, Cluster
FROM customer_segmentation
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customer_segmentation.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

