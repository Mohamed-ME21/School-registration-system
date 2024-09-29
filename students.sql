-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2024 at 05:01 PM
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
-- Database: `stud`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `ID Student` int(11) NOT NULL,
  `Name Student` varchar(100) NOT NULL,
  `E-Mail` varchar(100) NOT NULL,
  `Phone Student` varchar(100) NOT NULL,
  `Qualification` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`ID Student`, `Name Student`, `E-Mail`, `Phone Student`, `Qualification`, `Gender`, `Address`) VALUES
(1, 'Mohamed', 'meid15067@gmail.com', '1116455176', 'Very Good', 'Male', 'Giza'),
(2, 'Ahmed', 'ahmed15067@gmail.com', '1116485176', 'Very Good', 'Male', 'Giza'),
(4, 'Yossef', 'yossef1457@gmail.com', '102248654', 'Good', 'Male', 'Cairo'),
(5, 'Naglaa', 'naglaa2514@yahoo.com', '124952', 'Excellent', 'Femal', 'ALX'),
(6, 'Heba', 'heba1482@gmaail.com', '10214975', 'Very Good', 'Femal', 'ALX'),
(7, 'Mostafa', 'most1425@gmail.com', '12149745', 'Good', 'Male', 'Cairo'),
(8, 'Salsabil', 'sal478@gmail.com', '102345975', 'Excellent', 'Femal', 'Cairo'),
(9, 'Khaled', 'khaled148@gmail.com', '1244681', 'week', 'Male', 'Fayom'),
(10, 'Shams', 'shams258@gmail.com', '112365478', 'Excellent', 'Femal', 'ALX');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`ID Student`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
