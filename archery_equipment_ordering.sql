-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 03:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `archery_equipment_ordering`
--

-- --------------------------------------------------------

--
-- Table structure for table `archery_ordering`
--

CREATE TABLE `archery_ordering` (
  `name_label` text NOT NULL,
  `Phonenumber_label` int(13) NOT NULL,
  `email_label` varchar(50) NOT NULL,
  `Address_label` varchar(50) NOT NULL,
  `district_label` text NOT NULL,
  `Paymentmethod_label` text NOT NULL,
  `selected_items` varchar(50) NOT NULL,
  `total_price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `archery_ordering`
--

INSERT INTO `archery_ordering` (`name_label`, `Phonenumber_label`, `email_label`, `Address_label`, `district_label`, `Paymentmethod_label`, `selected_items`, `total_price`) VALUES
('Kaizer', 123456789, 'kaizer@gmail.com', 'Tempoyang', 'Lipis', 'Payment in store', '[\'bow 35lbs- rm250\', \'Arrow 500spine- rm20\']', 270),
('Hanifmuhammad hanif aiman bin kamaruzaman ', 1121955708, 'hanifaiman2004@gmail.com', 'kuala berang, terengganu', 'Kuantan', 'Cash on delivery', '[\'bow 25lbs- rm150\', \'bow 30lbs- rm200\', \'bow 35lb', 1040),
(' Irfan Mustaqim', 139578070, 'Irfan45@gmail.com', 'Kg Berchang', 'Lipis', 'Cash on delivery', '[\'bow 35lbs- rm250\', \'Arrow 500spine- rm20\']', 270),
(' Irfan Mustaqim', 139578070, '', 'Kg Berchang', 'Lipis', 'Cash on delivery', '[]', 0),
(' Irfan Mustaqim', 139578070, '', 'Kg Berchang', 'Lipis', 'Cash on delivery', '[]', 0),
(' Irfan Mustaqim', 139578070, 'irfan45@gmail.com', 'Kg Berchang', 'Lipis', 'Cash on delivery', '[\'bow 30lbs- rm200\', \'Arrow 600spine- rm30\']', 230);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
