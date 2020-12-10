/* Iteration #1. */
SELECT DISTINCT name
FROM babies
WHERE name LIKE "S%"
LIMIT 20;
/* Iteration #2. */
SELECT DISTINCT name,
    gender,
    number
FROM babies
WHERE year = 1880
ORDER BY number DESC
LIMIT 10;