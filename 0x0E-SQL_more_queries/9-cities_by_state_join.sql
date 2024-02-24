-- script that lists all cities contained in the database hbtn_0d_usa.

SELECT id, name, states.name
FROM cities
JOIN states ON state_id.cities = states.id
ORDER BY cities.id ASC;
