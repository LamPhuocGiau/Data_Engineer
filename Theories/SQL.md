# Structured Query Language (SQL)
## Table of contents
- [Querying single table](#Querying-single-table)
- [Aliases](#Aliases)
- [Filtering the output](#Filtering-the-output)
- [Querying multible tables](#Querying-multible-tables)
## Querying single table
Country table:                          
id | name | population | area           
--- | --- | --- | ---                   
1 | France | 66600000 | 640680          
2 | Germany | 80700000 | 357000         
... | ... |  ... | ...                  

City table:
Id | name | country_id | population | rating 
--- | --- | --- | --- | ---
1 | Paris | 1 | 2243000 | 5 
2 | Berlin | 2 | 3460000 | 3 
...| ... | ... | ... | ...

Fetch all columns from the country table:
```
    SELECT *
    FROM country;
```
Fetch id and name columns from the city table:
```
    SELECT id, name
    FROM city;
```
Fetch city names sorted by the rating column in the DESCending order:
```
    SELECT name
    FROM city
    ORDER BY rating DESC;
```    
Fetch city names sorted by the rating column in the default ASCending order:
```
    SELECT name
    FROM city
    ORDER BY rating [ASC];
```
[(Back to top)](#table-of-contents)
## Aliases
Columns
```
    SELECT name AS city_name
    FROM city;
```
Tables
```
    SELECT co.name, ci.name
    FROM city AS ci
    JOIN country AS co
     ON ci.country_id = co.id;
```
[(Back to top)](#table-of-contents)
## Filtering the output
**Comparison operators**.

Fetch names of cities that have a rating above 3:
```
    SELECT name
    FROM city
    WHERE rating > 3;
```
Fetch names of cities that are neither Berlin nor Madrid:
```
    SELECT name
    FROM city
    WHERE name != 'Berlin'
     AND name != 'Madrid';
```
**Text operators**.

Fetch names of cities that start with a 'P' or end with an 's':
```
    SELECT name
    FROM city
    WHERE name LIKE 'P%'
     OR name LIKE '%s';
```
Fetch names of cities that start with any letter followed by 'ublin' (like Dublin in Ireland or Lublin in Poland):
```
    SELECT name
    FROM city
    WHERE name LIKE '_ublin';
```
**Other operators**.

Fetch names of cities that have a population between 500K and 5M:
```
    SELECT name
    FROM city
    WHERE population BETWEEN 500000 AND 5000000;
```
Fetch names of cities that don't miss a rating value:
```
    SELECT name
    FROM city
    WHERE rating IS NOT NULL;
```
Fetch names of cities that are in countries with IDs 1, 4, 7, or 8:
```
    SELECT name
    FROM city
    WHERE country_id IN (1, 4, 7, 8);
```
[(Back to top)](#table-of-contents)
## Querying multible tables
**Inner join**.

JOIN (or explicitly INNER JOIN) returns rows that have matching values in both tables.
```
        SELECT city.name, country.name
        FROM city
        [INNER] JOIN country
         ON city.country_id = country.id;
```
![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Images/inner_join.png)
**Left join**.

LEFT JOIN returns all rows from the left table with corresponding rows from the right table. If there's no matching row, NULLs are returned as values from the second table
```
SELECT city.name, country.name
FROM city
LEFT JOIN country
 ON city.country_id = country.id;
```
![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Images/left_join.png)
**Right join**.

RIGHT JOIN returns all rows from the right table with corresponding rows from the left table. If there's no matching row, NULLs are returned as values from the left table
```
SELECT city.name, country.name
FROM city
RIGHT JOIN country
 ON city.country_id = country.id;
```
![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Images/right_join.png)
**Full join**.

FULL JOIN (or explicitly FULL OUTER JOIN) returns all rows from both tables – if there's no matching row in the second table, NULLs are returned.
```
SELECT city.name, country.name
FROM city
FULL [OUTER] JOIN country
 ON city.country_id = country.id;
```
![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Images/full_join.png)
**Cross join**.

CROSS JOIN returns all possible combinations of rows from both tables. There are two syntaxes available.
```
SELECT city.name, country.name
FROM city
CROSS JOIN country;
SELECT city.name, country.name
FROM city, country;
```
![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Images/cross_join.png)
**Natural join**.

NATURAL JOIN will join tables by all columns with the same name.
```
SELECT city.name, country.name
FROM city
NATURAL JOIN country;
```
![alt text](https://github.com/LamPhuocGiau/Data_Engineer/blob/main/Images/natural_join.png)
NATURAL JOIN used these columns to match rows: city.id, city.name, country.id, country.name NATURAL JOIN is very rarely used in practice.
[(Back to top)](#table-of-contents)


















