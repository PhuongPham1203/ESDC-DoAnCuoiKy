-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th4 05, 2021 lúc 08:24 PM
-- Phiên bản máy phục vụ: 10.4.17-MariaDB
-- Phiên bản PHP: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `esdc_doan`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `book`
--

CREATE TABLE `book` (
  `id` int(11) NOT NULL,
  `check_book` tinyint(4) NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date_checkin` date NOT NULL,
  `date_checkout` date NOT NULL,
  `custumer_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `custumer_email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `custumer_number` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date_create` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `book_room`
--

CREATE TABLE `book_room` (
  `id_book` int(11) NOT NULL,
  `id_room` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `check_book_room` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `price`
--

CREATE TABLE `price` (
  `id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `price` double NOT NULL,
  `oder` int(11) NOT NULL,
  `status_check` int(11) NOT NULL DEFAULT 1,
  `date_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `room`
--

CREATE TABLE `room` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL,
  `room_type` int(11) NOT NULL,
  `room_level` int(11) NOT NULL,
  `status_check` tinyint(4) NOT NULL DEFAULT 1,
  `date_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `room`
--

INSERT INTO `room` (`id`, `name`, `description`, `room_type`, `room_level`, `status_check`, `date_create`) VALUES
(1, 'A101', 'Phòng stand ở tầng 1', 2, 1, 1, '2021-04-04 15:02:15'),
(2, 'A102', 'Phòng 102 ở tầng 1', 2, 1, 1, '2021-04-04 15:03:10'),
(3, 'A103', 'Phòng 103 ở tầng 1', 2, 1, 1, '2021-04-04 15:03:25'),
(4, 'A104', 'Phòng 104 ở tầng 1', 2, 1, 1, '2021-04-04 15:03:37'),
(5, 'A201', 'Phòng này ở tầng 2', 3, 2, 1, '2021-04-04 15:17:39'),
(6, 'A202', 'A202', 3, 2, 1, '2021-04-04 15:19:27'),
(7, 'A203', 'A203', 3, 2, 1, '2021-04-04 15:19:37'),
(8, 'A204', 'A204', 2, 2, 1, '2021-04-04 15:19:57'),
(9, 'A205', 'A205', 2, 2, 1, '2021-04-04 15:20:09'),
(10, 'A301', 'A301', 4, 3, 1, '2021-04-04 15:20:26'),
(11, 'A302', 'A302', 4, 3, 1, '2021-04-04 15:20:33'),
(12, 'A303', 'A303', 4, 3, 1, '2021-04-04 15:21:07'),
(13, 'A304', 'A304', 4, 3, 1, '2021-04-04 15:21:25'),
(14, 'A351', 'A401', 5, 4, 1, '2021-04-04 15:21:50'),
(15, 'A352', 'A402', 5, 4, 1, '2021-04-04 15:22:05'),
(16, 'A353', 'A403', 7, 4, 1, '2021-04-04 15:22:35'),
(17, 'A501', 'Phòng đơn', 6, 5, 1, '2021-04-04 15:23:27'),
(18, 'A502', 'A502', 6, 5, 1, '2021-04-04 15:23:39'),
(19, 'A503', 'A503', 2, 5, 1, '2021-04-04 15:23:52'),
(20, 'A504', 'A504', 3, 5, 1, '2021-04-04 15:24:05'),
(21, 'A601', 'A601', 3, 6, 1, '2021-04-04 15:24:19'),
(22, 'A602', 'A602', 3, 6, 1, '2021-04-04 15:24:31'),
(23, 'A701', 'Căn phòng tập thể', 7, 11, 1, '2021-04-04 15:24:49'),
(24, 'A206', 'Phòng thuộc tầng 2', 3, 2, 1, '2021-04-04 15:57:13'),
(25, 'A710', 'Đây là tầng 7', 6, 11, 0, '2021-04-05 23:27:21');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `room_level`
--

CREATE TABLE `room_level` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `description` text COLLATE utf8_unicode_ci NOT NULL,
  `status_check` tinyint(4) NOT NULL DEFAULT 1,
  `date_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `room_level`
--

INSERT INTO `room_level` (`id`, `name`, `description`, `status_check`, `date_create`) VALUES
(1, 'Tầng 1', 'Tầng 1 của khách sạn', 1, '2021-04-04 13:47:57'),
(2, 'Tầng 2', 'Đây là tầng 2', 1, '2021-04-04 13:48:20'),
(3, 'Tầng 3', 'Tầng 3 của khách sạn', 1, '2021-04-04 13:48:29'),
(4, 'Tầng 3.5', 'Tầng 4', 1, '2021-04-04 13:48:36'),
(5, 'Tầng 5', 'Tầng 5', 1, '2021-04-04 13:48:44'),
(6, 'Tầng 6', 'Tầng 6', 1, '2021-04-04 13:48:51'),
(7, 'Tầng 5.5', 'Tầng 5.5', 0, '2021-04-04 13:49:01'),
(8, 'Tầng 7', 'Tầng 7', 0, '2021-04-04 13:49:11'),
(9, 'Tầng 8', 'Tầng 8', 0, '2021-04-04 13:49:20'),
(10, 'Tầng 5.5', 'Tầng giữa 5 và 6', 0, '2021-04-04 13:53:13'),
(11, 'Tầng 7', 'Tầng 7 của hote', 1, '2021-04-04 14:28:43');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `room_type`
--

CREATE TABLE `room_type` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT ' ',
  `description` text COLLATE utf8_unicode_ci NOT NULL,
  `number_adult` int(11) NOT NULL DEFAULT 0,
  `number_children` int(11) NOT NULL DEFAULT 0,
  `price_hour` int(11) DEFAULT NULL,
  `price_day` int(11) DEFAULT NULL,
  `status_check` tinyint(4) NOT NULL DEFAULT 1,
  `date_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `room_type`
--

INSERT INTO `room_type` (`id`, `name`, `description`, `number_adult`, `number_children`, `price_hour`, `price_day`, `status_check`, `date_create`) VALUES
(1, 'a', '1', 1, 2, NULL, NULL, 0, '2021-04-04 12:19:08'),
(2, 'Phòng Standard (STD)', 'Standard là hạng phòng tiêu chuẩn trong khách sạn, có diện tích nhỏ, thường nằm ở tầng thấp, không có view hoặc view không đẹp. Phòng STD được trang bị các vật dụng - trang thiết bị cơ bản và có mức giá thấp nhất.', 2, 1, NULL, NULL, 1, '2021-04-04 12:19:43'),
(3, 'Phòng Superior (SUP)', 'So với Standard thì Superior là hạng phòng có chất lượng tốt hơn - diện tích rộng - trang thiết bị tiện nghi - view đẹp. Cũng vì thế mà mức giá thuê phòng SUP sẽ cao hơn.', 2, 0, NULL, NULL, 1, '2021-04-04 12:20:06'),
(4, 'Phòng Deluxe (DLX)', 'Hạng phòng trên SUP 1 bậc là Deluxe. Đây là loại phòng cao cấp trong các khách sạn, chủ yếu nằm trên tầng cao với không gian rộng, nhiều thiết bị tiện nghi - view ngắm cảnh đẹp.', 4, 4, NULL, NULL, 1, '2021-04-04 12:20:18'),
(5, 'Phòng Suite (SUT)', 'SUT là hạng phòng cao cấp nhất của mỗi khách sạn. Và với mục đích tăng thêm mức độ VIP, phòng SUT hay được đặt tên là: phòng Hoàng gia (Royal Suite Room), phòng Tổng Thống (President Room)… Một đặc điểm dễ nhận thấy là phòng Suite thường nằm ở vị trí cho tầm nhìn đẹp nhất và trong mỗi phòng như vậy có thể có nhiều phòng chức năng khác nhau: phòng khách, phòng ngủ, phòng họp, phòng ăn… Cùng với đó là các dịch vụ đặc biệt kèm theo: đưa - đón tận sân bay, Butler phục vụ riêng…', 2, 2, NULL, NULL, 1, '2021-04-04 12:20:37'),
(6, 'Phòng đơn', 'Phòng đơn dành cho một người hoặc kèm theo trẻ em', 1, 1, NULL, NULL, 1, '2021-04-04 12:21:13'),
(7, 'Phòng Tập thể', 'Đây là phòng tập thể', 4, 4, NULL, NULL, 1, '2021-04-04 13:04:38');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `token` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `level` tinyint(4) NOT NULL,
  `status_check` tinyint(4) NOT NULL,
  `date_create` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `token`, `level`, `status_check`, `date_create`) VALUES
(1, 'admin', 'admin', '5G2RWB4CHU', 1, 1, '2021-03-16 12:36:15'),
(2, 'letan', 'letan', 'TWTS72I17J', 2, 1, '2021-03-16 12:36:36');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `book_room`
--
ALTER TABLE `book_room`
  ADD KEY `id_book` (`id_book`),
  ADD KEY `id_room` (`id_room`);

--
-- Chỉ mục cho bảng `price`
--
ALTER TABLE `price`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_roomtype` (`room_type`),
  ADD KEY `room_roomlevel` (`room_level`);

--
-- Chỉ mục cho bảng `room_level`
--
ALTER TABLE `room_level`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `room_type`
--
ALTER TABLE `room_type`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `book`
--
ALTER TABLE `book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `room`
--
ALTER TABLE `room`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT cho bảng `room_level`
--
ALTER TABLE `room_level`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT cho bảng `room_type`
--
ALTER TABLE `room_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `book_room`
--
ALTER TABLE `book_room`
  ADD CONSTRAINT `book_room_ibfk_1` FOREIGN KEY (`id_book`) REFERENCES `book` (`id`),
  ADD CONSTRAINT `book_room_ibfk_2` FOREIGN KEY (`id_room`) REFERENCES `room` (`id`);

--
-- Các ràng buộc cho bảng `room`
--
ALTER TABLE `room`
  ADD CONSTRAINT `room_roomlevel` FOREIGN KEY (`room_level`) REFERENCES `room_level` (`id`),
  ADD CONSTRAINT `room_roomtype` FOREIGN KEY (`room_type`) REFERENCES `room_type` (`id`);

--
-- Các ràng buộc cho bảng `room_type`
--
ALTER TABLE `room_type`
  ADD CONSTRAINT `roomtype_roomtype_price` FOREIGN KEY (`price_hour`) REFERENCES `roomtype_price` (`id`),
  ADD CONSTRAINT `roomtype_roomtype_price_day` FOREIGN KEY (`price_day`) REFERENCES `roomtype_price` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
