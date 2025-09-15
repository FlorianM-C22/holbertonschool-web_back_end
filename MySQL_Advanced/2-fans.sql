-- 2. Best band ever!

-- Select origin and nb_fans columns
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans) DESC;