-- SQL script that creates a stored procedure `AddBonus`
-- that adds a new correction for a student.
CREATE PROCEDURE AddBonus (
    IN user_id INT, 
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
  INSERT INTO projects (name) 
  SELECT project_name 
  WHERE NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name);
  
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);

END;