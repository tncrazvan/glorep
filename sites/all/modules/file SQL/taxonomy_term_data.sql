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
-- Table structure for table `taxonomy_term_data`
--

CREATE TABLE IF NOT EXISTS `taxonomy_term_data` (
  `tid` int(10) unsigned NOT NULL COMMENT 'Primary Key: Unique term ID.',
  `vid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT 'The taxonomy_vocabulary.vid of the vocabulary to which the term is assigned.',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT 'The term name.',
  `description` longtext COMMENT 'A description of the term.',
  `format` varchar(255) DEFAULT NULL COMMENT 'The filter_format.format of the description.',
  `weight` int(11) NOT NULL DEFAULT '0' COMMENT 'The weight of this term in relation to other terms.'
) ENGINE=InnoDB AUTO_INCREMENT=190 DEFAULT CHARSET=utf8 COMMENT='Stores term information.';

--
-- Dumping data for table `taxonomy_term_data`
--

INSERT INTO `taxonomy_term_data` (`tid`, `vid`, `name`, `description`, `format`, `weight`) VALUES
(81, 26, '540 - Chemistry & allied sciences', '', '', 0),
(82, 26, '541 - Physical Chemistry', '', '', 0),
(83, 26, '541.2 - Theoretical Chemistry', '', '', 0),
(84, 26, '541.3 - Miscellaneous Topics in Physical Chemistry', '', '', 0),
(85, 26, '541.33 - Surface Chemistry', '', '', 0),
(86, 26, '541.34 - Solutions Chemistry', '', '', 0),
(87, 26, '541.35 - Photochemistry', '', '', 0),
(88, 26, '541.36 - Thermochemistry & Thermodynamics', '', '', 0),
(89, 26, '541.37 - Electro Chemistry & Magneto Chemistry', '', '', 0),
(90, 26, '541.38 - Radio Chemistry (Nuclear Chemistry)', '', '', 0),
(91, 26, '541.39 - Chemical reactions', '', '', 0),
(92, 26, '541.7 - Optical Activity', '', '', 0),
(93, 26, '542 - Techniques, Procedures, Apparatus, Equipment & Materials', '', '', 0),
(94, 26, '542.1 - Laboratories', '', '', 0),
(95, 26, '542.2 - Containers and Accessory Equipment', '', '', 0),
(96, 26, '542.3 - Testing and Measuring', '', '', 0),
(97, 26, '542.4 - Heating and Distilling', '', '', 0),
(98, 26, '542.6 - Filtering and Dialysis', '', '', 0),
(99, 26, '542.7 - Gas Production, Processing, Measuring', '', '', 0),
(100, 26, '542.8 - Auxiliary Techniques and Procedures, Electrical and Electronic Equipment', '', '', 0),
(101, 26, '542.84 - Electrical Equipment', '', '', 0),
(102, 26, '542.85 - Chemistry Data Processing', '', '', 0),
(103, 26, '543 - Analytical chemistry', '', '', 0),
(104, 26, '543.1 - General Topics in Analytical Chemistry', '', '', 0),
(105, 26, '543.2 - Classical Methods', '', '', 0),
(106, 26, '543.4 - Electro Chemical Analysis', '', '', 0),
(107, 26, '543.5 - Optical Spectroscopy (Spectrum Analysis)', '', '', 0),
(108, 26, '543.6 - Non-Optical Spectroscopy', '', '', 0),
(109, 26, '543.8 - Chromatography', '', '', 0),
(110, 26, '546 - Inorganic Chemistry', '', '', 0),
(111, 26, '546.2 - Hydrogen and its Compounds', '', '', 0),
(112, 26, '546.3 - Metals, Metallic Compunds, Alloys', '', '', 0),
(113, 26, '546.4 - Group 3', '', '', 0),
(114, 26, '546.5 - Groups 4, 5, 6, 7', '', '', 0),
(115, 26, '546.6 - Groups 8, 9, 10, 11, 12, 13, 14', '', '', 0),
(116, 26, '546.7 - Groups 15, 16, 17, 18', '', '', 0),
(117, 26, '546.8 - Periodic Law and Periodic Table', '', '', 0),
(118, 26, '547 - Organic Chemistry', '', '', 0),
(119, 26, '547.2 - Organic Chemical Reactions', '', '', 0),
(120, 26, '547.1 - Physical And Theoretical Chemistry', '', '', 0),
(121, 26, '547.4 - Aliphatic Compounds', '', '', 0),
(122, 26, '547.5 - Cyclic Compounds', '', '', 0),
(123, 26, '547.6 - Aromatic Compounds', '', '', 0),
(124, 26, '547.7 - Macro-Molecules and Related Compounds', '', '', 0),
(125, 26, '547.8 - Other Organic Substances', '', '', 0),
(126, 26, '548 - Crystallography', '', '', 0),
(127, 26, '548.1 - Geometrical Crystallography', '', '', 0),
(128, 26, '548.3 - Chemical Crystallography', '', '', 0),
(129, 26, '548.5 - Crystallization and Crystal Growth', '', '', 0),
(130, 26, '548.7 - Mathematical Crystallography', '', '', 0),
(131, 26, '548.8 - Physical and Structural Crystallography', '', '', 0),
(132, 26, '548.9 - Optical Crystallography', '', '', 0),
(133, 26, '549 - Mineralogy', '', '', 0),
(134, 26, '549.1 - Determinative Mineralogy', '', '', 0),
(135, 26, '549.2 - Native Elements', '', '', 0),
(136, 26, '549.3 - Sulfides, Sulfosalts, Related Minerals', '', '', 0),
(137, 26, '549.4 - Halides', '', '', 0),
(138, 26, '549.5 - Oxides', '', '', 0),
(139, 26, '549.6 - Silicates', '', '', 0),
(140, 26, '549.7 - Other Minerals', '', '', 0),
(141, 27, '510 - Mathematics', '', '', 0),
(142, 27, '511 - General Principles of Mathematics', '', '', 0),
(143, 27, '511.3 - Mathematical Logic', '', '', 0),
(144, 27, '511.5 - Topics in Graph Theory', '', '', 0),
(145, 27, '511.6 - Combinatorial Analysis', '', '', 0),
(146, 27, '512 - Algebra', '', '', 0),
(147, 27, '512.2 - Groups and Group Theory', '', '', 0),
(148, 27, '512.3 - Algebraic Fields', '', '', 0),
(149, 27, '512.4 - Rings, Ideals', '', '', 0),
(150, 27, '512.5 - Linear Algebra', '', '', 0),
(151, 27, '512.6 - Category Thoery, Homological Algebra, K-Theory', '', '', 0),
(152, 27, '512.7 - Number Theory', '', '', 0),
(153, 27, '512.9 - Foundations of Algebra', '', '', 0),
(154, 27, '513 - Arithmetic', '', '', 0),
(155, 27, '513.2 - Arithmetic Operations', '', '', 0),
(156, 27, '513.5 - Numeration Systems', '', '', 0),
(157, 27, '514 - Topology', '', '', 0),
(158, 27, '514.2 - Algebraic Topology', '', '', 0),
(159, 27, '514.3 - Topology of Spaces', '', '', 0),
(160, 27, '514.7 - Analytic Topology', '', '', 0),
(161, 27, '515 - Analysis', '', '', 0),
(162, 27, '515.2 - General Aspects of Analysis', '', '', 0),
(163, 27, '515.3 - Differential Calculus and Equations', '', '', 0),
(164, 27, '515.4 - Integral Calculus and Equations', '', '', 0),
(165, 27, '515.5 - Special Functions', '', '', 0),
(166, 27, '515.7 - Functional Analysis', '', '', 0),
(167, 27, '515.8 - Functions of Real Variables', '', '', 0),
(168, 27, '515.9 - Functions of Complex Variables', '', '', 0),
(169, 27, '516 - Geometry', '', '', 0),
(170, 27, '516.2 - Euclidean Geometry', '', '', 0),
(171, 27, '516.3 - Analytic Geometries', '', '', 0),
(172, 27, '516.4 - Affine Geometry', '', '', 0),
(173, 27, '516.5 - Projective Geometry', '', '', 0),
(174, 27, '516.9 - Non-Euclidean Geometries', '', '', 0),
(175, 27, '518 - Numerical Analysis', '', '', 0),
(176, 27, '519 - Probabilities and Applied Mathematics', '', '', 0),
(177, 27, '519.2 - Probailities', '', '', 0),
(178, 27, '519.3 - Game Theory', '', '', 0),
(179, 27, '519.5 - Statistical Mathematics', '', '', 0),
(180, 27, '512.1 - Algebra combined with other branches of mathematics', '', '', 0),
(181, 27, '512.72 - Elementary Number Theory', '', '', 0),
(182, 27, '512.73 - Analytic number theory', '', '', 0),
(183, 27, '512.74 - Algebraic number theory', '', '', 0),
(184, 27, '515.72 - Operational calculus', '', '', 0),
(185, 27, '515.73 - Topological vector spaces', '', '', 0),
(186, 27, '515.78 - Special topics of functional analysis', '', '', 0),
(187, 27, '512.78 - Specific fields of numbers', '', '', 0),
(188, 27, '512.92 - Algebraic operations', '', '', 0),
(189, 27, '512.94 - Theory of equations', '', '', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `taxonomy_term_data`
--
ALTER TABLE `taxonomy_term_data`
  ADD PRIMARY KEY (`tid`),
  ADD KEY `taxonomy_tree` (`vid`,`weight`,`name`),
  ADD KEY `vid_name` (`vid`,`name`),
  ADD KEY `name` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `taxonomy_term_data`
--
ALTER TABLE `taxonomy_term_data`
  MODIFY `tid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary Key: Unique term ID.',AUTO_INCREMENT=190;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
