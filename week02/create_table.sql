CREATE DATABASE IF NOT EXISTS geekbang;
USE geekbang;
CREATE TABLE IF NOT EXISTS maoyan_movie(
    `movie_id` INT UNSIGNED AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `category` VARCHAR(100) NOT NULL,
    `release_time` VARCHAR(100),
    PRIMARY KEY (`movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
