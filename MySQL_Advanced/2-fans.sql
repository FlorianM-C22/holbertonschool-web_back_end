-- 2. Best band ever!

-- Select origin and nb_fans columns
SELECT 
    origin, 
    nb_fans,
    RANK() OVER (ORDER BY nb_fans ASC) as rank
FROM metal_bands
ORDER BY nb_fans ASC;