-- Writes a script that lists all cities contained in the database hbtn_0d_usa.
-- list all cities in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON states.id = cities.state_id ORDER BY cities.id;