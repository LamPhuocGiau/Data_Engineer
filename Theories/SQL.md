# Structured Query Language (SQL)
## Table of contents
- [Querying single table](#Querying-single-table)
- [Aliases](#Aliases)
- [Filtering the output](#Filtering-the-output)
- [Multible tables]()
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
## Multible table

