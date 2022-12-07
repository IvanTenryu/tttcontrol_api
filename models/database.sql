--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255)  COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `login` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_type`  tinyint(1) NOT NULL DEFAULT "1",
  `status`  tinyint(1) NOT NULL DEFAULT "1",
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) unsigned NOT NULL,
  `updated_by` int(10) unsigned DEFAULT NULL,
  `deleted_by` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Table structure for table `sim`
--

CREATE TABLE `sim`(
  `telephone` int(10) unsigned NOT NULL,
  `account` varchar(15)  COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `father_account` varchar(15) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `iccid` varchar(25) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `package` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `status`  tinyint(1) NOT NULL DEFAULT "1",
  `cancellation_date` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) unsigned NOT NULL,
  `updated_by` int(10) unsigned DEFAULT NULL,
  `deleted_by` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`telephone`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


--
-- Table structure for table `gps`
--

CREATE TABLE `gps`(
  `serial` int(10) unsigned NOT NULL,
  `imei` int NOT NULL UNIQUE,
  `description` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `software_version` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `firmware_version` varchar(100) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `status`  tinyint(1) NOT NULL DEFAULT "1",
  `comments` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `sim_telephone` int(10) unsigned ,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) unsigned NOT NULL,
  `updated_by` int(10) unsigned DEFAULT NULL,
  `deleted_by` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`serial`),
  FOREIGN KEY (sim_telephone) REFERENCES sim(telephone)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;


--
-- Table structure for table `change_log`
--
CREATE TABLE `change_log`(
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `gps_serial` int(10) unsigned NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `type` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `previous_value` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `new_value` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  primary key(id),
  FOREIGN KEY (gps_serial) REFERENCES gps(serial)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Table structure for table `installation`
--
CREATE TABLE `installation`(
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `vehicle_description` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `economic_number` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `plate` varchar(20) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `gps_tag` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `fuse_status` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `installation_energy_type` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `ignition_control` tinyint(1) NOT NULL DEFAULT "0",
  `ignition_detection` tinyint(1) NOT NULL DEFAULT "0",
  `odometer` tinyint(1) NOT NULL DEFAULT "0",
  `extra_control` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_validator` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) unsigned NOT NULL,
  `updated_by` int(10) unsigned DEFAULT NULL,
  `deleted_by` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY(`id`),
  FOREIGN KEY (`user_id`) REFERENCES user(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;



--
-- Table structure for table `maintainance`
--
CREATE TABLE `maintenance`(
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `economic_number` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `issue_description` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `gps_tag` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `fuse_status` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `installation_energy_type` varchar(50) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `installation_status` varchar(255) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `switch` enum("none","gps","sim") CHARACTER SET latin1 DEFAULT "none",
  `new_tag` varchar(10) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_validator` varchar(30) COLLATE utf8mb4_spanish_ci DEFAULT NULL,
  `user_id` int(10) unsigned NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_by` int(10) unsigned NOT NULL,
  `updated_by` int(10) unsigned DEFAULT NULL,
  `deleted_by` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY (user_id) REFERENCES user(id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;