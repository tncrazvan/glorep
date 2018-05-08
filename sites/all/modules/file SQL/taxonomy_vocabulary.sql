-- phpMyAdmin SQL Dump
-- version 4.4.13.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 13, 2016 at 12:26 PM
-- Server version: 5.6.30-0ubuntu0.15.10.1
-- PHP Version: 5.6.11-1ubuntu3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `glorep2`
--

-- --------------------------------------------------------

--
-- Table structure for table `taxonomy_vocabulary`
--

CREATE TABLE IF NOT EXISTS `taxonomy_vocabulary` (
  `vid` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `machine_name` varchar(255) NOT NULL,
  `description` longtext,
  `hierarchy` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `module` varchar(255) NOT NULL,
  `weight` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `taxonomy_vocabulary`
--

INSERT INTO `taxonomy_vocabulary` (`vid`, `name`, `machine_name`, `description`, `hierarchy`, `module`, `weight`) VALUES
(26, 'Chemistry & allied sciences', 'chemistry_&_allied_sciences', '', 1, 'taxonomy', 0),
(27, 'Mathematics', 'mathematics', '', 1, 'taxonomy', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `taxonomy_vocabulary`
--
ALTER TABLE `taxonomy_vocabulary`
  ADD PRIMARY KEY (`vid`),
  ADD KEY `list` (`weight`,`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `taxonomy_vocabulary`
--
ALTER TABLE `taxonomy_vocabulary`
  MODIFY `vid` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=28;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
