-- 7. Average score

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE average_user FLOAT;

SELECT AVG(score) INTO average_user
FROM corrections AS c
WHERE c.user_id = user_id;

UPDATE users
SET average_score = average_user
WHERE id = user_id;

END;
//
DELIMITER ;