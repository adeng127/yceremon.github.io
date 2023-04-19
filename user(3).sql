/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.0.32 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Email` varchar(765),
  `username` varchar(765),
  `password` varchar(765),
  PRIMARY KEY (`id`)
);
insert into `user` (`id`, `Email`, `username`, `password`) values('1','123@qq.com','tom','1234');
insert into `user` (`id`, `Email`, `username`, `password`) values('2','12342@qq.com','bob','123456');
