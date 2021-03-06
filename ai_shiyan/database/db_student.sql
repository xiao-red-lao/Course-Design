/*
Navicat MySQL Data Transfer

Source Server         : mr
Source Server Version : 80019
Source Host           : 127.0.0.1:3306
Source Database       : db_student

Target Server Type    : MYSQL
Target Server Version : 80019
File Encoding         : 65001

Date: 2020-04-21 13:54:22
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tb_class`
-- ----------------------------
DROP TABLE IF EXISTS `tb_class`;
CREATE TABLE `tb_class` (
  `classID` int NOT NULL,
  `gradeID` int NOT NULL,
  `className` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_class
-- ----------------------------
INSERT INTO `tb_class` VALUES ('1', '1', '一班');
INSERT INTO `tb_class` VALUES ('2', '1', '二班');
INSERT INTO `tb_class` VALUES ('3', '1', '三班');
INSERT INTO `tb_class` VALUES ('4', '2', '一班');
INSERT INTO `tb_class` VALUES ('5', '2', '二班');

-- ----------------------------
-- Table structure for `tb_grade`
-- ----------------------------
DROP TABLE IF EXISTS `tb_grade`;
CREATE TABLE `tb_grade` (
  `gradeID` int NOT NULL DEFAULT '1',
  `gradeName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`gradeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_grade
-- ----------------------------
INSERT INTO `tb_grade` VALUES ('1', '初一');
INSERT INTO `tb_grade` VALUES ('2', '初二');
INSERT INTO `tb_grade` VALUES ('3', '初三');

-- ----------------------------
-- Table structure for `tb_student`
-- ----------------------------
DROP TABLE IF EXISTS `tb_student`;
CREATE TABLE `tb_student` (
  `stuID` varchar(20) NOT NULL DEFAULT 'SID00101001',
  `stuName` varchar(20) DEFAULT NULL,
  `classID` int DEFAULT NULL,
  `gradeID` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` char(4) DEFAULT NULL,
  `phone` char(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stuID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_student
-- ----------------------------
INSERT INTO `tb_student` VALUES ('BS0101001', '小王', '1', '1', '20', '男', '13610780204', '北京市朝阳区');
INSERT INTO `tb_student` VALUES ('BS0101002', '小科', '1', '1', '21', '男', '1300000000', '山西省长治市');
INSERT INTO `tb_student` VALUES ('BS0102001', '小科', '2', '1', '21', '男', '1300000000', '山西省长治市');
INSERT INTO `tb_student` VALUES ('BS0201001', '王子', '4', '2', '19', '男', '15500000000', '吉林省长春市');

-- ----------------------------
-- Table structure for `tb_user`
-- ----------------------------
DROP TABLE IF EXISTS `tb_user`;
CREATE TABLE `tb_user` (
  `userName` varchar(20) NOT NULL,
  `userPwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_user
-- ----------------------------
INSERT INTO `tb_user` VALUES ('mr', 'mrsoft');
INSERT INTO `tb_user` VALUES ('小科', '111');

-- ----------------------------
-- View structure for `v_classinfo`
-- ----------------------------
DROP VIEW IF EXISTS `v_classinfo`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_classinfo` AS select `tb_class`.`classID` AS `classID`,`tb_grade`.`gradeID` AS `gradeID`,`tb_grade`.`gradeName` AS `gradeName`,`tb_class`.`className` AS `className` from (`tb_class` join `tb_grade`) where (`tb_class`.`gradeID` = `tb_grade`.`gradeID`) ;

-- ----------------------------
-- View structure for `v_studentinfo`
-- ----------------------------
DROP VIEW IF EXISTS `v_studentinfo`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_studentinfo` AS select `tb_student`.`stuID` AS `stuID`,`tb_student`.`stuName` AS `stuName`,`tb_student`.`age` AS `age`,`tb_student`.`sex` AS `sex`,`tb_student`.`phone` AS `phone`,`tb_student`.`address` AS `address`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeName` AS `gradeName` from ((`tb_student` join `tb_class`) join `tb_grade`) where ((`tb_student`.`classID` = `tb_class`.`classID`) and (`tb_student`.`gradeID` = `tb_grade`.`gradeID`)) ;
