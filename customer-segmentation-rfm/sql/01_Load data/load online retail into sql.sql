SHOW VARIABLES LIKE 'secure_file_priv';

CREATE TABLE online_retail (
    InvoiceNo VARCHAR(255),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate VARCHAR(50),
    UnitPrice DECIMAL(10, 2),
    CustomerID VARCHAR(20),
    Country VARCHAR(50)
);

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Online_Retail.csv"
INTO TABLE online_retail
CHARACTER SET latin1
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

