-- script in which Each record should display: cities.id - cities.name - states.name

SELECT c.id AS id, c.name AS name, s.name AS name FROM cities c
INNER JOIN states s ON s.id = c.state_id
ORDER BY c.id DESC;
