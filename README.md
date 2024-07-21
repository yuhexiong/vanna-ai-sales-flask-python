# Vanna AI Flask Sales

Connect Vanna AI to database PostgreSQL and use database data finetune AI, and finally use Flask as the frontend web page.  
Vanna AI can not only write sql query according to the data format, but can also directly fetch the data from the database and then create chart.  


## Overview
- AI: Vanna AI v0.6.3
- Database: PostgreSQL v13.2
- Web FrameWork: Flask


## ENV

copy .env.example as .env  
VANNA_MODEL and VANNA_API_KEY can be get at [Vanni AI Office WebSite](https://vanna.ai/)  
```
VANNA_MODEL=
VANNA_API_KEY=
PG_HOST=localhost
PG_DBNAME=postgres
PG_USER=postgres
PG_PASSWORD=password
PG_PORT=5432
```


## Run

### Install dependencies
```
pip install vanna
pip install psycopg2
pip install python-dotenv
```

### Run
```
python run.py
```

## UI

```
http://localhost:8084
```

### Total Sales Amount For Each Day

![image](./images/total_sales_amount.png)
![image](./images/total_sales_amount_chart.png)

### Percentage Of Total Sales Amount By Category

![image](./images/category_sales_amount.png)
![image](./images/category_sales_amount_chart.png)