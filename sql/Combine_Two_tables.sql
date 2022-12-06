# Write your MySQL query statement below
SELECT Person.firstName, Person.lastName, Address.City, Address.State from Address LEFT JOIN Person on Person.PersonId = Address.PersonId;