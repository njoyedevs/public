-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema logins
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `logins` ;

-- -----------------------------------------------------
-- Schema logins
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `logins` DEFAULT CHARACTER SET utf8mb3 ;
USE `logins` ;

-- -----------------------------------------------------
-- Table `logins`.`logins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `logins`.`logins` (
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
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `logins`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `logins`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message` VARCHAR(500) NULL DEFAULT NULL,
  `read` VARCHAR(5) NULL DEFAULT 'False',
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `logins_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_logins1_idx` (`logins_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_logins1`
    FOREIGN KEY (`logins_id`)
    REFERENCES `logins`.`logins` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `logins`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `logins`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(250) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `message_id` INT NOT NULL,
  `login_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_has_logins_logins1_idx` (`login_id` ASC) VISIBLE,
  INDEX `fk_messages_has_logins_messages1_idx` (`message_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_has_logins_logins1`
    FOREIGN KEY (`login_id`)
    REFERENCES `logins`.`logins` (`id`),
  CONSTRAINT `fk_messages_has_logins_messages1`
    FOREIGN KEY (`message_id`)
    REFERENCES `logins`.`messages` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
