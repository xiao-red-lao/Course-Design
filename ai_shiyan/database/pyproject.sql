/*
 Navicat Premium Data Transfer

 Source Server         : database16
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : pyproject

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 17/08/2020 15:04:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int(50) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `cla` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` int(100) NOT NULL,
  `address` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students
-- ----------------------------
INSERT INTO `students` VALUES (96047,'麦子',22,'男',"信科1班",123456,"湛江");
INSERT INTO `students` VALUES (12811,'张三',24,'女',"计科5班",6129852,"广州");
INSERT INTO `students` VALUES (12947,'李四',24,'男',"网络3班",6829852,"北京");
INSERT INTO `students` VALUES (91724,'王五',19,'男',"信科2班",148756,"深圳");
INSERT INTO `students` VALUES (12792,'张一山',23,'男',"计科5班",6289852,"广州");
INSERT INTO `students` VALUES (24802,'刘大姐',24,'女',"网络3班",6826752,"北京");
INSERT INTO `students` VALUES (91200,'娃哈哈',22,'女',"信科1班",175456,"广州");
INSERT INTO `students` VALUES (92749,'廖一一',22,'女',"计科5班",2479852,"广州");
INSERT INTO `students` VALUES (94242,'李二牛',24,'男',"网络3班",6746852,"北京");
INSERT INTO `students` VALUES (27288,'陈浩南',19,'男',"信科2班",128886,"香港");
INSERT INTO `students` VALUES (26422,'吴亦凡',23,'男',"计科5班",567852,"广州");
INSERT INTO `students` VALUES (29422,'迪丽热巴',24,'女',"信科1班",6898052,"北京");

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` int(11) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (001,"信科1班",56);
INSERT INTO `class` VALUES (002,"电气5班",61);
INSERT INTO `class` VALUES (003,"汽车9班",68);
INSERT INTO `class` VALUES (004,"信科2班",48);

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `id` int(50) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `C` int(50) DEFAULT NULL,
  `java` int(50) DEFAULT NULL,
  `python` int(50) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES (96047,'麦子',90,80,70);
INSERT INTO `grade` VALUES (12811,'张三',57,84,43);
INSERT INTO `grade` VALUES (12947,'李四',67,32,99);
INSERT INTO `grade` VALUES (91724,'王五',84,74,84);
INSERT INTO `grade` VALUES (24802,'刘大姐',67,65,78);
INSERT INTO `grade` VALUES (91200,'娃哈哈',65,68,90);
INSERT INTO `grade` VALUES (92749,'廖一一',78,78,69);
INSERT INTO `grade` VALUES (94242,'李二牛',78,99,87);
INSERT INTO `grade` VALUES (27288,'陈浩南',67,68,54);
INSERT INTO `grade` VALUES (26422,'吴亦凡',67,89,87);
INSERT INTO `grade` VALUES (29422,'迪丽热巴',67,89,56);

