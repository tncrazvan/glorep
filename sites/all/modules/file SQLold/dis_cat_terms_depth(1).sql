-- phpMyAdmin SQL Dump
-- version 4.4.13.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 13, 2016 at 01:24 PM
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
-- Table structure for table `dis_cat_terms_depth`
--

CREATE TABLE IF NOT EXISTS `dis_cat_terms_depth` (
  `tid` int(11) NOT NULL,
  `depth` int(11) NOT NULL,
  `vid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dis_cat_terms_depth`
--

INSERT INTO `dis_cat_terms_depth` (`tid`, `depth`, `vid`) VALUES
(81, 0, 26),
(82, 1, 26),
(83, 2, 26),
(84, 2, 26),
(85, 3, 26),
(86, 3, 26),
(87, 3, 26),
(88, 3, 26),
(89, 3, 26),
(90, 3, 26),
(91, 3, 26),
(92, 2, 26),
(93, 1, 26),
(94, 2, 26),
(95, 2, 26),
(96, 2, 26),
(97, 2, 26),
(98, 2, 26),
(99, 2, 26),
(100, 2, 26),
(101, 3, 26),
(102, 3, 26),
(103, 1, 26),
(104, 2, 26),
(105, 2, 26),
(106, 2, 26),
(107, 2, 26),
(108, 2, 26),
(109, 2, 26),
(110, 1, 26),
(111, 2, 26),
(112, 2, 26),
(113, 2, 26),
(114, 2, 26),
(115, 2, 26),
(116, 2, 26),
(117, 2, 26),
(118, 1, 26),
(119, 2, 26),
(120, 2, 26),
(121, 2, 26),
(122, 2, 26),
(123, 2, 26),
(124, 2, 26),
(125, 2, 26),
(126, 1, 26),
(127, 2, 26),
(128, 2, 26),
(129, 2, 26),
(130, 2, 26),
(131, 2, 26),
(132, 2, 26),
(133, 1, 26),
(134, 2, 26),
(135, 2, 26),
(136, 2, 26),
(137, 2, 26),
(138, 2, 26),
(139, 2, 26),
(140, 2, 26),
(141, 0, 27),
(142, 1, 27),
(143, 2, 27),
(144, 2, 27),
(145, 2, 27),
(146, 1, 27),
(147, 2, 27),
(148, 2, 27),
(149, 2, 27),
(150, 2, 27),
(151, 2, 27),
(152, 2, 27),
(153, 2, 27),
(154, 1, 27),
(155, 2, 27),
(156, 2, 27),
(157, 1, 27),
(158, 2, 27),
(159, 2, 27),
(160, 2, 27),
(161, 1, 27),
(162, 2, 27),
(163, 2, 27),
(164, 2, 27),
(165, 2, 27),
(166, 2, 27),
(167, 2, 27),
(168, 2, 27),
(169, 1, 27),
(170, 2, 27),
(171, 2, 27),
(172, 2, 27),
(173, 2, 27),
(174, 2, 27),
(175, 1, 27),
(176, 1, 27),
(177, 2, 27),
(178, 2, 27),
(179, 2, 27),
(180, 2, 27),
(181, 3, 27),
(182, 3, 27),
(183, 3, 27),
(184, 3, 27),
(185, 3, 27),
(186, 3, 27),
(187, 3, 27),
(188, 3, 27),
(189, 3, 27),
(191, 1, 26);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dis_cat_terms_depth`
--
ALTER TABLE `dis_cat_terms_depth`
  ADD PRIMARY KEY (`tid`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
