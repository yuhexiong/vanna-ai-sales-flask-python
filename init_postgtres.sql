CREATE TABLE Sales (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    product_category VARCHAR(50) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    units_sold INT NOT NULL,
    region VARCHAR(50) NOT NULL
);

INSERT INTO Sales (date, product_category, unit_price, units_sold, region) VALUES
('2024-01-15', 'Electronics', 40.00, 30, 'North America'),
('2024-01-15', 'Clothing', 20.00, 50, 'Europe'),
('2024-01-15', 'Home Appliances', 25.00, 20, 'Asia'),
('2024-01-16', 'Electronics', 45.00, 40, 'North America'),
('2024-01-16', 'Clothing', 18.00, 35, 'Europe'),
('2024-01-17', 'Home Appliances', 30.00, 25, 'Asia'),
('2024-01-18', 'Electronics', 50.00, 50, 'North America'),
('2024-01-18', 'Clothing', 22.00, 45, 'Europe'),
('2024-01-19', 'Home Appliances', 28.00, 30, 'Asia'),
('2024-02-01', 'Electronics', 55.00, 55, 'North America'),
('2024-02-01', 'Clothing', 25.00, 40, 'Europe'),
('2024-02-02', 'Home Appliances', 35.00, 27, 'Asia'),
('2024-02-03', 'Electronics', 60.00, 60, 'North America'),
('2024-02-03', 'Clothing', 23.00, 38, 'Europe'),
('2024-02-04', 'Home Appliances', 32.00, 32, 'Asia'),
('2024-02-05', 'Electronics', 65.00, 65, 'North America'),
('2024-02-05', 'Clothing', 24.00, 42, 'Europe'),
('2024-02-06', 'Home Appliances', 40.00, 28, 'Asia'),
('2024-03-01', 'Electronics', 70.00, 70, 'North America'),
('2024-03-01', 'Clothing', 26.00, 50, 'Europe'),
('2024-03-02', 'Home Appliances', 45.00, 35, 'Asia');