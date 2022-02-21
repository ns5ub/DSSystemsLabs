# 1. Write a query to get Product name and quantity/unit.  
SELECT northwind.products.product_name, northwind.products.quantity_per_unit FROM northwind.products;

# 2. Write a query to get current Product list (Product ID and name).  
SELECT northwind.products.product_name, northwind.products.id FROM northwind.products WHERE discontinued = 0;

# 3. Write a query to get discontinued Product list (Product ID and name). 
SELECT northwind.products.product_name, northwind.products.id FROM northwind.products WHERE discontinued = 1;

# 4. Write a query to get most expense and least expensive Product list (name and unit price).
SELECT DISTINCT northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
	WHERE northwind.order_details.unit_price = (SELECT MIN(northwind.order_details.unit_price) FROM northwind.order_details)
    OR northwind.order_details.unit_price = (SELECT MAX(northwind.order_details.unit_price) FROM northwind.order_details);  
    
# 5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.
SELECT DISTINCT northwind.products.id, northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id 
	WHERE northwind.order_details.unit_price < 20;
    
# 6. Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.  
SELECT DISTINCT northwind.products.id, northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
	WHERE northwind.order_details.unit_price BETWEEN 15 AND 25;
    
# 7. Write a query to get Product list (name, unit price) of above average price.  
SELECT DISTINCT northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
	WHERE northwind.order_details.unit_price > (SELECT AVG(northwind.order_details.unit_price) FROM northwind.order_details);
    
# 8. Write a query to get Product list (name, unit price) of ten most expensive products.  
SELECT DISTINCT northwind.products.product_name, northwind.order_details.unit_price FROM northwind.products JOIN northwind.order_details ON northwind.products.id = northwind.order_details.product_id
	ORDER BY northwind.order_details.unit_price DESC
    LIMIT 10;
    
# 9. Write a query to count current and discontinued products. 
SELECT northwind.products.discontinued, COUNT(northwind.products.discontinued) FROM northwind.products GROUP BY  northwind.products.discontinued;

# 10. Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.  
SELECT northwind.products.product_name, northwind.order_details.quantity AS UnitsOnOrder, northwind.inventory_transactions.quantity AS UnitsOnStock
	FROM northwind.products JOIN northwind.order_details JOIN northwind.inventory_transactions ON northwind.products.id = northwind.order_details.product_id
         AND northwind.order_details.product_id = northwind.inventory_transactions.product_id
	WHERE northwind.inventory_transactions.quantity < northwind.order_details.quantity;

# Not sure whether We need to calculate single stock based on inventory transaction type:
#SELECT added_table.product_id, (added_table.added - subtracted_table.removed) as calc_stock FROM
#	(SELECT northwind.inventory_transactions.product_id, SUM(northwind.inventory_transactions.quantity) AS added FROM northwind.inventory_transactions WHERE northwind.inventory_transactions.transaction_type = 1 GROUP BY northwind.inventory_transactions.product_id) AS added_table
#    NATURAL JOIN
#	(SELECT northwind.inventory_transactions.product_id, SUM(northwind.inventory_transactions.quantity) AS removed FROM northwind.inventory_transactions WHERE NOT northwind.inventory_transactions.transaction_type = 1 GROUP BY northwind.inventory_transactions.product_id) AS subtracted_table;