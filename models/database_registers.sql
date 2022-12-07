-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2022 at 12:46 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tttcontrol`
--

-- --------------------------------------------------------

--
-- Table structure for table `change_log`
--

CREATE TABLE `change_log` (
  `id` int(10) UNSIGNED NOT NULL,
  `gps_serial` int(10) UNSIGNED NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `type` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `previous_value` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `new_value` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Dumping data for table `change_log`
--

INSERT INTO `change_log` (`id`, `gps_serial`, `date`, `type`, `previous_value`, `new_value`) VALUES
(1, 121212, '2022-08-29 10:30:14', 'sample', '1', '2'),
(2, 123123, '2022-08-27 20:16:03', 'dvsdfg', '20', '10'),
(3, 121212, '2022-08-29 10:29:18', 'sample', '0', '1'),
(4, 121212, '2022-08-29 10:30:14', 'sample', '0', '1');

-- --------------------------------------------------------

--
-- Table structure for table `gps`
--

CREATE TABLE `gps` (
  `serial` int(10) UNSIGNED NOT NULL,
  `imei` int(11) NOT NULL,
  `description` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `software_version` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `firmware_version` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `comments` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `sim_telephone` int(10) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) UNSIGNED NOT NULL,
  `updated_by` int(10) UNSIGNED DEFAULT NULL,
  `deleted_by` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Dumping data for table `gps`
--

INSERT INTO `gps` (`serial`, `imei`, `description`, `software_version`, `firmware_version`, `status`, `comments`, `sim_telephone`, `created_at`, `updated_at`, `deleted_at`, `created_by`, `updated_by`, `deleted_by`) VALUES
(1, 121212, 'sample', '1', '1', 1, '213123', 987654321, '2022-08-27 20:08:12', '2022-08-27 20:08:12', NULL, 0, NULL, NULL),
(121212, 1, 'updated description', 'updated', 'updated', 1, 'updated comment', 12121212, '2022-08-29 09:38:20', '2022-08-29 09:41:59', NULL, 1, 1, NULL),
(123123, 1213, 'sample', '1', '1', 1, '213123', 987654321, '2022-08-27 20:08:12', '2022-08-27 20:08:12', NULL, 0, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `installation`
--

CREATE TABLE `installation` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `vehicle_description` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `economic_number` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `plate` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `gps_tag` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `fuse_status` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `installation_energy_type` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `ignition_control` tinyint(1) NOT NULL DEFAULT 0,
  `ignition_detection` tinyint(1) NOT NULL DEFAULT 0,
  `odometer` tinyint(1) NOT NULL DEFAULT 0,
  `extra_control` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_validator` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) UNSIGNED NOT NULL,
  `updated_by` int(10) UNSIGNED DEFAULT NULL,
  `deleted_by` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Dumping data for table `installation`
--

INSERT INTO `installation` (`id`, `user_id`, `date`, `vehicle_description`, `economic_number`, `plate`, `gps_tag`, `fuse_status`, `installation_energy_type`, `ignition_control`, `ignition_detection`, `odometer`, `extra_control`, `user_validator`, `created_at`, `updated_at`, `deleted_at`, `created_by`, `updated_by`, `deleted_by`) VALUES
(1, 1, '2022-08-29 09:32:55', 'updated description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-27 20:21:58', '2022-08-29 09:33:14', NULL, 1, 1, NULL),
(2, 1, '2022-08-27 20:22:04', 'sample 2', 'sample', 'sample', 'sample', 'sample', 'sample', 1, 1, 1, 'sample', 'sample', '2022-08-27 20:22:04', '2022-08-27 20:22:04', NULL, 1, NULL, NULL),
(3, 1, '2022-08-29 07:38:29', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 07:38:33', NULL, NULL, 1, NULL, NULL),
(4, 1, '2022-08-29 08:05:49', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 08:05:53', NULL, NULL, 1, NULL, NULL),
(5, 1, '2022-08-29 08:55:09', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 08:55:13', NULL, NULL, 1, NULL, NULL),
(6, 1, '2022-08-29 08:58:05', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 08:58:10', NULL, NULL, 1, NULL, NULL),
(7, 1, '2022-08-29 08:59:57', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 09:00:02', NULL, NULL, 1, NULL, NULL),
(8, 1, '2022-08-29 09:15:22', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 09:15:35', NULL, NULL, 1, NULL, NULL),
(9, 1, '2022-08-29 09:32:55', 'sample description', 'sample num', 'sample plate', 'sample tag', 'sample fus', 'sample', 1, 1, 1, 'sample extra', 'sample validation', '2022-08-29 09:33:08', NULL, NULL, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `maintenance`
--

CREATE TABLE `maintenance` (
  `id` int(10) UNSIGNED NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `economic_number` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `issue_description` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `gps_tag` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `fuse_status` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `installation_energy_type` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `installation_status` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `switch` enum('none','gps','sim') CHARACTER SET latin1 DEFAULT 'none',
  `new_tag` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_validator` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) UNSIGNED NOT NULL,
  `updated_by` int(10) UNSIGNED DEFAULT NULL,
  `deleted_by` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Dumping data for table `maintenance`
--

INSERT INTO `maintenance` (`id`, `date`, `economic_number`, `issue_description`, `gps_tag`, `fuse_status`, `installation_energy_type`, `installation_status`, `switch`, `new_tag`, `user_validator`, `user_id`, `created_at`, `updated_at`, `deleted_at`, `created_by`, `updated_by`, `deleted_by`) VALUES
(1, '2022-08-29 09:06:47', 'updated num', 'updated issue', 'updated ta', 'updated st', 'updated', 'updated', 'gps', 'updated ne', 'updated validator', 1, '2022-08-27 20:36:15', '2022-08-29 09:07:06', NULL, 1, 1, NULL),
(2, '2022-08-27 20:36:52', 'aesfsdf', 'sample 2', 'sample 2', 'sample 2', 'sample 2', 'sample 2', 'gps', 'sample 2', 'sample 2', 2, '2022-08-27 20:36:52', '2022-08-27 20:36:52', NULL, 1, NULL, NULL),
(3, '2022-08-29 05:01:43', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 05:01:48', NULL, NULL, 1, NULL, NULL),
(4, '2022-08-29 05:02:04', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 05:02:09', NULL, NULL, 1, NULL, NULL),
(5, '2022-08-29 05:10:56', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 05:11:08', NULL, NULL, 1, NULL, NULL),
(6, '2022-08-29 05:12:02', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 05:12:15', NULL, NULL, 1, NULL, NULL),
(7, '2022-08-29 05:28:59', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 05:29:11', NULL, NULL, 1, NULL, NULL),
(8, '2022-08-29 05:30:35', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 05:30:48', NULL, NULL, 1, NULL, NULL),
(9, '2022-08-29 07:04:21', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 07:04:33', NULL, NULL, 1, NULL, NULL),
(10, '2022-08-29 09:05:52', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 09:06:05', NULL, NULL, 1, NULL, NULL),
(11, '2022-08-29 09:06:47', 'sample num', 'sample issue', 'sample tag', 'sample sta', 'sample', 'sample', 'gps', 'sample new', 'sample validator', 1, '2022-08-29 09:07:00', NULL, NULL, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `sim`
--

CREATE TABLE `sim` (
  `telephone` int(10) UNSIGNED NOT NULL,
  `account` varchar(15) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `father_account` varchar(15) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `iccid` varchar(25) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `package` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `cancellation_date` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) UNSIGNED NOT NULL,
  `updated_by` int(10) UNSIGNED DEFAULT NULL,
  `deleted_by` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Dumping data for table `sim`
--

INSERT INTO `sim` (`telephone`, `account`, `father_account`, `iccid`, `package`, `status`, `cancellation_date`, `created_at`, `updated_at`, `deleted_at`, `created_by`, `updated_by`, `deleted_by`) VALUES
(12121212, 'updated sample', 'sample father', '000001', 'sample package', 1, '2022-08-29 05:22:28', '2022-08-28 22:21:03', '2022-08-29 05:22:47', NULL, 1, 1, NULL),
(123456789, '12123', '1232', '1231231221', '123123123', 1, NULL, '2022-08-27 19:46:54', '2022-08-28 22:10:12', NULL, 1, NULL, NULL),
(987654321, '12123', '1232', '1231231221', '123123123', 1, NULL, '2022-08-27 19:47:05', '2022-08-27 19:49:28', NULL, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `login` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_type` tinyint(1) NOT NULL DEFAULT 1,
  `status` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) UNSIGNED NOT NULL,
  `updated_by` int(10) UNSIGNED DEFAULT NULL,
  `deleted_by` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `login`, `password`, `user_type`, `status`, `created_at`, `updated_at`, `deleted_at`, `created_by`, `updated_by`, `deleted_by`) VALUES
(1, 'name updated', 'login updated', 'updatedpass123**', 1, 1, '2022-08-27 18:55:00', '2022-08-28 22:01:10', NULL, 1, 1, NULL),
(2, 'sample2', 'sample2', '12121212', 1, 1, '2022-08-27 18:55:12', '2022-08-27 18:55:12', NULL, 1, 1, NULL),
(4, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 20:45:24', NULL, NULL, 1, NULL, NULL),
(5, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 20:45:47', NULL, NULL, 1, NULL, NULL),
(6, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 20:46:20', NULL, NULL, 1, NULL, NULL),
(7, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 20:55:00', NULL, NULL, 1, NULL, NULL),
(8, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 22:03:07', NULL, NULL, 1, NULL, NULL),
(9, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 22:38:42', NULL, NULL, 1, NULL, NULL),
(10, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 22:39:41', NULL, NULL, 1, NULL, NULL),
(11, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-28 22:40:52', NULL, NULL, 1, NULL, NULL),
(12, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-29 04:38:28', NULL, NULL, 1, NULL, NULL),
(13, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-29 05:20:43', NULL, NULL, 1, NULL, NULL),
(14, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-29 07:02:48', NULL, NULL, 1, NULL, NULL),
(15, 'sample name', 'sample login', 'samplepass123**', 1, 1, '2022-08-29 09:01:34', NULL, NULL, 1, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `change_log`
--
ALTER TABLE `change_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `gps_serial` (`gps_serial`);

--
-- Indexes for table `gps`
--
ALTER TABLE `gps`
  ADD PRIMARY KEY (`serial`),
  ADD UNIQUE KEY `imei` (`imei`),
  ADD KEY `sim_telephone` (`sim_telephone`);

--
-- Indexes for table `installation`
--
ALTER TABLE `installation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `maintenance`
--
ALTER TABLE `maintenance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `sim`
--
ALTER TABLE `sim`
  ADD PRIMARY KEY (`telephone`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `change_log`
--
ALTER TABLE `change_log`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `installation`
--
ALTER TABLE `installation`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `maintenance`
--
ALTER TABLE `maintenance`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `change_log`
--
ALTER TABLE `change_log`
  ADD CONSTRAINT `change_log_ibfk_1` FOREIGN KEY (`gps_serial`) REFERENCES `gps` (`serial`);

--
-- Constraints for table `gps`
--
ALTER TABLE `gps`
  ADD CONSTRAINT `gps_ibfk_1` FOREIGN KEY (`sim_telephone`) REFERENCES `sim` (`telephone`);

--
-- Constraints for table `installation`
--
ALTER TABLE `installation`
  ADD CONSTRAINT `installation_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `maintenance`
--
ALTER TABLE `maintenance`
  ADD CONSTRAINT `maintenance_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
