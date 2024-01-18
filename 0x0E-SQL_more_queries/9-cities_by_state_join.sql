-- script in which Each record should display: cities.id - cities.name - states.name
USE hbtn_0d_usa;

SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities
INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id DESC;
