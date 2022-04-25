/*
Navicat MySQL Data Transfer

Source Server         : myconnect
Source Server Version : 80027
Source Host           : localhost:3306
Source Database       : db_book

Target Server Type    : MYSQL
Target Server Version : 80027
File Encoding         : 65001

Date: 2021-12-10 16:57:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tb_book
-- ----------------------------
DROP TABLE IF EXISTS `tb_book`;
CREATE TABLE `tb_book` (
  `Bid` int NOT NULL AUTO_INCREMENT,
  `Bclass` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Bname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Bprice` decimal(10,2) NOT NULL,
  `Bnum` int DEFAULT NULL,
  `Bauthor` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT '',
  PRIMARY KEY (`Bid`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of tb_book
-- ----------------------------
INSERT INTO `tb_book` VALUES ('1', '童话', '两只老虎', '38.00', '1', '我');
INSERT INTO `tb_book` VALUES ('2', '恐怖', '你的名字', '40.00', '1', '我');
INSERT INTO `tb_book` VALUES ('3', '爱情', '龙族', '59.00', '3', '我');
INSERT INTO `tb_book` VALUES ('6', '童话', '一只龙', '534.00', '2', '我');
INSERT INTO `tb_book` VALUES ('7', '悬疑', '你的龙外婆', '345.00', '1', '我');
INSERT INTO `tb_book` VALUES ('9', '恐怖', '外婆桥', '32.00', '1', '我');
INSERT INTO `tb_book` VALUES ('10', '悬疑', '数据库实验', '999.00', '1', '我');
INSERT INTO `tb_book` VALUES ('16', '绿色', '笑话', '124.00', '1', '怒');
INSERT INTO `tb_book` VALUES ('18', '童话', '微软', '235.00', '2', '覆盖到');
INSERT INTO `tb_book` VALUES ('19', '恐怖', '恐怖小说', '345.00', '2', '你');
INSERT INTO `tb_book` VALUES ('20', '悬疑', '迷城', '43.00', '5', '我');
INSERT INTO `tb_book` VALUES ('21', '爱情', '好运来', '98.00', '1', '小红帽');
INSERT INTO `tb_book` VALUES ('22', '童话', '小红帽', '34.00', '1', '大灰狼');
INSERT INTO `tb_book` VALUES ('25', '悬疑', '黑色', '24.00', '4', '老虎');
INSERT INTO `tb_book` VALUES ('26', '悬疑', 'jojo', '53.00', '1', '荒木');
INSERT INTO `tb_book` VALUES ('27', '童话', '飞机', '34.00', '1', '航空');
INSERT INTO `tb_book` VALUES ('28', '爱情', '数据库', '45.00', '0', '老师');

-- ----------------------------
-- Table structure for tb_pwd
-- ----------------------------
DROP TABLE IF EXISTS `tb_pwd`;
CREATE TABLE `tb_pwd` (
  `user` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of tb_pwd
-- ----------------------------
INSERT INTO `tb_pwd` VALUES ('1', '111111');
INSERT INTO `tb_pwd` VALUES ('1021', '1021');
INSERT INTO `tb_pwd` VALUES ('1048', '111111');
INSERT INTO `tb_pwd` VALUES ('1234', '1111');
INSERT INTO `tb_pwd` VALUES ('12345', '11111');
INSERT INTO `tb_pwd` VALUES ('1528', '111111');
INSERT INTO `tb_pwd` VALUES ('1623', '111111');

-- ----------------------------
-- Table structure for tb_record
-- ----------------------------
DROP TABLE IF EXISTS `tb_record`;
CREATE TABLE `tb_record` (
  `Bid` int NOT NULL,
  `Uname` varchar(255) NOT NULL,
  `class` varchar(255) DEFAULT NULL,
  `datetime` datetime NOT NULL,
  PRIMARY KEY (`Uname`,`datetime`),
  KEY `bid_foreign` (`Bid`) USING BTREE,
  CONSTRAINT `user_foreign` FOREIGN KEY (`Uname`) REFERENCES `tb_user` (`Uuser`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of tb_record
-- ----------------------------
INSERT INTO `tb_record` VALUES ('6', '123', '+1', '2021-12-01 15:36:43');
INSERT INTO `tb_record` VALUES ('7', '123', '+1', '2021-12-06 15:30:53');
INSERT INTO `tb_record` VALUES ('9', '123', '+1', '2021-12-09 15:35:57');
INSERT INTO `tb_record` VALUES ('10', '123', '1', '2021-12-10 02:50:01');
INSERT INTO `tb_record` VALUES ('16', '123', '1', '2021-12-10 03:05:15');
INSERT INTO `tb_record` VALUES ('18', '1234', '-1', '2021-12-10 04:20:12');
INSERT INTO `tb_record` VALUES ('19', '1234', '-1', '2021-12-10 04:26:07');
INSERT INTO `tb_record` VALUES ('20', '1234', '+1', '2021-12-10 04:42:32');
INSERT INTO `tb_record` VALUES ('21', '1234', '+1', '2021-12-10 04:46:09');
INSERT INTO `tb_record` VALUES ('22', '1234', '1', '2021-12-10 05:51:49');
INSERT INTO `tb_record` VALUES ('25', '1234', '1', '2021-12-10 06:30:34');
INSERT INTO `tb_record` VALUES ('26', '1234', '-1', '2021-12-10 06:32:22');
INSERT INTO `tb_record` VALUES ('27', '1234', '-1', '2021-12-10 06:32:56');
INSERT INTO `tb_record` VALUES ('16', '1234', '-1', '2021-12-10 06:33:43');
INSERT INTO `tb_record` VALUES ('20', '1234', '1', '2021-12-10 06:33:53');
INSERT INTO `tb_record` VALUES ('3', '1234', '-1', '2021-12-10 06:34:29');
INSERT INTO `tb_record` VALUES ('2', '1234', '1', '2021-12-10 10:22:31');
INSERT INTO `tb_record` VALUES ('1', '1234', '1', '2021-12-10 10:41:51');
INSERT INTO `tb_record` VALUES ('0', '1234', '1', '2021-12-10 10:42:22');
INSERT INTO `tb_record` VALUES ('27', '1234', '1', '2021-12-10 15:23:32');
INSERT INTO `tb_record` VALUES ('25', '1234', '-1', '2021-12-10 15:27:51');
INSERT INTO `tb_record` VALUES ('28', '1234', '1', '2021-12-10 16:21:37');
INSERT INTO `tb_record` VALUES ('28', '1234', '-1', '2021-12-10 16:22:32');
INSERT INTO `tb_record` VALUES ('1', '12345', '1', '2021-12-10 03:07:49');
INSERT INTO `tb_record` VALUES ('2', '12345', '+1', '2021-12-17 15:28:55');
INSERT INTO `tb_record` VALUES ('3', '12345', '-1', '2021-12-26 15:36:12');
INSERT INTO `tb_record` VALUES ('0', '1245', '1', '2021-12-10 02:35:16');
INSERT INTO `tb_record` VALUES ('0', '1245', '1', '2021-12-10 04:42:05');
INSERT INTO `tb_record` VALUES ('0', '1245', '1', '2021-12-10 04:44:56');
INSERT INTO `tb_record` VALUES ('0', '6456', '1', '2021-12-10 05:23:08');
INSERT INTO `tb_record` VALUES ('0', '6456', '1', '2021-12-10 05:38:02');
INSERT INTO `tb_record` VALUES ('0', '6456', '1', '2021-12-10 05:49:39');

-- ----------------------------
-- Table structure for tb_user
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `Uid` int NOT NULL AUTO_INCREMENT,
  `Uuser` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Uname` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Uclass` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `Usex` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `Utelephone` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`Uid`,`Uuser`),
  KEY `Uname` (`Uname`),
  KEY `Uuser` (`Uuser`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('1', '123', '章清风', '管理员', '男', '1234');
INSERT INTO `tb_user` VALUES ('2', '1234', '借口借口', '管理员', '女', '245235235');
INSERT INTO `tb_user` VALUES ('3', '12345', '小钱', '会员', '女', null);
INSERT INTO `tb_user` VALUES ('5', '1245', '小孙', '管理员', '女', null);
INSERT INTO `tb_user` VALUES ('8', '6456', 'nkasd', '会员', null, null);

-- ----------------------------
-- View structure for my_buy
-- ----------------------------
DROP VIEW IF EXISTS `my_buy`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `my_buy` AS select `tb_record`.`Uname` AS `Uname`,`tb_book`.`Bclass` AS `Bclass`,`tb_book`.`Bname` AS `Bname`,`tb_book`.`Bprice` AS `Bprice`,`tb_record`.`datetime` AS `datetime` from (`tb_book` join `tb_record`) where ((`tb_book`.`Bid` = `tb_record`.`Bid`) and (`tb_record`.`class` = -(1))) ;

-- ----------------------------
-- View structure for my_sold
-- ----------------------------
DROP VIEW IF EXISTS `my_sold`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `my_sold` AS select `tb_record`.`Uname` AS `Uname`,`tb_book`.`Bname` AS `Bname`,`tb_book`.`Bprice` AS `Bprice`,`tb_record`.`datetime` AS `datetime`,`tb_book`.`Bclass` AS `Bclass` from (`tb_record` join `tb_book`) where ((`tb_book`.`Bid` = `tb_record`.`Bid`) and (`tb_record`.`class` = 1)) ;
DROP TRIGGER IF EXISTS `book_add`;
DELIMITER ;;
CREATE TRIGGER `book_add` AFTER INSERT ON `tb_book` FOR EACH ROW begin
insert into tb_record values(new.bid,1234,1,sysdate());
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `book_update`;
DELIMITER ;;
CREATE TRIGGER `book_update` AFTER UPDATE ON `tb_book` FOR EACH ROW begin
insert into tb_record values(new.bid,1234,NEW.Bnum-OLD.Bnum,sysdate());
end
;;
DELIMITER ;
DROP TRIGGER IF EXISTS `useradd`;
DELIMITER ;;
CREATE TRIGGER `useradd` AFTER INSERT ON `tb_user` FOR EACH ROW begin
insert into tb_pwd values(new.Uuser,'111111');
end
;;
DELIMITER ;
