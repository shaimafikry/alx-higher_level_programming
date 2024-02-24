-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.

SELECT cities.name FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
WHERE state_id = cities.id
ORDER BY cities.id DESC;
