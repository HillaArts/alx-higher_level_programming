-- Assuming the temperatures table structure is like this:
-- CREATE TABLE temperatures (
--   id INT AUTO_INCREMENT PRIMARY KEY,
--   city VARCHAR(255),
--   temperature DECIMAL(5, 2),
--   month VARCHAR(3),
--   year INT
-- );

-- Display the top 3 cities' temperatures during July and August ordered by temperature (descending)
SELECT city, temperature
FROM temperatures
WHERE (month = 'Jul' OR month = 'Aug')
ORDER BY temperature DESC
LIMIT 3;
