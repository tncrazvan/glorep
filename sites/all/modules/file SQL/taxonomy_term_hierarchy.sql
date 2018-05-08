-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 24, 2016 at 12:51 AM
-- Server version: 5.7.13-0ubuntu0.16.04.2
-- PHP Version: 7.0.8-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `drupal2`
--

-- --------------------------------------------------------

--
-- Table structure for table `taxonomy_term_hierarchy`
--

CREATE TABLE `taxonomy_term_hierarchy` (
  `tid` int(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT 'Primary Key: The taxonomy_term_data.tid of the term.',
  `parent` int(10) UNSIGNED NOT NULL DEFAULT '0' COMMENT 'Primary Key: The taxonomy_term_data.tid of the term’s parent. 0 indicates no parent.'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Stores the hierarchical relationship between terms.';

--
-- Dumping data for table `taxonomy_term_hierarchy`
--

INSERT INTO `taxonomy_term_hierarchy` (`tid`, `parent`) VALUES
(81, 0),
(141, 0),
(82, 81),
(93, 81),
(103, 81),
(110, 81),
(118, 81),
(126, 81),
(133, 81),
(191, 81),
(83, 82),
(84, 82),
(92, 82),
(85, 84),
(86, 84),
(87, 84),
(88, 84),
(89, 84),
(90, 84),
(91, 84),
(94, 93),
(95, 93),
(96, 93),
(97, 93),
(98, 93),
(99, 93),
(100, 93),
(101, 100),
(102, 100),
(104, 103),
(105, 103),
(106, 103),
(107, 103),
(108, 103),
(109, 103),
(111, 110),
(112, 110),
(113, 110),
(114, 110),
(115, 110),
(116, 110),
(117, 110),
(119, 118),
(120, 118),
(121, 118),
(122, 118),
(123, 118),
(124, 118),
(125, 118),
(127, 126),
(128, 126),
(129, 126),
(130, 126),
(131, 126),
(132, 126),
(134, 133),
(135, 133),
(136, 133),
(137, 133),
(138, 133),
(139, 133),
(140, 133),
(142, 141),
(146, 141),
(154, 141),
(157, 141),
(161, 141),
(169, 141),
(175, 141),
(176, 141),
(143, 142),
(144, 142),
(145, 142),
(147, 146),
(148, 146),
(149, 146),
(150, 146),
(151, 146),
(152, 146),
(153, 146),
(180, 146),
(181, 152),
(182, 152),
(183, 152),
(187, 152),
(188, 153),
(189, 153),
(155, 154),
(156, 154),
(158, 157),
(159, 157),
(160, 157),
(162, 161),
(163, 161),
(164, 161),
(165, 161),
(166, 161),
(167, 161),
(168, 161),
(184, 166),
(185, 166),
(186, 166),
(170, 169),
(171, 169),
(172, 169),
(173, 169),
(174, 169),
(177, 176),
(178, 176),
(179, 176);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `taxonomy_term_hierarchy`
--
ALTER TABLE `taxonomy_term_hierarchy`
  ADD PRIMARY KEY (`tid`,`parent`),
  ADD KEY `parent` (`parent`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
