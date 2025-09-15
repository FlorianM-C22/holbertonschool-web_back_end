-- 3. Old school band

SELECT band_name, (IFNULL(split, 2024) - formed) as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY (IFNULL(split, 2024) - formed) DESC;