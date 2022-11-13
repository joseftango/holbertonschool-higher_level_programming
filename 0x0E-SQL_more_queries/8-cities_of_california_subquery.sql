-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities IN
WHERE name = (SELECT name FROM cities WHERE name = 'California')
ORDER BY id ASC;
