# 1. Write a query to get Product name and quantity/unit.  
SELECT northwind.products.product_name, northwind.products.quantity_per_unit FROM northwind.products;
# 2. Write a query to get current Product list (Product ID and name).  
SELECT northwind.products.product_name, northwind.products.id FROM northwind.products WHERE discontinued = 0;
# 3. Write a query to get discontinued Product list (Product ID and name). 
SELECT northwind.products.product_name, northwind.products.id FROM northwind.products WHERE discontinued = 1;
# 4. Write a query to get most expense and least expensive Product list (name and unit price).
SELECT northwind.products.product_name, northwind.products.standard_cost FROM northwind.products 
	WHERE standard_cost = (SELECT MIN(northwind.products.standard_cost) FROM northwind.products)
    OR standard_cost = (SELECT MAX(northwind.products.standard_cost) FROM northwind.products);  
# 5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.
SELECT northwind.products.id, northwind.products.product_name, northwind.products.standard_cost FROM northwind.products WHERE northwind.products.standard_cost < 20;
# 6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
SELECT northwind.products.id, northwind.products.product_name, northwind.products.standard_cost FROM northwind.products WHERE northwind.products.standard_cost BETWEEN 15 AND 25;
# 7. Write a query to get Product list (name, unit price) of above average price.  
SELECT northwind.products.product_name, northwind.products.standard_cost FROM northwind.products 
	WHERE northwind.products.standard_cost > (SELECT AVG(northwind.products.standard_cost) FROM northwind.products);
# 8. Write a query to get Product list (name, unit price) of ten most expensive products.  
SELECT northwind.products.product_name, northwind.products.standard_cost FROM northwind.products 
	ORDER BY northwind.products.standard_cost DESC
    LIMIT 10;
# 9. Write a query to count current and discontinued products. 
SELECT northwind.products.discontinued, COUNT(northwind.products.discontinued) FROM northwind.products GROUP BY  northwind.products.discontinued;
# 10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  

# Stock
SELECT added_table.product_id, (added_table.added - subtracted_table.removed) as Stock FROM
	(SELECT northwind.inventory_transactions.product_id, SUM(northwind.inventory_transactions.quantity) AS added FROM northwind.inventory_transactions WHERE northwind.inventory_transactions.transaction_type = 1 GROUP BY northwind.inventory_transactions.product_id) AS added_table
    NATURAL JOIN
	(SELECT northwind.inventory_transactions.product_id, SUM(northwind.inventory_transactions.quantity) AS removed FROM northwind.inventory_transactions WHERE NOT northwind.inventory_transactions.transaction_type = 1 GROUP BY northwind.inventory_transactions.product_id) AS subtracted_table;
    
 # On Order
SELECT northwind.order_details.product_id, northwind.order_details.quantity as Ordered FROM northwind.order_details WHERE northwind.order_details.status_id = 4;