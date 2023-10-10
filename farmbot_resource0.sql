-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: farmbot
-- ------------------------------------------------------
-- Server version	8.0.33
USE farmbot;
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `resource`
--

DROP TABLE IF EXISTS `resource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resource` (
  `idresource` int NOT NULL,
  `electricityUsed` float NOT NULL,
  `waterUsed` float NOT NULL,
  `fertiliserused` float NOT NULL,
  `date` datetime NOT NULL,
  `landid` int NOT NULL,
  `humidity` float NOT NULL,
  `temp` float NOT NULL,
  PRIMARY KEY (`idresource`,`landid`),
  KEY `gardenid_idx` (`landid`),
  CONSTRAINT `gardenid` FOREIGN KEY (`landid`) REFERENCES `garden` (`idgarden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource`
--

LOCK TABLES `resource` WRITE;
/*!40000 ALTER TABLE `resource` DISABLE KEYS */;
INSERT INTO `resource` VALUES (1,3,345,0,'2023-09-11 00:00:00',1,25,25),(2,4,0,0,'2023-09-10 00:00:00',1,30,30),(3,0,265,0,'2023-09-09 00:00:00',1,30,27),(4,4,0,0,'2023-09-08 00:00:00',1,35,29),(5,2,367,0,'2023-09-07 00:00:00',1,30,23),(6,0,0,0,'2023-09-06 00:00:00',1,32,20),(7,2,532,50,'2023-09-05 00:00:00',1,30,27),(8,0,0,0,'2023-09-04 00:00:00',1,35,30),(9,0,0,0,'2023-09-03 00:00:00',1,33,34),(10,1,534,0,'2023-09-02 00:00:00',1,30,38),(11,2,753,0,'2023-09-01 00:00:00',1,35,35);
/*!40000 ALTER TABLE `resource` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-10 16:34:10
