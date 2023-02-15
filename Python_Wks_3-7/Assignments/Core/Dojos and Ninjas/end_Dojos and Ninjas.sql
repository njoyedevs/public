-- Query: Create 3 new dojos
-- INSERT INTO `dojos_and_ninjas`.`dojos` (`name`) VALUES ('Dojo_1'),( 'Dojo_2'), ('Dojo_3');

-- Query: Delete the 3 dojos you just created
-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM `dojos_and_ninjas`.`dojos`;

-- Query: Create 3 more dojos
--  INSERT INTO `dojos_and_ninjas`.`dojos` (`name`) VALUES ('Dojo_1'),( 'Dojo_2'), ('Dojo_3');

--  SELECT * FROM dojos;

-- Query: Create 3 ninjas that belong to the first dojo
-- INSERT INTO `dojos_and_ninjas`.`ninjas` (`first_name`,`last_name`, `age`, `dojo_id`) VALUES ('Bob', 'Jones', '48', '1'),( 'Jane', 'Jones', '33', '1'), ('Al', 'Summers', '8', '1');

-- Query: Create 3 ninjas that belong to the second dojo
-- INSERT INTO `dojos_and_ninjas`.`ninjas` (`first_name`,`last_name`, `age`, `dojo_id`) VALUES ('Sam', 'Jackson', '55', '2'),( 'Bruce', 'Willis', '60', '2'), ('John', 'Travolta', '60', '2');

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO `dojos_and_ninjas`.`ninjas` (`first_name`,`last_name`, `age`, `dojo_id`) VALUES ('Thor', 'Odenson', '10000', '3'),( 'Oden', 'Wed', '250000', '3'), ('Loke', 'Swedan', '18000', '3');

SELECT * FROM ninjas;







