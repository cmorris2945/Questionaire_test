-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 27, 2024 at 01:09 AM
-- Server version: 10.2.44-MariaDB-cll-lve
-- PHP Version: 8.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drbot_health_final`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact_form`
--

CREATE TABLE `contact_form` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` varchar(200) NOT NULL,
  `created_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact_form`
--

INSERT INTO `contact_form` (`id`, `email`, `message`, `created_date`) VALUES
(1, 'phlksmcwrOa@superstomatologpro.ru', 'Ð›Ð°Ð¹Ð½ÐµÑ€Ñ‹ Ð´Ð»Ñ Ð·ÑƒÐ±Ð¾Ð² <a href=aligner-price.ru>aligner-price.ru</a> . \r\n', '2024-04-23'),
(2, 'saniya.chat360@gmail.com', 'test data contact form tech team', '2024-06-19'),
(3, 'test@gmail.com', 'test data', '2024-06-20'),
(4, 'pratik_p@gmail.com', 'test data', '2024-06-20');

-- --------------------------------------------------------

--
-- Table structure for table `inquiry_within`
--

CREATE TABLE `inquiry_within` (
  `id` int(11) NOT NULL,
  `enq_id` varchar(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile_number` varchar(12) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `relation` varchar(255) DEFAULT NULL,
  `diagnosis` varchar(255) DEFAULT NULL,
  `specify_location_of_cancer` varchar(500) NOT NULL,
  `testing` varchar(3) DEFAULT NULL,
  `tests` varchar(255) DEFAULT NULL,
  `insurance` varchar(5) NOT NULL,
  `opinion` text DEFAULT NULL,
  `noOpinionReason` text DEFAULT NULL,
  `interested` varchar(3) DEFAULT NULL,
  `discussion` text DEFAULT NULL,
  `remark` mediumtext NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `subsribe`
--

CREATE TABLE `subsribe` (
  `id` int(11) NOT NULL,
  `email_subscribe` varchar(200) NOT NULL,
  `created_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subsribe`
--

INSERT INTO `subsribe` (`id`, `email_subscribe`, `created_date`) VALUES
(1, 'MikeH@SoCPAnow.com', '2024-06-13'),
(2, 'nicholewowens@yahoo.com', '2024-06-14'),
(3, 'kanua1@icloud.com', '2024-06-17'),
(4, 'chandrakant@gmail.com', '2024-06-18'),
(5, 'punitakhanna1@gmail.com', '2024-06-18'),
(6, 'kanua1@icloud.com', '2024-06-19'),
(7, 'testingdrbot@gmail.com', '2024-06-19'),
(8, 'hitendra@gmail.com', '2024-06-19'),
(10, 'admin@autovista.in', '2024-06-19'),
(11, 's@gmaail.com', '2024-06-19'),
(12, 'info@sumanel.com', '2024-06-19'),
(13, 'admin@autovista.in', '2024-06-19'),
(14, 'testingdrbot@gmailcom', '2024-06-19'),
(15, 'saniyapathan296@gmail.com', '2024-06-19');

-- --------------------------------------------------------

--
-- Table structure for table `visitor_counter`
--

CREATE TABLE `visitor_counter` (
  `id` int(11) NOT NULL,
  `visitor_counter` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `visitor_counter`
--

INSERT INTO `visitor_counter` (`id`, `visitor_counter`) VALUES
(1, 5085);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact_form`
--
ALTER TABLE `contact_form`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `inquiry_within`
--
ALTER TABLE `inquiry_within`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `subsribe`
--
ALTER TABLE `subsribe`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `visitor_counter`
--
ALTER TABLE `visitor_counter`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact_form`
--
ALTER TABLE `contact_form`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `inquiry_within`
--
ALTER TABLE `inquiry_within`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `subsribe`
--
ALTER TABLE `subsribe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `visitor_counter`
--
ALTER TABLE `visitor_counter`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
