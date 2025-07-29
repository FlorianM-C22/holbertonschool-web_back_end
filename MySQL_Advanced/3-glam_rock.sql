-- 3. Old school band

-- Select band_name and style columns
SELECT band_name, style
FROM metal_bands
-- Filter for glam rock bands
WHERE style LIKE '%Glam rock%'
-- Order by the number of fans in descending order
ORDER BY fans DESC;