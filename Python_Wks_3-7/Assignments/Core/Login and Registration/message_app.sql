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
CREATE SCHEMA IF NOT EXISTS `message_app` DEFAULT CHARACTER SET utf8 ;
USE `message_app` ;

-- -----------------------------------------------------
-- Table `message_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `message_app`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `optimism` VARCHAR(45) NULL,
  `password` VARCHAR(60) NULL,
  `confirm` VARCHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `message_app`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `message_app`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `recipient_id` INT NULL,
  `message` VARCHAR(250) NULL,
  `read` VARCHAR(5) NULL DEFAULT 'False',
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `message_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `message_app`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `message_app`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(250) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id` INT NOT NULL,
  `message_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_messages1_idx` (`message_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `message_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`message_id`)
    REFERENCES `message_app`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
