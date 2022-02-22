SELECT dim_customers.last_name, SUM(fact_orders.quantity) as total_quantity, SUM(fact_orders.unit_price) as total_unit_price
FROM fact_orders JOIN dim_customers on fact_orders.customer_id = dim_customers.customer_key
GROUP BY dim_customers.last_name;