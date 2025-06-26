-- List all cities with their corresponding state names, ordered by cities.id
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
