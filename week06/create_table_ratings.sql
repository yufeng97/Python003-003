USE geekbang;
DROP TABLE IF EXISTS `ratings`;
CREATE TABLE IF NOT EXISTS ratings(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `star` CHAR(1) NOT NULL,
    `comment` TEXT NOT NULL,
    `comment_date` DATE NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
