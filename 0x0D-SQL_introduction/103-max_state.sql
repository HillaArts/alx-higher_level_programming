-- Assuming the temperatures table structure is like this:
-- CREATE TABLE temperatures (
--   id INT AUTO_INCREMENT PRIMARY KEY,
--   state VARCHAR(255),
--   temperature DECIMAL(5, 2),
--   month VARCHAR(3),
--   year INT
-- );

-- Display the max temperature of each state ordered by state name
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

