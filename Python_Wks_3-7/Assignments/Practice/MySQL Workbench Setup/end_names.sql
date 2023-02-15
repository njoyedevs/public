-- Write the query to select all the names in the database.
-- The columns should appear, even if there are no records in the database yet.
-- SELECT name FROM names;

-- Insert your own name into the database!
-- INSERT INTO `names`.`names` (`name`) VALUES ('Terrell Owens');

-- Insert another name or, NINJA BONUS: insert more than one name in a single statement.
-- INSERT INTO `names`.`names` (`name`) VALUES ('Bob Jones'),( 'Jack Demsey'), ('Alex Smith');

-- Update name
--  UPDATE `names`.`names` SET `name` = 'Donovan McNabe';

-- Optional: Try creating, updating and deleting records using the statements you've learn about.
-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM `names`.`names` WHERE (`name` = 'Donovan McNabe');

SELECT * FROM names;