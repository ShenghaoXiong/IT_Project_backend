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
-- Table structure for table `plants`
--

DROP TABLE IF EXISTS `plants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plants` (
  `idPlants` int NOT NULL,
  `idGarden` int NOT NULL,
  `plantsName` varchar(45) NOT NULL,
  `binomialName` varchar(45) NOT NULL,
  `plantDay` int NOT NULL,
  `plantXpoint` float NOT NULL,
  `plantYpoint` float NOT NULL,
  `radius` float NOT NULL,
  `lastWatering` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idPlants`),
  KEY `idGarden_idx` (`idGarden`),
  CONSTRAINT `idGarden` FOREIGN KEY (`idGarden`) REFERENCES `garden` (`idgarden`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plants`
--

LOCK TABLES `plants` WRITE;
/*!40000 ALTER TABLE `plants` DISABLE KEYS */;
INSERT INTO `plants` VALUES (1,1,'Potato','Solanum tuberosum',2,200,200,50,'2023-09-07 00:00:00','russet-potato-24px.png'),(2,1,'Tomato','Solanum lycopersicum',30,800,100,100,'2023-09-11 00:00:00','tomato-24px.png'),(3,1,'Cabbages','Brassica oleracea',50,800,600,200,'2023-09-07 00:00:00','green-cabbage-24px.png'),(4,1,'Cayenne Pepper','Capsicum annuum',10,300,700,450,'2023-09-05 00:00:00','cayenne-pepper-24px'),(5,1,'Cherry','Prunus avium',10,1800,300,350,'2023-09-09 00:00:00','bing-cherry-24px'),(6,1,'Van Zerden Garlic','Allium sativum',15,1200,100,100,'2023-09-02 00:00:00','garlic-24px.png'),(7,1,'Van Zerden Garlic','Allium sativum',15,1100,100,100,'2023-09-02 00:00:00','garlic-24px.png'),(8,1,'Shishito Pepper','Capsicum annuum',20,1800,500,200,'2023-09-09 00:00:00','shishito-pepper-24px'),(9,1,'Corn','Zea mays',20,1300,700,300,'2023-09-11 00:00:00','corn-24px.png'),(10,2,'Datil Pepper','Capsicum chinense',13,200,200,100,'2023-09-07 00:00:00','datil-pepper-24px.png'),(11,2,'Datil Pepper','Capsicum chinense',13,200,500,100,'2023-09-07 00:00:00','datil-pepper-24px.png'),(12,2,'Datil Pepper','Capsicum chinense',13,200,800,100,'2023-09-07 00:00:00','datil-pepper-24px.png'),(13,2,'Datil Pepper','Capsicum chinense',13,500,200,100,'2023-09-07 00:00:00','datil-pepper-24px.png'),(14,2,'Datil Pepper','Capsicum chinense',13,500,500,100,'2023-09-07 00:00:00','datil-pepper-24px.png'),(15,2,'Datil Pepper','Capsicum chinense',13,500,800,100,'2023-09-07 00:00:00','datil-pepper-24px.png'),(16,2,'Chili Pepper','Capsicum',15,800,200,100,'2023-09-09 00:00:00','birds-eye-chili-24px.png'),(17,2,'Chili Pepper','Capsicum',15,800,500,100,'2023-09-09 00:00:00','birds-eye-chili-24px.png'),(18,2,'Chili Pepper','Capsicum',15,800,800,100,'2023-09-09 00:00:00','birds-eye-chili-24px.png'),(19,2,'Chili Pepper','Capsicum',15,1100,200,100,'2023-09-09 00:00:00','birds-eye-chili-24px.png'),(20,2,'Chili Pepper','Capsicum',15,1100,500,100,'2023-09-09 00:00:00','birds-eye-chili-24px.png'),(21,2,'Chili Pepper','Capsicum',15,100,800,100,'2023-09-09 00:00:00','birds-eye-chili-24px.png'),(22,2,'Carrot','Daucus Carota',11,1300,100,25,'2023-09-11 00:00:00','carrot-24px.png'),(23,2,'Carrot','Daucus Carota',11,1400,100,25,'2023-09-11 00:00:00','carrot-24px.png'),(24,2,'Carrot','Daucus Carota',11,1200,300,25,'2023-09-11 00:00:00','carrot-24px.png'),(25,2,'Carrot','Daucus Carota',11,1300,300,25,'2023-09-11 00:00:00','carrot-24px.png'),(26,2,'Eggplant','Solanum melongena',8,1700,200,150,'2023-09-11 00:00:00','eggplant-24px.png'),(27,2,'Eggplant','Solanum melongena',8,1700,500,150,'2023-09-11 00:00:00','eggplant-24px.png');
/*!40000 ALTER TABLE `plants` ENABLE KEYS */;
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
