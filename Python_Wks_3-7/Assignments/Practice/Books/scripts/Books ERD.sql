-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Books_ERD
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Books_ERD` ;

-- -----------------------------------------------------
-- Schema Books_ERD
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Books_ERD` DEFAULT CHARACTER SET utf8 ;
USE `Books_ERD` ;

-- -----------------------------------------------------
-- Table `Books_ERD`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Books_ERD`.`authors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Books_ERD`.`books`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Books_ERD`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NULL,
  `num_of_pages` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Books_ERD`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Books_ERD`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `author_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_favorites_users_idx` (`author_id` ASC) VISIBLE,
  INDEX `fk_favorites_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_favorites_users`
    FOREIGN KEY (`author_id`)
    REFERENCES `Books_ERD`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_favorites_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `Books_ERD`.`books` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Books_ERD`.`follows`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Books_ERD`.`follows` (
  `followed_user_id` INT NOT NULL,
  `follower_id` INT NOT NULL,
  `id` INT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`followed_user_id`, `follower_id`),
  INDEX `fk_users_has_users_users2_idx` (`follower_id` ASC) VISIBLE,
  INDEX `fk_users_has_users_users1_idx` (`followed_user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_users_users1`
    FOREIGN KEY (`followed_user_id`)
    REFERENCES `Books_ERD`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_users_users2`
    FOREIGN KEY (`follower_id`)
    REFERENCES `Books_ERD`.`authors` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
