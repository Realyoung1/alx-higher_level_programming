-- I listed all cities contained in the database hbtn_0d_usa
-- Best School






SELECT c.id, c.name, s.name FROM cities AS c, states AS s WHERE c.state_id = s.id;
