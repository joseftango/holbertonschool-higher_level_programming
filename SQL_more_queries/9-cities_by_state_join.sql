-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities 
INNER JOIN states
WHERE cities.state_id = states.id;
