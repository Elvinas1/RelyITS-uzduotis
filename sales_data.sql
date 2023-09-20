-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 20, 2023 at 08:26 PM
-- Server version: 8.1.0
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sales_data`
--
CREATE DATABASE IF NOT EXISTS `sales_data` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `sales_data`;

-- --------------------------------------------------------

--
-- Table structure for table `sales_records`
--

DROP TABLE IF EXISTS `sales_records`;
CREATE TABLE IF NOT EXISTS `sales_records` (
  `id` int NOT NULL AUTO_INCREMENT,
  `transaction_date` date DEFAULT NULL,
  `store_id` varchar(255) DEFAULT NULL,
  `total_items` int DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `total_receipts` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sales_records`
--

INSERT INTO `sales_records` (`id`, `transaction_date`, `store_id`, `total_items`, `total_amount`, `total_receipts`) VALUES
(1, '2019-07-22', '3004', 1, '22041.88', 1),
(2, '2019-07-22', '3004', 1, '196.89', 1),
(3, '2019-07-22', '3000', 1, '384.15', 1),
(4, '2019-07-22', '3000', 1, NULL, NULL),
(5, '2019-07-22', '3000', 1, '79.00', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
