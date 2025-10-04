select * from online_retail_ii;

-- lets clean the data up!
CREATE TABLE Clean_retail_data
SELECT InvoiceNo, StockCode, Description,
	   Quantity, str_to_date(InvoiceDate, '%d/%m/%Y %H:%i') As InvoiceDate,
       UnitPrice, CustomerID, Country
  FROM online_retail_ii
       WHERE CustomerID IS NOT NULL
       AND Quantity > 0
       AND UnitPrice > 0
       AND CustomerID <> '';
       
UPDATE clean_retail_data
SET Country = 'Ireland'
WHERE Country = 'EIRE';
       
select * from Clean_retail_data;

--  lets get into creating the recency, frequency and monetary table
CREATE TABLE R_F_M
SELECT CustomerID,
        FORMAT(SUM(Quantity * unitprice), 0) AS Monetary,
        COUNT(DISTINCT InvoiceNo) AS Frequency,
        DATEDIFF(CURDATE(), MAX(InvoiceDate)) AS Recency
     FROM Clean_retail_data
		GROUP BY CustomerID
        ORDER BY Monetary;
        
select * from r_f_m;

