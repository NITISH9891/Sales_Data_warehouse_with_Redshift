import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

# "CREATE DATABASE IF NOT EXISTS sales_insights;"
# "USE sales_insights;"


customers_drop = "DROP TABLE IF EXISTS customers;"
date_drop = "DROP TABLE IF EXISTS date;"
markets_drop = "DROP TABLE IF EXISTS markets;"
products_drop = "DROP TABLE IF EXISTS products;"
transactions_drop = "DROP TABLE IF EXISTS transactions;"



ARN             = config.get('IAM_ROLE', 'ARN')

CUSTOMERS_DATA       = config.get('S3', 'CUSTOMERS_DATA')
DATE_DATA            = config.get('S3', 'DATE_DATA')
MARKETS_DATA         = config.get('S3', 'MARKETS_DATA')
PRODUCTS_DATA        = config.get('S3', 'PRODUCTS_DATA')
TRANSACTIONS_DATA    = config.get('S3', 'TRANSACTIONS_DATA')


# CREATE TABLES

customers_table_create = ("""CREATE TABLE customers (
                customer_code       VARCHAR(45)     NOT NULL,
                custmer_name        VARCHAR(45)     DEFAULT NULL,
                customer_type       VARCHAR(45)     DEFAULT NULL);""")

date_table_create = ("""CREATE TABLE date (
                date                DATE            NOT NULL,
                cy_date             VARCHAR(45)     DEFAULT NULL,
                year                INTEGER         DEFAULT NULL,
                month_name          VARCHAR(45)     DEFAULT NULL,
                date_yy_mmm         VARCHAR(45)     DEFAULT NULL);""")

markets_table_create = ("""CREATE TABLE markets (
                markets_code        VARCHAR(45)     NOT NULL,
                markets_name        VARCHAR(45)     DEFAULT NULL,
                zone                VARCHAR(45)     DEFAULT NULL);""")

products_table_create = ("""CREATE TABLE products (
                product_code        VARCHAR(45)     NOT NULL,
                product_type        VARCHAR(45)     DEFAULT NULL);""")

transactions_table_create = ("""CREATE TABLE transactions (
                customer_code       VARCHAR(45)     DEFAULT NULL,
                product_code        VARCHAR(45)     DEFAULT NULL,
                market_code         VARCHAR(45)     DEFAULT NULL,
                order_date          DATE            DEFAULT NULL,
                sales_qty           INTEGER         DEFAULT NULL,
                sales_amount        INTEGER         DEFAULT NULL,
                currency            VARCHAR(45)     DEFAULT NULL,
                profit_margin_percentage DOUBLE     DEFAULT NULL,
                profit_margin       DOUBLE          DEFAULT NULL,
                cost_price          DECIMAL         DEFAULT NULL);""")



# FACT AND DIMENSION TABLE

customers_copy = ("""
        COPY customers FROM {}
        credentials 'aws_iam_role={}'
        delimiter ','
        ignoreheader 1
        region 'us-west-1';""").format(CUSTOMERS_DATA, ARN)

date_copy = ("""
        COPY date FROM {}
        credentials 'aws_iam_role={}'
        delimiter ','
        ignoreheader 1
        region 'us-west-1';""").format(DATE_DATA, ARN)

markets_copy = ("""
        COPY markets FROM {}
        credentials 'aws_iam_role={}'
        delimiter ','
        ignoreheader 1
        region 'us-west-1';""").format(MARKETS_DATA, ARN)

products_copy = ("""
        COPY products FROM {}
        credentials 'aws_iam_role={}'
        delimiter ','
        ignoreheader 1
        region 'us-west-1';""").format(PRODUCTS_DATA, ARN)

transactions_copy = ("""
        COPY transactions FROM {}
        credentials 'aws_iam_role={}'
        delimiter ','
        ignoreheader 1
        region 'us-west-1';""").format(TRANSACTIONS_DATA, ARN)



# QUERY LISTS

drop_table_queries = [customers_drop, date_drop, markets_drop, products_drop, transactions_drop]

create_table_queries = [customers_table_create, date_table_create, markets_table_create, products_table_create, transactions_table_create]

copy_table_queries = [customers_copy, markets_copy, products_copy, date_copy, transactions_copy]

