# Write your MySQL query statement below
# Swap salaries for Males & Females
Update Salary
Set sex = if(sex = 'm','f','m')
