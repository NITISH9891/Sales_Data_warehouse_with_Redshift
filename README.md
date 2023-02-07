# Sales Data Warehouse with Amazon S3 and Redshift

## Project Description

The goal of this project is to create an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for our analytics team to continue finding meaningful insights.

## ETL MODEL

![ETL-model]( https://github.com/NITISH9891/Sales_Data_warehouse_with_Redshift/blob/main/ETL-model.png)

## Project Steps:

- Design schemas for fact and dimension tables
- Write a SQL CREATE statement for each of these tables and SQL DROP statements to drop tables in the beginning of the table creation process if it already exists 
- Launch a redshift cluster and create an IAM role that has read access to S3 using python SDK or AWS console.
- Add redshift database name, secret keys, access key,IAM role ARN etc information to cluster.cfg
- Test by running the CREATE_TABLE.py and checking the table schemas in redshift database. For validating Schema,we can use Query Editor in the AWS Redshift console. 
- Write code to load data from S3 to analytics tables on Redshift.
- Test these data loading code after creating tables and running the analytic queries on the Redshift database to compare results with the expected results.
- connect Redshift cluster with Power-BI [data visualization tool] and generate a meaningful Sales dashboard.
- Delete the Redshift cluster when done.

## Project Files:

- **Creating Redshift Cluster using the AWS python sdk.ipynb** :- infrastructure as code for creating Redshift clusters in AWS.
- **cluster.cfg** :- Configuration file used that contains info about Redshift, IAM and S3
- **SQL_DATA.py** :- definition of SQL statements, which will be imported into the two other files below.
- **CREATE_TABLE.py** :- creates fact and dimension tables for the star schema in Redshift.
- **LOAD_DATA.py** :-  load data from S3 into staging tables on Redshift and then process that data into analytics tables on Redshift using Copy command.
- **Sale-report.pbix** :- create a dashboard using PowerBI Desktop.
- **Images** :- all relevant images related to this project 

## Schema Design

For this project, we have implemented this following star schema:

![sale_fact_schema](https://github.com/NITISH9891/Sales_Data_warehouse_with_Redshift/blob/main/sales_fact_schema.png)


## Data Analysis Using Query Editor in Redshift

* Show all customer records

    SELECT * FROM customers;

* Show total number of customers

    SELECT count(*) FROM customers;

* Show transactions for Chennai market (market code for chennai is Mark001)

    SELECT * FROM transactions WHERE market_code='Mark001';

* Show distrinct product codes that were sold in chennai

    SELECT distinct product_code 
    FROM transactions WHERE market_code='Mark001';

* Show transactions where currency is US dollars

    SELECT * from transactions WHERE currency="USD";

* Show transactions in 2020 join by date table

    SELECT transactions.*, date.* 
    FROM transactions 
    INNER JOIN date ON transactions.order_date=date.date 
    WHERE date.year=2020;

* Show total revenue in year 2020,

    SELECT SUM(transactions.sales_amount) 
    FROM transactions 
    INNER JOIN date ON transactions.order_date=date.date 
    WHERE date.year=2020 and transactions.currency="INR" or transactions.currency="USD";
	
* Show total revenue in year 2020, January Month,

    SELECT SUM(transactions.sales_amount) 
    FROM transactions 
    INNER JOIN date ON transactions.order_date=date.date 
    WHERE date.year=2020 and and date.month_name="January" and (transactions.currency="INR" or transactions.currency="USD");

* Show total revenue in year 2020 in Chennai

    SELECT SUM(transactions.sales_amount) 
    FROM transactions 
    INNER JOIN date ON transactions.order_date=date.date 
    WHERE date.year=2020 and transactions.market_code="Mark001";


## Data Analysis Using PowerBI Desktop

![sale-insights-PowerBI-report](https://github.com/NITISH9891/Sales_Data_warehouse_with_Redshift/blob/main/sale-insights-PowerBI-report.jpg )

