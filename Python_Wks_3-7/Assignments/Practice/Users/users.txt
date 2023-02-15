-- Query: Create 3 new users
-- INSERT INTO `users`.`users` (`first_name`, `last_name`, `email`) VALUES ('Bob', 'Jones', 'bobjones@yahoo.com'),('Jack', 'Demsey', 'jackdemsey@yahoo.com'), ('Alex', 'Smith', 'alexsmith@yahoo.com');

-- Query: Retrieve all the users
-- SELECT * FROM users;

-- Query: Retrieve the first user using their email address
-- SELECT * FROM users WHERE email = 'alexsmith@yahoo.com';

-- Query: Retrieve the last user using their id
-- SELECT * FROM users WHERE email = 'alexsmith@yahoo.com'; 

-- Query: Change the user with id=3 so their last name is Pancakes
-- UPDATE `users`.`users` SET `last_name` = 'Pancakes' WHERE (`id` = '3');

-- Query: Delete the user with id=2 from the database
-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM `users`.`users` WHERE (`id` = '2');

-- Query: Get all the users, sorted by their first name
-- SELECT * FROM users ORDER BY first_name ASC;

-- BONUS Query: Get all the users, sorted by their first name in descending order
-- SELECT * FROM users ORDER BY first_name DESC;

-- SELECT * FROM users;