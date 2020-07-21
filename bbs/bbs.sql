/*
SQLyog Ultimate v11.24 (64 bit)
MySQL - 5.5.53 : Database - flask_bbs
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`flask_bbs` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `flask_bbs`;

/*Table structure for table `alembic_version` */

DROP TABLE IF EXISTS `alembic_version`;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `alembic_version` */

insert  into `alembic_version`(`version_num`) values ('bafcee725f91');

/*Table structure for table `banner` */

DROP TABLE IF EXISTS `banner`;

CREATE TABLE `banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `image_url` varchar(255) NOT NULL,
  `link_url` varchar(255) NOT NULL,
  `priority` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `is_delete` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Data for the table `banner` */

insert  into `banner`(`id`,`name`,`image_url`,`link_url`,`priority`,`create_time`,`is_delete`) values (2,'C#','https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2097526952,1617711139&fm=26&gp=0.jpg','https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=C%23%E5%9B%BE%E7%89%87',3,'2020-06-18 12:45:48',0),(3,'python','https://dss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3501657826,149658298&fm=26&gp=0.jpg','https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=Python%E5%9B%BE%E7%89%87',4,'2020-06-18 13:11:04',0),(4,'Go','https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1552226973,1813125703&fm=26&gp=0.jpg','https://www.baidu.com/s?wd=go%E8%AF%AD%E8%A8%80%E5%9B%BE%E7%89%87',2,'2020-06-19 14:06:36',1),(5,'PHP','https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=298939098,990023656&fm=26&gp=0.jpg','https://www.baidu.com/s?wd=php%E5%9B%BE%E7%89%87',1,'2020-06-19 14:07:17',1);

/*Table structure for table `cms_board` */

DROP TABLE IF EXISTS `cms_board`;

CREATE TABLE `cms_board` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `cms_board` */

insert  into `cms_board`(`id`,`name`,`create_time`) values (1,'Python','2020-06-19 15:52:51'),(2,'Go','2020-06-19 16:02:13'),(3,'PHp','2020-06-19 16:27:53'),(4,'C#','2020-06-19 16:19:07'),(5,'Java',NULL),(6,'HHH','2020-06-20 23:45:01');

/*Table structure for table `cms_role` */

DROP TABLE IF EXISTS `cms_role`;

CREATE TABLE `cms_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `desc` varchar(50) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `permissions` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `cms_role` */

insert  into `cms_role`(`id`,`name`,`desc`,`create_time`,`permissions`) values (1,'访问者','只能查看数据，不能修改数据','2020-06-12 17:33:15',1),(2,'运营人员','管理帖子，管理评论，管理前台用户','2020-06-12 17:33:15',23),(3,'管理员','拥有本系统大部分权限','2020-06-12 17:33:15',63),(4,'开发者','拥有所有权限','2020-06-12 17:33:15',255);

/*Table structure for table `cms_role_user` */

DROP TABLE IF EXISTS `cms_role_user`;

CREATE TABLE `cms_role_user` (
  `cms_role_id` int(11) DEFAULT NULL,
  `cms_user_id` int(11) DEFAULT NULL,
  KEY `cms_role_id` (`cms_role_id`),
  KEY `cms_user_id` (`cms_user_id`),
  CONSTRAINT `cms_role_user_ibfk_1` FOREIGN KEY (`cms_role_id`) REFERENCES `cms_role` (`id`),
  CONSTRAINT `cms_role_user_ibfk_2` FOREIGN KEY (`cms_user_id`) REFERENCES `cms_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cms_role_user` */

insert  into `cms_role_user`(`cms_role_id`,`cms_user_id`) values (3,4);

/*Table structure for table `cms_user` */

DROP TABLE IF EXISTS `cms_user`;

CREATE TABLE `cms_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `join_time` datetime DEFAULT NULL,
  `_password` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `cms_user` */

insert  into `cms_user`(`id`,`username`,`email`,`join_time`,`_password`) values (3,'admin','456@qq.com','2020-06-09 15:26:29','pbkdf2:sha256:150000$pSuMRqb5$244ca9a5ba48f2682089dc272d4fe86ec7a63492409f5baea262ce98124e9c23'),(4,'djt','719106933@qq.com','2020-06-09 18:19:49','pbkdf2:sha256:150000$NvNrVAnV$c6476f5d90260381d6c6e962fed36b09af7b50b0a412b187069e6ec2e6d7382c');

/*Table structure for table `comment` */

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text NOT NULL,
  `create_time` datetime DEFAULT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `post_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `front_user` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `comment` */

insert  into `comment`(`id`,`content`,`create_time`,`author_id`,`post_id`) values (1,'<p><strong><em>这篇Python文章写的真好</em></strong></p>','2020-06-22 00:03:39','2a6NaNpmtdtXLwBCLEkeF3',1),(2,'<p>231231231</p>','2020-06-22 15:38:55','2a6NaNpmtdtXLwBCLEkeF3',4),(3,'<p>45645645645</p>','2020-06-22 15:38:58','2a6NaNpmtdtXLwBCLEkeF3',4),(4,'<p>456456456456789</p>','2020-06-22 15:39:02','2a6NaNpmtdtXLwBCLEkeF3',1),(5,'<p>7897894323786645645</p>','2020-06-22 15:39:05','2a6NaNpmtdtXLwBCLEkeF3',1),(6,'<p>7897895464536453</p>','2020-06-22 15:39:07','2a6NaNpmtdtXLwBCLEkeF3',1),(7,'<p>879534546</p>','2020-06-22 15:39:11','2a6NaNpmtdtXLwBCLEkeF3',9),(8,'<p>/45645645645</p>','2020-06-22 15:39:15','2a6NaNpmtdtXLwBCLEkeF3',9),(9,'<p>456</p>','2020-06-22 15:39:17','2a6NaNpmtdtXLwBCLEkeF3',9),(10,'<p>686</p>','2020-06-22 15:39:18','2a6NaNpmtdtXLwBCLEkeF3',9),(11,'<p>/9*/*/9</p>','2020-06-22 15:39:20','2a6NaNpmtdtXLwBCLEkeF3',9),(12,'<p>4656456</p>','2020-06-22 15:45:13','2a6NaNpmtdtXLwBCLEkeF3',1),(13,'<p>456456456456</p>','2020-06-22 15:45:14','2a6NaNpmtdtXLwBCLEkeF3',1),(14,'<p>456456456</p>','2020-06-22 15:45:15','2a6NaNpmtdtXLwBCLEkeF3',1);

/*Table structure for table `front_user` */

DROP TABLE IF EXISTS `front_user`;

CREATE TABLE `front_user` (
  `id` varchar(50) NOT NULL,
  `telephone` varchar(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `_password` varchar(200) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `realname` varchar(100) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `signature` varchar(100) DEFAULT NULL,
  `gender` enum('MALE','FEMAIL','SECRET','UNKNOW') DEFAULT NULL,
  `join_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `telephone` (`telephone`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `front_user` */

insert  into `front_user`(`id`,`telephone`,`username`,`_password`,`email`,`realname`,`avatar`,`signature`,`gender`,`join_time`) values ('2a6NaNpmtdtXLwBCLEkeF3','13714160953','djt','pbkdf2:sha256:150000$uWwyqVP0$193659600f0285d1c54ccbf657e9c363d80c0f9bba8d210df1a5e31488c7dfa5',NULL,NULL,NULL,NULL,'UNKNOW','2020-06-15 00:42:22'),('hPAh9ANr685MxjnBBQpVoi','13716161717','hello','pbkdf2:sha256:150000$z9VJZo5C$3734c9a665e041fb8b55bea0f535acf330c93b9f91e8d1a5014da1e165b1ebf2',NULL,NULL,NULL,NULL,'UNKNOW','2020-06-16 10:49:41'),('NhJVovormJZURm5nf6asJp','19874700953','admin','pbkdf2:sha256:150000$P9GNaVKK$66614a2fe419e852ad079b6a52f8af79187b5d493cf3a4765c2cfba05bb1361b',NULL,NULL,NULL,NULL,'UNKNOW','2020-06-16 01:02:27');

/*Table structure for table `highlight_post` */

DROP TABLE IF EXISTS `highlight_post`;

CREATE TABLE `highlight_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `highlight_post_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

/*Data for the table `highlight_post` */

insert  into `highlight_post`(`id`,`post_id`,`create_time`) values (13,1,'2020-06-21 17:46:37'),(14,4,'2020-06-21 17:46:41'),(15,3,'2020-06-21 17:46:46'),(16,7,'2020-06-22 01:34:45'),(17,9,'2020-06-22 01:34:46'),(18,13,'2020-06-22 01:34:47');

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `content` text NOT NULL,
  `content_html` text,
  `create_time` datetime DEFAULT NULL,
  `board_id` int(11) DEFAULT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `read_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `board_id` (`board_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `front_user` (`id`),
  CONSTRAINT `post_ibfk_2` FOREIGN KEY (`board_id`) REFERENCES `cms_board` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=254 DEFAULT CHARSET=utf8;

/*Data for the table `post` */

insert  into `post`(`id`,`title`,`content`,`content_html`,`create_time`,`board_id`,`author_id`,`read_count`) values (1,'python','# python','<h1>python</h1>','2020-06-20 23:10:38',1,'2a6NaNpmtdtXLwBCLEkeF3',1),(2,'python','# python','<h1>python</h1>','2020-06-20 23:10:48',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(3,'go','![](https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1552226973,1813125703&fm=26&gp=0.jpg)\ngogog','<p><img alt=\"\" src=\"https://dss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1552226973,1813125703&amp;fm=26&amp;gp=0.jpg\">\ngogog</p>','2020-06-20 23:12:09',2,'2a6NaNpmtdtXLwBCLEkeF3',6),(4,'python','# python','<h1>python</h1>','2020-06-20 23:16:06',1,'2a6NaNpmtdtXLwBCLEkeF3',1),(7,'标题：2','内容：2','<p>内容：2</p>','2020-06-22 01:32:53',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(8,'标题：3','内容：3','<p>内容：3</p>','2020-06-22 01:32:53',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(9,'标题：4','内容：4','<p>内容：4</p>','2020-06-22 01:32:53',1,'2a6NaNpmtdtXLwBCLEkeF3',2),(13,'标题：8','内容：8','<p>内容：8</p>','2020-06-22 01:32:54',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(205,'标题：1','内容：1','<p>内容：1</p>','2020-06-22 02:05:09',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(206,'标题：2','内容：2','<p>内容：2</p>','2020-06-22 02:05:09',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(207,'标题：3','内容：3','<p>内容：3</p>','2020-06-22 02:05:09',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(208,'标题：4','内容：4','<p>内容：4</p>','2020-06-22 02:05:09',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(209,'标题：5','内容：5','<p>内容：5</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(210,'标题：6','内容：6','<p>内容：6</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(211,'标题：7','内容：7','<p>内容：7</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(212,'标题：8','内容：8','<p>内容：8</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(213,'标题：9','内容：9','<p>内容：9</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(214,'标题：10','内容：10','<p>内容：10</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(215,'标题：11','内容：11','<p>内容：11</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(216,'标题：12','内容：12','<p>内容：12</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(217,'标题：13','内容：13','<p>内容：13</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(218,'标题：14','内容：14','<p>内容：14</p>','2020-06-22 02:05:10',3,'2a6NaNpmtdtXLwBCLEkeF3',0),(219,'标题：15','内容：15','<p>内容：15</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(220,'标题：16','内容：16','<p>内容：16</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(221,'标题：17','内容：17','<p>内容：17</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(222,'标题：18','内容：18','<p>内容：18</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(223,'标题：19','内容：19','<p>内容：19</p>','2020-06-22 02:05:10',3,'2a6NaNpmtdtXLwBCLEkeF3',0),(224,'标题：20','内容：20','<p>内容：20</p>','2020-06-22 02:05:10',2,'2a6NaNpmtdtXLwBCLEkeF3',0),(225,'标题：21','内容：21','<p>内容：21</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(226,'标题：22','内容：22','<p>内容：22</p>','2020-06-22 02:05:10',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(227,'标题：23','内容：23','<p>内容：23</p>','2020-06-22 02:05:10',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(228,'标题：24','内容：24','<p>内容：24</p>','2020-06-22 02:05:10',2,'2a6NaNpmtdtXLwBCLEkeF3',0),(229,'标题：25','内容：25','<p>内容：25</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(230,'标题：26','内容：26','<p>内容：26</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(231,'标题：27','内容：27','<p>内容：27</p>','2020-06-22 02:05:10',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(232,'标题：28','内容：28','<p>内容：28</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(233,'标题：29','内容：29','<p>内容：29</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(234,'标题：30','内容：30','<p>内容：30</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(235,'标题：31','内容：31','<p>内容：31</p>','2020-06-22 02:05:10',2,'2a6NaNpmtdtXLwBCLEkeF3',0),(236,'标题：32','内容：32','<p>内容：32</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(237,'标题：33','内容：33','<p>内容：33</p>','2020-06-22 02:05:10',2,'2a6NaNpmtdtXLwBCLEkeF3',0),(238,'标题：34','内容：34','<p>内容：34</p>','2020-06-22 02:05:10',2,'2a6NaNpmtdtXLwBCLEkeF3',0),(239,'标题：35','内容：35','<p>内容：35</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(240,'标题：36','内容：36','<p>内容：36</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(241,'标题：37','内容：37','<p>内容：37</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(242,'标题：38','内容：38','<p>内容：38</p>','2020-06-22 02:05:10',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(243,'标题：39','内容：39','<p>内容：39</p>','2020-06-22 02:05:10',5,'2a6NaNpmtdtXLwBCLEkeF3',0),(244,'标题：40','内容：40','<p>内容：40</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(245,'标题：41','内容：41','<p>内容：41</p>','2020-06-22 02:05:10',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(246,'标题：42','内容：42','<p>内容：42</p>','2020-06-22 02:05:10',2,'2a6NaNpmtdtXLwBCLEkeF3',0),(247,'标题：43','内容：43','<p>内容：43</p>','2020-06-22 02:05:10',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(248,'标题：44','内容：44','<p>内容：44</p>','2020-06-22 02:05:10',6,'2a6NaNpmtdtXLwBCLEkeF3',0),(249,'标题：45','内容：45','<p>内容：45</p>','2020-06-22 02:05:11',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(250,'标题：46','内容：46','<p>内容：46</p>','2020-06-22 02:05:11',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(251,'标题：47','内容：47','<p>内容：47</p>','2020-06-22 02:05:11',4,'2a6NaNpmtdtXLwBCLEkeF3',0),(252,'标题：48','内容：48','<p>内容：48</p>','2020-06-22 02:05:11',1,'2a6NaNpmtdtXLwBCLEkeF3',0),(253,'标题：49','内容：49','<p>内容：49</p>','2020-06-22 02:05:11',2,'2a6NaNpmtdtXLwBCLEkeF3',0);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
