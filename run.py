import os
from dotenv import load_dotenv
from vanna.remote import VannaDefault
from vanna.flask import VannaFlaskApp

load_dotenv(dotenv_path='./.env')

# env
model = os.getenv('VANNA_MODEL')
api_key = os.getenv('VANNA_API_KEY')
host = os.getenv('PG_HOST')
dbname = os.getenv('PG_DBNAME')
user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
port = int(os.getenv('PG_PORT'))

# setting vanna
vn = VannaDefault(model=model, api_key=api_key)
vn.connect_to_postgres(host=host, dbname=dbname, user=user, password=password, port=port)

# training
# ddl
vn.train(ddl="""
    CREATE TABLE Sales (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        product_category VARCHAR(50) NOT NULL,
        sales_amount DECIMAL(10, 2) NOT NULL,
        units_sold INT NOT NULL,
        region VARCHAR(50) NOT NULL
    );
""")

# documentation
vn.train(documentation="sales_amount means (unit_price * units_sold).")
vn.train(documentation="region options include North America, Europe and Asia.")
vn.train(documentation="category options of product include Home Appliances, Electronics and Clothing.")
vn.train(documentation="date format as YYYY-MM-DD.")

# question and sql
vn.train(
    question="Show all categories of product.", 
    sql="""
        SELECT DISTINCT product_category FROM Sales;
""")

vn.train(
    question="Show the total sales amount for each region, sorted from highest to lowest.", 
    sql="""
        SELECT
            region,
            SUM(unit_price * units_sold) AS total_sales_amount
        FROM Sales
        GROUP BY region
        ORDER BY total_sales_amount DESC;
""")

vn.train(
    question="Show the total sales amount for each day.", 
    sql="""
        SELECT
            date,
            SUM(unit_price * units_sold) AS total_sales_amount
        FROM Sales
        GROUP BY date
        ORDER BY date;
""")

vn.train(
    question="Show the percentage of total sales amount by category.", 
    sql="""
        SELECT
            category,
            SUM(unit_price * units_sold) AS category_sales_amount,
            (SUM(unit_price * units_sold) / (SELECT SUM(unit_price * units_sold) FROM Sales)) * 100 AS percentage_of_total
        FROM
            Sales
        GROUP BY category
        ORDER BY percentage_of_total DESC;
""")

# web ui
VannaFlaskApp(vn, allow_llm_to_see_data=True).run()