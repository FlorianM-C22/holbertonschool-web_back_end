-- 10. Safe divide

DELIMITER //
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS float DETERMINISTIC
BEGIN
RETURN IF(b = 0, 0, (a / b));
END;
//
DELIMITER ;