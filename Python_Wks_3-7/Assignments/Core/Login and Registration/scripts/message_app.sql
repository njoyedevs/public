-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema message_app
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `message_app` ;

-- -----------------------------------------------------
-- Schema message_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `message_app` DEFAULT CHARACTER SET utf8mb3 ;
USE `message_app` ;

-- -----------------------------------------------------
-- Table `message_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `message_app`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `optimism` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(60) NULL DEFAULT NULL,
  `confirm` VARCHAR(60) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `message_app`.`friends`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `message_app`.`friends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `friend_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_friendships_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_friendships_users2_idx` (`friend_id` ASC) VISIBLE,
  CONSTRAINT `fk_friendships_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `message_app`.`users` (`id`),
  CONSTRAINT `fk_friendships_users2`
    FOREIGN KEY (`friend_id`)
    REFERENCES `message_app`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 26
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `message_app`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `message_app`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `recipient_id` INT NULL DEFAULT NULL,
  `message` VARCHAR(250) NULL DEFAULT NULL,
  `read` VARCHAR(5) NULL DEFAULT 'False',
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `message_app`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
