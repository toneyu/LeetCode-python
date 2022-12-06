# Write your MySQL query statement below
Select employee_id, if(employee_id%2 != 0 and name not like 'M%',salary, 0 ) as bonus
from employees
Order by employee_id
