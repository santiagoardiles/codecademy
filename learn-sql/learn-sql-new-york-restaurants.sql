/* Query #1. */
SELECT
    *
FROM
    nomnom;

/* Query #2. */
SELECT
    DISTINCT neighborhood
FROM
    nomnom;

/* Query #3. */
SELECT
    DISTINCT cuisine
FROM
    nomnom;

/* Query #4. */
SELECT
    *
FROM
    nomnom
WHERE
    cuisine = "Chinese";

/* Query #5. */
SELECT
    *
FROM
    nomnom
WHERE
    review >= 4;

/* Query #6. */
SELECT
    *
FROM
    nomnom
WHERE
    cuisine = "Italian"
    AND price LIKE "%$$$%";

/* Query #7. */
SELECT
    *
FROM
    nomnom
WHERE
    name LIKE "%meatball%";

/* Query #8. */
SELECT
    *
FROM
    nomnom
WHERE
    neighborhood = "Midtown"
    OR neighborhood = "Downtown"
    OR neighborhood = "Chinatown";

/* Query #9. */
SELECT
    *
FROM
    nomnom
WHERE
    health IS NULL;

/* Query #10. */
SELECT
    *
FROM
    nomnom
ORDER BY
    review DESC
LIMIT
    10;

/* Query #11. */
SELECT
    name,
    CASE
        WHEN review > 4.5 THEN "Extraordinary"
        WHEN review > 4 THEN "Excellent"
        WHEN review > 3 THEN "Good"
        WHEN review > 2 THEN "Fair"
        ELSE "Poor"
    END AS "Review"
FROM
    nomnom;