# Vanna AI Sales Flask

**(also provided Traditional Chinese version document [README-CH.md](README-CH.md).)**

Connect Vanna AI to database PostgreSQL and use database data finetune AI, and finally use Flask as the frontend web page.  
Vanna AI can not only write sql query according to the data schema, but can also directly fetch the data from the database and then create chart.  
Also provide [init_postgres.sql](init_postgres.sql) for example data of my project.  


## Overview
- AI: Vanna AI v0.6.3
- Database: PostgreSQL v13.2
- Web FrameWork: Flask


## ENV

copy .env.example as .env  
`VANNA_MODEL` and `VANNA_API_KEY` can be get at [Vanna AI Office WebSite](https://vanna.ai/)  

```yaml
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
