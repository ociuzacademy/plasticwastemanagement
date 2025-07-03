-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 16, 2021 at 06:43 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_plastic`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add cart_tb', 1, 'add_cart_tb'),
(2, 'Can change cart_tb', 1, 'change_cart_tb'),
(3, 'Can delete cart_tb', 1, 'delete_cart_tb'),
(4, 'Can view cart_tb', 1, 'view_cart_tb'),
(5, 'Can add register_tb', 2, 'add_register_tb'),
(6, 'Can change register_tb', 2, 'change_register_tb'),
(7, 'Can delete register_tb', 2, 'delete_register_tb'),
(8, 'Can view register_tb', 2, 'view_register_tb'),
(9, 'Can add unit_register_tb', 3, 'add_unit_register_tb'),
(10, 'Can change unit_register_tb', 3, 'change_unit_register_tb'),
(11, 'Can delete unit_register_tb', 3, 'delete_unit_register_tb'),
(12, 'Can view unit_register_tb', 3, 'view_unit_register_tb'),
(13, 'Can add workers_register_tb', 4, 'add_workers_register_tb'),
(14, 'Can change workers_register_tb', 4, 'change_workers_register_tb'),
(15, 'Can delete workers_register_tb', 4, 'delete_workers_register_tb'),
(16, 'Can view workers_register_tb', 4, 'view_workers_register_tb'),
(17, 'Can add waste_location_tb', 5, 'add_waste_location_tb'),
(18, 'Can change waste_location_tb', 5, 'change_waste_location_tb'),
(19, 'Can delete waste_location_tb', 5, 'delete_waste_location_tb'),
(20, 'Can view waste_location_tb', 5, 'view_waste_location_tb'),
(21, 'Can add product_tb', 6, 'add_product_tb'),
(22, 'Can change product_tb', 6, 'change_product_tb'),
(23, 'Can delete product_tb', 6, 'delete_product_tb'),
(24, 'Can view product_tb', 6, 'view_product_tb'),
(25, 'Can add order_tb', 7, 'add_order_tb'),
(26, 'Can change order_tb', 7, 'change_order_tb'),
(27, 'Can delete order_tb', 7, 'delete_order_tb'),
(28, 'Can view order_tb', 7, 'view_order_tb'),
(29, 'Can add order_item_tb', 8, 'add_order_item_tb'),
(30, 'Can change order_item_tb', 8, 'change_order_item_tb'),
(31, 'Can delete order_item_tb', 8, 'delete_order_item_tb'),
(32, 'Can view order_item_tb', 8, 'view_order_item_tb'),
(33, 'Can add log entry', 9, 'add_logentry'),
(34, 'Can change log entry', 9, 'change_logentry'),
(35, 'Can delete log entry', 9, 'delete_logentry'),
(36, 'Can view log entry', 9, 'view_logentry'),
(37, 'Can add permission', 10, 'add_permission'),
(38, 'Can change permission', 10, 'change_permission'),
(39, 'Can delete permission', 10, 'delete_permission'),
(40, 'Can view permission', 10, 'view_permission'),
(41, 'Can add group', 11, 'add_group'),
(42, 'Can change group', 11, 'change_group'),
(43, 'Can delete group', 11, 'delete_group'),
(44, 'Can view group', 11, 'view_group'),
(45, 'Can add user', 12, 'add_user'),
(46, 'Can change user', 12, 'change_user'),
(47, 'Can delete user', 12, 'delete_user'),
(48, 'Can view user', 12, 'view_user'),
(49, 'Can add content type', 13, 'add_contenttype'),
(50, 'Can change content type', 13, 'change_contenttype'),
(51, 'Can delete content type', 13, 'delete_contenttype'),
(52, 'Can view content type', 13, 'view_contenttype'),
(53, 'Can add session', 14, 'add_session'),
(54, 'Can change session', 14, 'change_session'),
(55, 'Can delete session', 14, 'delete_session'),
(56, 'Can view session', 14, 'view_session'),
(57, 'Can add feedback_tb', 15, 'add_feedback_tb'),
(58, 'Can change feedback_tb', 15, 'change_feedback_tb'),
(59, 'Can delete feedback_tb', 15, 'delete_feedback_tb'),
(60, 'Can view feedback_tb', 15, 'view_feedback_tb');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'admin', NULL, 0, '', '', '', 'admin@gmail.com', 0, 0, '0000-00-00 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(9, 'admin', 'logentry'),
(11, 'auth', 'group'),
(10, 'auth', 'permission'),
(12, 'auth', 'user'),
(13, 'contenttypes', 'contenttype'),
(1, 'recycling_app', 'cart_tb'),
(15, 'recycling_app', 'feedback_tb'),
(8, 'recycling_app', 'order_item_tb'),
(7, 'recycling_app', 'order_tb'),
(6, 'recycling_app', 'product_tb'),
(2, 'recycling_app', 'register_tb'),
(3, 'recycling_app', 'unit_register_tb'),
(5, 'recycling_app', 'waste_location_tb'),
(4, 'recycling_app', 'workers_register_tb'),
(14, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-11-12 16:17:51.232367'),
(2, 'auth', '0001_initial', '2020-11-12 16:17:54.067304'),
(3, 'admin', '0001_initial', '2020-11-12 16:18:03.153694'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-11-12 16:18:05.607311'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-11-12 16:18:05.685437'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-11-12 16:18:06.631583'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-11-12 16:18:07.721956'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-11-12 16:18:08.127229'),
(9, 'auth', '0004_alter_user_username_opts', '2020-11-12 16:18:08.557355'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-11-12 16:18:09.540822'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-11-12 16:18:09.618947'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-11-12 16:18:09.681482'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-11-12 16:18:09.853353'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-11-12 16:18:10.040858'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-11-12 16:18:10.308897'),
(16, 'auth', '0011_update_proxy_permissions', '2020-11-12 16:18:10.387006'),
(17, 'recycling_app', '0001_initial', '2020-11-12 16:18:14.341777'),
(18, 'sessions', '0001_initial', '2020-11-12 16:18:28.324438'),
(19, 'recycling_app', '0002_feedback_tb', '2020-11-15 17:09:57.177150'),
(20, 'recycling_app', '0003_remove_order_tb_worker_email', '2020-11-17 05:51:04.935955'),
(21, 'auth', '0012_alter_user_first_name_max_length', '2021-01-27 08:07:15.906802'),
(22, 'recycling_app', '0004_auto_20210127_1337', '2021-01-27 08:07:16.059811'),
(23, 'recycling_app', '0005_unit_register_tb_licence_number', '2021-01-27 08:32:31.364481');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5m5gnxqqk9r15ytfh1yz6sm2kgwe4ptx', 'eyJpZCI6OH0:1mmrDB:Lc7Gflbel8-g6X_FkC-FoKJyECR6pSuwRNZRaQC_gzI', '2021-11-30 05:40:53.554014'),
('b1gruzq4furqxty2uavl4pmwzt15aoim', 'e30:1mmTj8:80mV3v5qoT6-uhHQUtAtQP84ZNi4JRPF2CUS28F1V9w', '2021-11-29 04:36:18.165658'),
('f11tro2f545nw5hvlidbuz8xrldxw5uh', 'ZTJhMDg3Zjc4YjIyZDk1MzQwNmI4YzUyYTliMWMxMTJmNzQyZjUzODp7fQ==', '2020-12-01 05:11:06.057673'),
('frzlvwrqfrnsiyzqdh6d3shq1mnpnxg7', 'Zjc5YzNjZTQ2OTZmYTNhNDIxNDMyMDE1YzYzMjZjMDQxNGQxODVkODp7ImlkIjozfQ==', '2021-04-17 08:58:28.289869'),
('hfm836xkbgafchltpdwbm5y1iopb1kzl', 'ZTJhMDg3Zjc4YjIyZDk1MzQwNmI4YzUyYTliMWMxMTJmNzQyZjUzODp7fQ==', '2020-11-29 17:20:56.253412'),
('orxfupq8fyl518zjesdv730vzgruj64o', 'e30:1lQlgr:uhQNGvx9PjDBzudinWWXBT8Z0IsxBRsrZCuCSDN9Pr4', '2021-04-12 06:47:57.818890'),
('uvjh32f4e4jymhe1mo5ebb216n2bofwg', 'e30:1l4gAd:Ps6UhOMqqo1Z3JxaXkBpQVXMdltMurY2pXIarFfjcKM', '2021-02-10 08:27:23.607879'),
('v054dptjtrxqlf52lgscs7b7dkbyafnq', 'eyJpZCI6OH0:1mmTS1:OdggpYOOh9MTZtM_DAIsKAIkrPB_sxKrp6vOrcJhgpY', '2021-11-29 04:18:37.208975');

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_cart_tb`
--

CREATE TABLE `recycling_app_cart_tb` (
  `id` int(11) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `total` varchar(30) NOT NULL,
  `status` varchar(10) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  `unit_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_cart_tb`
--

INSERT INTO `recycling_app_cart_tb` (`id`, `quantity`, `total`, `status`, `product_id_id`, `unit_id_id`, `user_id_id`) VALUES
(35, '1', '55', 'paid', 16, 5, 8),
(36, '2', '500', 'paid', 14, 6, 8);

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_feedback_tb`
--

CREATE TABLE `recycling_app_feedback_tb` (
  `id` int(11) NOT NULL,
  `feedback` varchar(30) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  `unit_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_order_item_tb`
--

CREATE TABLE `recycling_app_order_item_tb` (
  `id` int(11) NOT NULL,
  `total` varchar(30) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `payment_status` varchar(30) NOT NULL,
  `worker_email` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `cart_id_id` int(11) NOT NULL,
  `order_id_id` int(11) NOT NULL,
  `product_id_id` int(11) NOT NULL,
  `unit_id_id` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_order_item_tb`
--

INSERT INTO `recycling_app_order_item_tb` (`id`, `total`, `date`, `time`, `payment_status`, `worker_email`, `status`, `cart_id_id`, `order_id_id`, `product_id_id`, `unit_id_id`, `user_id_id`) VALUES
(24, '605', '2021-11-16', '11:12:08', 'paid', '', 'pending', 35, 24, 16, 5, 8),
(25, '605', '2021-11-16', '11:12:08', 'paid', '', 'pending', 36, 24, 14, 6, 8);

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_order_tb`
--

CREATE TABLE `recycling_app_order_tb` (
  `id` int(11) NOT NULL,
  `product_id` varchar(30) NOT NULL,
  `payment` varchar(30) NOT NULL,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `total` varchar(30) NOT NULL,
  `payment_status` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `cart_id` varchar(30) NOT NULL,
  `unit_id` varchar(30) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_order_tb`
--

INSERT INTO `recycling_app_order_tb` (`id`, `product_id`, `payment`, `date`, `time`, `total`, `payment_status`, `status`, `cart_id`, `unit_id`, `user_id_id`) VALUES
(24, '[16, 14]', '605', '2021-11-16', '11:12:08', '', 'paid', 'pending', '[35, 36]', '[5, 6]', 8);

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_product_tb`
--

CREATE TABLE `recycling_app_product_tb` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `code` varchar(30) NOT NULL,
  `description` varchar(290) NOT NULL,
  `image` varchar(100) NOT NULL,
  `price` varchar(30) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `unitid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_product_tb`
--

INSERT INTO `recycling_app_product_tb` (`id`, `name`, `code`, `description`, `image`, `price`, `quantity`, `unitid_id`) VALUES
(13, 'pot', 'p01', 'a beautiful pot', 'files/pot_1.jpg', '100', '100', 6),
(14, 'Bottle craft', 'P12', 'Bottle craft', 'files/bottle_art_1.jpg', '250', '100', 6),
(15, 'pen holder', 'P3', 'Pen holder', 'files/pen_holder1_1.jpg', '55', '25', 6),
(16, 'Pencil holder', 'P121', 'Pencil holder', 'files/pen_holder2.jpg', '55', '200', 5);

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_register_tb`
--

CREATE TABLE `recycling_app_register_tb` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `gender` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `mobile_Number` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `Aadhar_Number` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_register_tb`
--

INSERT INTO `recycling_app_register_tb` (`id`, `name`, `email`, `password`, `gender`, `address`, `place`, `mobile_Number`, `status`, `Aadhar_Number`) VALUES
(8, 'liyat', 'liyat@gmail.com', '123', 'female', 'rose villa', 'Thalikulam', '9544981728', 'approved', '7887955544');

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_unit_register_tb`
--

CREATE TABLE `recycling_app_unit_register_tb` (
  `id` int(11) NOT NULL,
  `unit_name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `capacity` varchar(30) NOT NULL,
  `mobile_Number` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `licence_number` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_unit_register_tb`
--

INSERT INTO `recycling_app_unit_register_tb` (`id`, `unit_name`, `email`, `password`, `address`, `place`, `capacity`, `mobile_Number`, `status`, `licence_number`) VALUES
(5, 'KD company', 'kd@gmail.com', '123', 'rose villa', 'thrissur', '200', '9544981728', 'approved', 'LH120'),
(6, 'jk scarp', 'jk@gmail.com', '123', 'JK Scrap', 'thrissur', '1000kg', '8139008725', 'approved', 'QW12');

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_waste_location_tb`
--

CREATE TABLE `recycling_app_waste_location_tb` (
  `id` int(11) NOT NULL,
  `subject` varchar(30) NOT NULL,
  `description` varchar(100) NOT NULL,
  `address` varchar(30) NOT NULL,
  `place` varchar(100) NOT NULL,
  `district` varchar(30) NOT NULL,
  `worker_email` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `user_id_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_waste_location_tb`
--

INSERT INTO `recycling_app_waste_location_tb` (`id`, `subject`, `description`, `address`, `place`, `district`, `worker_email`, `status`, `user_id_id`) VALUES
(12, 'Plastic waste', 'plastic bottles', 'JK mall', 'Thalikulam', 'thrissur', 'das@gmail.com', 'accepted', 8);

-- --------------------------------------------------------

--
-- Table structure for table `recycling_app_workers_register_tb`
--

CREATE TABLE `recycling_app_workers_register_tb` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `dob` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `mobile_Number` varchar(30) NOT NULL,
  `workers_type` varchar(30) NOT NULL,
  `unit_id_id` int(11) NOT NULL,
  `Aadhar_Number` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recycling_app_workers_register_tb`
--

INSERT INTO `recycling_app_workers_register_tb` (`id`, `name`, `email`, `password`, `dob`, `address`, `place`, `mobile_Number`, `workers_type`, `unit_id_id`, `Aadhar_Number`) VALUES
(8, 'das', 'das@gmail.com', '123', '1999-08-08', 'ro0se villa', 'thalikulam', '9544981728', 'collecting dept', 5, '154758424654'),
(9, 'vinu', 'vinu@gmail.com', '123', '1999-08-08', 'rose villa', 'Thalikulam', '9544981728', 'delivery dept', 5, '457897'),
(10, 'kiran', 'kiran@gmail.com', '123', '2021-11-15', 'kiran villa', 'Thrissur', '8139008725', 'collecting dept', 6, '354555757575'),
(11, 'karun', 'karun@gmail.com', '123', '2021-11-09', 'karun villa', 'palarivattam', '8139008725', 'delivery dept', 6, '354555757575');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `recycling_app_cart_tb`
--
ALTER TABLE `recycling_app_cart_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_cart_t_product_id_id_d02e09dd_fk_recycling` (`product_id_id`),
  ADD KEY `recycling_app_cart_t_unit_id_id_88fa1525_fk_recycling` (`unit_id_id`),
  ADD KEY `recycling_app_cart_t_user_id_id_78a51d1a_fk_recycling` (`user_id_id`);

--
-- Indexes for table `recycling_app_feedback_tb`
--
ALTER TABLE `recycling_app_feedback_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_feedba_product_id_id_d2c45705_fk_recycling` (`product_id_id`),
  ADD KEY `recycling_app_feedba_unit_id_id_4f755909_fk_recycling` (`unit_id_id`),
  ADD KEY `recycling_app_feedba_user_id_id_5e199d00_fk_recycling` (`user_id_id`);

--
-- Indexes for table `recycling_app_order_item_tb`
--
ALTER TABLE `recycling_app_order_item_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_order__cart_id_id_d7c2cbb6_fk_recycling` (`cart_id_id`),
  ADD KEY `recycling_app_order__order_id_id_f45dea08_fk_recycling` (`order_id_id`),
  ADD KEY `recycling_app_order__product_id_id_922b86d8_fk_recycling` (`product_id_id`),
  ADD KEY `recycling_app_order__unit_id_id_0a9023c6_fk_recycling` (`unit_id_id`),
  ADD KEY `recycling_app_order__user_id_id_d8238bb2_fk_recycling` (`user_id_id`);

--
-- Indexes for table `recycling_app_order_tb`
--
ALTER TABLE `recycling_app_order_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_order__user_id_id_d86a0d0d_fk_recycling` (`user_id_id`);

--
-- Indexes for table `recycling_app_product_tb`
--
ALTER TABLE `recycling_app_product_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_produc_unitid_id_e5881237_fk_recycling` (`unitid_id`);

--
-- Indexes for table `recycling_app_register_tb`
--
ALTER TABLE `recycling_app_register_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recycling_app_unit_register_tb`
--
ALTER TABLE `recycling_app_unit_register_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recycling_app_waste_location_tb`
--
ALTER TABLE `recycling_app_waste_location_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_waste__user_id_id_4cfe87c1_fk_recycling` (`user_id_id`);

--
-- Indexes for table `recycling_app_workers_register_tb`
--
ALTER TABLE `recycling_app_workers_register_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recycling_app_worker_unit_id_id_dbb91f26_fk_recycling` (`unit_id_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `recycling_app_cart_tb`
--
ALTER TABLE `recycling_app_cart_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `recycling_app_feedback_tb`
--
ALTER TABLE `recycling_app_feedback_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `recycling_app_order_item_tb`
--
ALTER TABLE `recycling_app_order_item_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `recycling_app_order_tb`
--
ALTER TABLE `recycling_app_order_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `recycling_app_product_tb`
--
ALTER TABLE `recycling_app_product_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `recycling_app_register_tb`
--
ALTER TABLE `recycling_app_register_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `recycling_app_unit_register_tb`
--
ALTER TABLE `recycling_app_unit_register_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `recycling_app_waste_location_tb`
--
ALTER TABLE `recycling_app_waste_location_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `recycling_app_workers_register_tb`
--
ALTER TABLE `recycling_app_workers_register_tb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `recycling_app_cart_tb`
--
ALTER TABLE `recycling_app_cart_tb`
  ADD CONSTRAINT `recycling_app_cart_t_product_id_id_d02e09dd_fk_recycling` FOREIGN KEY (`product_id_id`) REFERENCES `recycling_app_product_tb` (`id`),
  ADD CONSTRAINT `recycling_app_cart_t_unit_id_id_88fa1525_fk_recycling` FOREIGN KEY (`unit_id_id`) REFERENCES `recycling_app_unit_register_tb` (`id`),
  ADD CONSTRAINT `recycling_app_cart_t_user_id_id_78a51d1a_fk_recycling` FOREIGN KEY (`user_id_id`) REFERENCES `recycling_app_register_tb` (`id`);

--
-- Constraints for table `recycling_app_feedback_tb`
--
ALTER TABLE `recycling_app_feedback_tb`
  ADD CONSTRAINT `recycling_app_feedba_product_id_id_d2c45705_fk_recycling` FOREIGN KEY (`product_id_id`) REFERENCES `recycling_app_product_tb` (`id`),
  ADD CONSTRAINT `recycling_app_feedba_unit_id_id_4f755909_fk_recycling` FOREIGN KEY (`unit_id_id`) REFERENCES `recycling_app_unit_register_tb` (`id`),
  ADD CONSTRAINT `recycling_app_feedba_user_id_id_5e199d00_fk_recycling` FOREIGN KEY (`user_id_id`) REFERENCES `recycling_app_register_tb` (`id`);

--
-- Constraints for table `recycling_app_order_item_tb`
--
ALTER TABLE `recycling_app_order_item_tb`
  ADD CONSTRAINT `recycling_app_order__cart_id_id_d7c2cbb6_fk_recycling` FOREIGN KEY (`cart_id_id`) REFERENCES `recycling_app_cart_tb` (`id`),
  ADD CONSTRAINT `recycling_app_order__order_id_id_f45dea08_fk_recycling` FOREIGN KEY (`order_id_id`) REFERENCES `recycling_app_order_tb` (`id`),
  ADD CONSTRAINT `recycling_app_order__product_id_id_922b86d8_fk_recycling` FOREIGN KEY (`product_id_id`) REFERENCES `recycling_app_product_tb` (`id`),
  ADD CONSTRAINT `recycling_app_order__unit_id_id_0a9023c6_fk_recycling` FOREIGN KEY (`unit_id_id`) REFERENCES `recycling_app_unit_register_tb` (`id`),
  ADD CONSTRAINT `recycling_app_order__user_id_id_d8238bb2_fk_recycling` FOREIGN KEY (`user_id_id`) REFERENCES `recycling_app_register_tb` (`id`);

--
-- Constraints for table `recycling_app_order_tb`
--
ALTER TABLE `recycling_app_order_tb`
  ADD CONSTRAINT `recycling_app_order__user_id_id_d86a0d0d_fk_recycling` FOREIGN KEY (`user_id_id`) REFERENCES `recycling_app_register_tb` (`id`);

--
-- Constraints for table `recycling_app_product_tb`
--
ALTER TABLE `recycling_app_product_tb`
  ADD CONSTRAINT `recycling_app_produc_unitid_id_e5881237_fk_recycling` FOREIGN KEY (`unitid_id`) REFERENCES `recycling_app_unit_register_tb` (`id`);

--
-- Constraints for table `recycling_app_waste_location_tb`
--
ALTER TABLE `recycling_app_waste_location_tb`
  ADD CONSTRAINT `recycling_app_waste__user_id_id_4cfe87c1_fk_recycling` FOREIGN KEY (`user_id_id`) REFERENCES `recycling_app_register_tb` (`id`);

--
-- Constraints for table `recycling_app_workers_register_tb`
--
ALTER TABLE `recycling_app_workers_register_tb`
  ADD CONSTRAINT `recycling_app_worker_unit_id_id_dbb91f26_fk_recycling` FOREIGN KEY (`unit_id_id`) REFERENCES `recycling_app_unit_register_tb` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
