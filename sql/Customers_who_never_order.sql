# Write your MySQL query statement below
# Select customers.name from customers
# SELECT Column_Name1 AS New_Column_Name, Column_Name2  As New_Column_Name FROM Table_Name;  
# left join to combine 

# select name as Customers from Customers
# Left join Orders on Customers.id = orders.customerid
# Where orders.customerid is null

Select name as Customers from Customers
left join Orders as o on Customers.id = o.customerid
where o.customerid is null