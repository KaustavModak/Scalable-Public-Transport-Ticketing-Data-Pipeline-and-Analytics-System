CREATE DATABASE transport;

USE transport;

CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY,
    user_id INT,
    route VARCHAR(10),
    price DOUBLE,
    city VARCHAR(20),
    vehicle_type VARCHAR(20),
    price_norm DOUBLE,
    price_category VARCHAR(20)
);

SELECT COUNT(*) FROM tickets;

-- Shows first few records
SELECT * FROM tickets LIMIT 10;

-- Calculates total revenue for each route
SELECT route, SUM(price) AS total_revenue
FROM tickets
GROUP BY route
ORDER BY total_revenue DESC;

-- Shows which city generates highest revenue
SELECT city, SUM(price) AS total_revenue
FROM tickets
GROUP BY city
ORDER BY total_revenue DESC;

-- Compare Bus vs Metro vs Train revenue
SELECT vehicle_type, SUM(price) AS total_revenue
FROM tickets
GROUP BY vehicle_type
ORDER BY total_revenue DESC;

-- COUNT ANALYSIS: NUMBER OF TICKETS PER ROUTE
SELECT route, COUNT(*) AS total_tickets
FROM tickets
GROUP BY route
ORDER BY total_tickets DESC;

-- Assign rank based on number of tickets
SELECT route,
       COUNT(*) AS total_tickets,
       RANK() OVER (ORDER BY COUNT(*) DESC) AS route_rank
FROM tickets
GROUP BY route;

-- TOP CITY BY REVENUE
SELECT city, SUM(price) AS revenue
FROM tickets
GROUP BY city
ORDER BY revenue DESC
LIMIT 1;

