-- List all cities of California using a subquery and order by cities.id
SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
