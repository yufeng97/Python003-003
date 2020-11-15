USE geekbang;

DROP TABLE IF EXISTS `zdm_phone`;
CREATE TABLE zdm_phone(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `brand` varchar(100),
    `article_title` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `phone_comment`;
CREATE TABLE phone_comment(
    `id` INT UNSIGNED AUTO_INCREMENT,
    `article_id` int UNSIGNED,
    `username` varchar(100),
    `comment` TEXT NOT NULL,
    `datetime` datetime,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`article_id`) REFERENCES `zdm_phone` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
