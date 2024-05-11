CREATE DATABASE IF NOT EXISTS `QLDSV` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;

USE `QLDSV`;

CREATE TABLE `account_gv` (
  `STT` int(11) NOT NULL AUTO_INCREMENT,
  `USERNAME` varchar(50) NOT NULL,
  `PASS` varchar(50) NOT NULL,
  PRIMARY KEY (`STT`),
  KEY `USERNAME` (`USERNAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
  
--
-- Dumping data for table `account_gv`
--

INSERT INTO `account_gv` (`STT`, `USERNAME`, `PASS`) VALUES
(1, 'GV01001', '123456'),
(2, 'GV01002', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `account_sv`
--

CREATE TABLE `account_sv` (
  `STT` int(10) NOT NULL,
  `USERNAME` varchar(10) NOT NULL,
  `PASS` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for table `account_sv`
--
ALTER TABLE `account_sv`
  ADD PRIMARY KEY (`STT`),
  ADD KEY `USERNAME` (`USERNAME`);
  

--
-- Dumping data for table `account_sv`
--

INSERT INTO `account_sv` (`STT`, `USERNAME`, `PASS`) VALUES
(1, '222010001', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `baithi`
--

CREATE TABLE `baithi` (
  `MAMH` varchar(10) NOT NULL,
  `MASV` varchar(10) NOT NULL,
  `SOPHACH` varchar(10) NOT NULL,
  `TINHTRANG` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for table `baithi`
--
ALTER TABLE `baithi`
  ADD PRIMARY KEY (`MASV`,`MAMH`);
-- --------------------------------------------------------

--
-- Table structure for table `bangdiem`
--

CREATE TABLE `bangdiem` (
  `MABD` varchar(10) NOT NULL,
  `HOCKY` varchar(10) NOT NULL DEFAULT '2',
  `NAMHOC` varchar(10) DEFAULT '2024',
  `DIEMTK_HE4` decimal(3,2) DEFAULT 0.00,
  `DIEMTK_HE10` decimal(3,2) DEFAULT 0.00,
  `XEPLOAIHK` varchar(10) DEFAULT NULL,
  `DIEMTB_TL` decimal(3,2) DEFAULT 0.00,
  `TONGTINCHI` int(11) DEFAULT 42,
  `MASV` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `bangdiem`
--
ALTER TABLE `bangdiem`
  ADD PRIMARY KEY (`MABD`),
  ADD KEY `MASV` (`MASV`);
  
  
--
-- Dumping data for table `bangdiem`
--

INSERT INTO `bangdiem` (`MABD`, `HOCKY`, `NAMHOC`, `DIEMTK_HE4`, `DIEMTK_HE10`, `XEPLOAIHK`, `DIEMTB_TL`, `TONGTINCHI`, `MASV`) VALUES
('D22201001', '2', '2024', 3.50, 8.17, 'GIỎI', 3.06, 62, '222010001'),
('D22201002', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010002'),
('D22201003', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010003'),
('D22201004', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010004'),
('D22201005', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010005'),
('D22201006', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010006'),
('D22201007', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010007'),
('D22201008', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010008'),
('D22201009', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010009'),
('D22201010', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010010'),
('D22201011', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010011'),
('D22201012', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010012'),
('D22201013', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010013'),
('D22201014', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010014'),
('D22201015', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010015'),
('D22201016', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010016'),
('D22201017', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010017'),
('D22201018', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010018'),
('D22201019', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010019'),
('D22201020', '2', '2024', 0.00, 0.00, NULL, 0.00, 42, '222010020');

-- --------------------------------------------------------

--
-- Table structure for table `chitietbangdiem`
--

CREATE TABLE `chitietbangdiem` (
  `MABD` varchar(10) NOT NULL,
  `MANHOM` varchar(10) NOT NULL,
  `DIEMQUATRINH` decimal(4,2) DEFAULT 0.00,
  `HESO_QT` decimal(3,2) DEFAULT 0.50,
  `DIEMTHI` decimal(4,2) DEFAULT 0.00,
  `HESO_THI` decimal(3,2) DEFAULT 0.50,
  `DIEMTB_HE10` decimal(4,2) DEFAULT 0.00,
  `DIEMTB_HE4` decimal(4,2) DEFAULT 0.00,
  `XEPLOAI` varchar(10) DEFAULT NULL,
  `TINHTRANG` bit(1) DEFAULT b'0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `chitietbangdiem`
--
ALTER TABLE `chitietbangdiem`
  ADD PRIMARY KEY (`MABD`,`MANHOM`),
  ADD KEY `MANHOM` (`MANHOM`);


--
-- Dumping data for table `chitietbangdiem`
--

INSERT INTO `chitietbangdiem` (`MABD`, `MANHOM`, `DIEMQUATRINH`, `HESO_QT`, `DIEMTHI`, `HESO_THI`, `DIEMTB_HE10`, `DIEMTB_HE4`, `XEPLOAI`, `TINHTRANG`) VALUES
('D22201001', 'N010101', 8.50, 0.50, 8.80, 0.50, 8.65, 4.00, 'A', b'1'),
('D22201001', 'N010201', 8.00, 0.50, 8.00, 0.50, 8.00, 3.00, 'B', b'1'),
('D22201001', 'N010301', 8.50, 0.50, 8.50, 0.50, 8.50, 4.00, 'A', b'1'),
('D22201001', 'N010401', 7.50, 0.50, 7.50, 0.50, 7.50, 3.00, 'B', b'1'),
('D22201002', 'N010101', 8.25, 0.50, 8.25, 0.50, 8.25, 4.00, 'A', b'1'),
('D22201002', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201003', 'N010101', 6.90, 0.50, 7.00, 0.50, 6.95, 3.00, 'B', b'1'),
('D22201003', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201004', 'N010101', 6.80, 0.50, 6.80, 0.50, 6.80, 3.00, 'B', b'1'),
('D22201004', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201005', 'N010101', 8.80, 0.50, 8.80, 0.50, 8.80, 4.00, 'A', b'1'),
('D22201005', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201006', 'N010101', 9.10, 0.50, 9.00, 0.50, 9.15, 4.00, 'A', b'1'),
('D22201006', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201007', 'N010101', 9.25, 0.50, 9.25, 0.50, 9.25, 4.00, 'A', b'1'),
('D22201007', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201008', 'N010101', 5.80, 0.50, 5.80, 0.50, 5.80, 2.00, 'C', b'1'),
('D22201008', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201009', 'N010101', 6.50, 0.50, 6.50, 0.50, 6.50, 3.00, 'B', b'1'),
('D22201009', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'0'),
('D22201010', 'N010101', 9.00, 0.50, 9.00, 0.50, 9.00, 4.00, 'A', b'1'),
('D22201010', 'N010201', 0.00, 0.50, 0.00, 0.50, 0.00, 0.00, NULL, b'1'),
('D22201011', 'N010102', 8.50, 0.50, 8.50, 0.50, 8.50, 4.00, 'A', b'1'),
('D22201012', 'N010102', 7.30, 0.50, 7.30, 0.50, 7.30, 3.00, 'B', b'1'),
('D22201013', 'N010102', 6.00, 0.50, 6.00, 0.50, 6.00, 2.00, 'C', b'1'),
('D22201014', 'N010102', 8.80, 0.50, 8.80, 0.50, 8.80, 4.00, 'A', b'1'),
('D22201015', 'N010102', 7.50, 0.50, 7.50, 0.50, 7.50, 3.00, 'B', b'1'),
('D22201016', 'N010102', 9.25, 0.50, 9.25, 0.50, 9.25, 4.00, 'A', b'1'),
('D22201017', 'N010102', 9.00, 0.50, 9.00, 0.50, 9.00, 4.00, 'A', b'1'),
('D22201018', 'N010102', 4.50, 0.50, 4.50, 0.50, 4.50, 1.00, 'D', b'1'),
('D22201019', 'N010102', 1.00, 0.50, 3.00, 0.50, 2.00, 0.00, 'F', b'0'),
('D22201020', 'N010102', 3.00, 0.50, 1.00, 0.50, 2.00, 0.00, 'F', b'0');

-- --------------------------------------------------------

--
-- Table structure for table `dangkynhom`
--

CREATE TABLE `dangkynhom` (
  `MASV` varchar(10) NOT NULL,
  `MANHOM` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `dangkynhom`
--
ALTER TABLE `dangkynhom`
  ADD PRIMARY KEY (`MASV`,`MANHOM`),
  ADD KEY `MANHOM` (`MANHOM`);


--
-- Dumping data for table `dangkynhom`
--

INSERT INTO `dangkynhom` (`MASV`, `MANHOM`) VALUES
('222010001', 'N010101'),
('222010001', 'N010201'),
('222010001', 'N010301'),
('222010001', 'N010401'),
('222010002', 'N010101'),
('222010002', 'N010201'),
('222010003', 'N010101'),
('222010003', 'N010201'),
('222010004', 'N010101'),
('222010004', 'N010201'),
('222010005', 'N010101'),
('222010005', 'N010201'),
('222010006', 'N010101'),
('222010006', 'N010201'),
('222010007', 'N010101'),
('222010007', 'N010201'),
('222010008', 'N010101'),
('222010008', 'N010201'),
('222010009', 'N010101'),
('222010009', 'N010201'),
('222010010', 'N010101'),
('222010010', 'N010201'),
('222010011', 'N010102'),
('222010011', 'N010202'),
('222010012', 'N010102'),
('222010012', 'N010202'),
('222010013', 'N010102'),
('222010013', 'N010202'),
('222010014', 'N010102'),
('222010014', 'N010202'),
('222010015', 'N010102'),
('222010015', 'N010202'),
('222010016', 'N010102'),
('222010016', 'N010202'),
('222010017', 'N010102'),
('222010017', 'N010202'),
('222010018', 'N010102'),
('222010018', 'N010202'),
('222010019', 'N010102'),
('222010019', 'N010202'),
('222010020', 'N010102'),
('222010020', 'N010202');

-- --------------------------------------------------------

--
-- Table structure for table `giangvien`
--

CREATE TABLE `giangvien` (
  `MAGV` varchar(10) NOT NULL,
  `HOTENGV` varchar(150) DEFAULT NULL,
  `NGAYSINH` date DEFAULT NULL,
  `GIOITINH` bit(1) DEFAULT NULL,
  `MAKHOA` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `giangvien`
--
ALTER TABLE `giangvien`
  ADD PRIMARY KEY (`MAGV`),
  ADD KEY `MAKHOA` (`MAKHOA`);
  
  
--
-- Dumping data for table `giangvien`
--

INSERT INTO `giangvien` (`MAGV`, `HOTENGV`, `NGAYSINH`, `GIOITINH`, `MAKHOA`) VALUES
('GV01001', 'Trương Thanh Tùng', '1986-12-03', b'1', 'CNTT01'),
('GV01002', 'Hồ Thanh Việt', '1992-05-27', b'1', 'CNTT01'),
('GV01003', 'Nguyễn Thị Hương', '1989-09-03', b'0', 'CNTT01'),
('GV01004', 'Nguyến Thanh Thuận', '1972-05-03', b'0', 'CNTT01'),
('GV02001', 'Phan Duy Khương', '1988-08-03', b'1', 'CNTT01'),
('GV02002', 'Trần Mỹ Lan', '1993-05-11', b'0', 'CNTT01'),
('GV02003', 'Trần Hồ Khải ', '1981-01-03', b'1', 'CNTT01'),
('GV02004', 'Hồ Thị Mỹ Ngọc', '1991-05-03', b'0', 'CNTT01'),
('GV03001', 'Nguyễn Phú Trọng Nam', '1977-03-03', b'1', 'CNTT01'),
('GV03002', 'TLê Thị Thanh Thảo', '1986-05-01', b'0', 'CNTT01'),
('GV03003', 'Nguyễn Thanh Việt', '1974-11-03', b'1', 'CNTT01'),
('GV03004', 'Phan Tuấn An', '1986-05-20', b'1', 'CNTT01');

-- --------------------------------------------------------

--
-- Table structure for table `khoa`
--

CREATE TABLE `khoa` (
  `MAKHOA` varchar(10) NOT NULL,
  `TENKHOA` varchar(100) NOT NULL,
  `SDT` varchar(12) NOT NULL,
  `PHONG` varchar(10) NOT NULL,
  `TRUONGKHOA` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `khoa`
--
ALTER TABLE `khoa`
  ADD PRIMARY KEY (`MAKHOA`);


--
-- Dumping data for table `khoa`
--

INSERT INTO `khoa` (`MAKHOA`, `TENKHOA`, `SDT`, `PHONG`, `TRUONGKHOA`) VALUES
('CNTT01', 'Công nghệ thông tin', '0876555829', 'A.A101', 'GV01001'),
('LUAT02', 'Luật', '0978645727', 'D.A101', 'GV02001'),
('NN03', 'Ngoại ngữ', '0987999634', 'D.A102', 'GV03001');

-- --------------------------------------------------------

--
-- Table structure for table `lop`
--

CREATE TABLE `lop` (
  `MALOP` varchar(10) NOT NULL,
  `TENLOP` varchar(50) NOT NULL,
  `KHOA` varchar(10) NOT NULL,
  `KHOAHOC` varchar(10) NOT NULL,
  `HEDAOTAO` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Indexes for table `lop`
--
ALTER TABLE `lop`
  ADD PRIMARY KEY (`MALOP`),
  ADD KEY `KHOA` (`KHOA`);


--
-- Dumping data for table `lop`
--

INSERT INTO `lop` (`MALOP`, `TENLOP`, `KHOA`, `KHOAHOC`, `HEDAOTAO`) VALUES
('DCT0122A', 'Công nghệ thông tin - Lớp A', 'CNTT01', 'K22', 'Đại Học Chính Quy'),
('DCT0122B', 'Công nghệ thông tin - Lớp B', 'CNTT01', 'K22', 'Đại Học Chính Quy');

-- --------------------------------------------------------

--
-- Table structure for table `monhoc`
--

CREATE TABLE `monhoc` (
  `MAMH` varchar(11) NOT NULL,
  `TENMH` varchar(150) NOT NULL,
  `SOTC` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `monhoc`
--
ALTER TABLE `monhoc`
  ADD PRIMARY KEY (`MAMH`);


--
-- Dumping data for table `monhoc`
--

INSERT INTO `monhoc` (`MAMH`, `TENMH`, `SOTC`) VALUES
('2010001', 'Cơ sở trí tuệ nhân tạo ', 4),
('2010002', 'Ngôn ngữ lập trình Python', 4),
('2010003', 'Ngôn ngữ lập trình Java', 4),
('2010004', 'Lập trình Web và ứng dụng', 4),
('2010005', 'Xác xuất thống kê ', 4),
('2010006', 'Hệ điều hành ', 4);

-- --------------------------------------------------------

--
-- Table structure for table `nhommonhoc`
--

CREATE TABLE `nhommonhoc` (
  `MANHOM` varchar(10) NOT NULL,
  `MAGV` varchar(10) NOT NULL,
  `MAMH` varchar(10) NOT NULL,
  `TENNHOM` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `nhommonhoc`
--
ALTER TABLE `nhommonhoc`
  ADD PRIMARY KEY (`MANHOM`),
  ADD KEY `MAGV` (`MAGV`,`MAMH`),
  ADD KEY `MAMH` (`MAMH`);


--
-- Dumping data for table `nhommonhoc`
--

INSERT INTO `nhommonhoc` (`MANHOM`, `MAGV`, `MAMH`, `TENNHOM`) VALUES
('N010101', 'GV01001', '2010001', 'Cơ sở trí tuệ nhân tạo - Nhóm 1'),
('N010102', 'GV01002', '2010001', 'Cơ sở trí tuệ nhân tạo - Nhóm 2'),
('N010201', 'GV01001', '2010002', 'Ngôn ngữ lập trình Python - Nhóm 1'),
('N010202', 'GV01002', '2010002', 'Ngôn ngữ lập trình Python - Nhóm 2'),
('N010301', 'GV01003', '2010003', 'Ngôn Ngữ lập trình Java - Nhóm 1'),
('N010401', 'GV01004', '2010004', 'Lập trình Web và ứng dụng - Nhóm 1');

-- --------------------------------------------------------

--
-- Table structure for table `sinhvien`
--

CREATE TABLE `sinhvien` (
  `MASV` varchar(10) NOT NULL,
  `HOTEN` varchar(150) NOT NULL,
  `NGAYSINH` date DEFAULT NULL,
  `GIOITINH` bit(2) NOT NULL DEFAULT b'0',
  `DIACHI` varchar(250) NOT NULL,
  `SDT` varchar(12) NOT NULL,
  `LOP` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


--
-- Indexes for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD PRIMARY KEY (`MASV`),
  ADD KEY `LOP` (`LOP`);

--
-- Dumping data for table `sinhvien`
--

INSERT INTO `sinhvien` (`MASV`, `HOTEN`, `NGAYSINH`, `GIOITINH`, `DIACHI`, `SDT`, `LOP`) VALUES
('222010001', 'Ngô Trí Hoàng An', '2004-12-04', b'01', '106106 Đường Lê Hồng Phong, Quận 5\n', '0816639022', 'DCT0122B'),
('222010002', 'Phạm Hoàng Anh', '2004-04-25', b'01', '8080 Đường Huỳnh Mẫn Đạt, Quận 5\n', '0864792899', 'DCT0122A'),
('222010003', 'Trần Thế Huy', '2004-05-25', b'01', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0864792899', 'DCT0122A'),
('222010004', 'Trần Thế An', '2004-01-12', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0776538800', 'DCT0122A'),
('222010005', 'Đỗ Lê Trí Ân', '2004-01-17', b'01', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0816639022', 'DCT0122B'),
('222010006', 'Trương Thế Bảo', '2004-05-17', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010007', 'Nguyễn Hoàng Bách', '2004-05-03', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122B'),
('222010008', 'Lê Thiện Chí', '2004-01-05', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1', '0864792899', 'DCT0122A'),
('222010009', 'Ngô Gia Cường', '2004-01-02', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122A'),
('222010010', 'Lê Ngọc Quỳnh Chi', '2004-05-28', b'00', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0816639022', 'DCT0122A'),
('222010011', 'Hồ Lê Minh Chi', '2004-01-26', b'00', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010012', 'Hà Duy', '2004-05-05', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0776538800', 'DCT0122A'),
('222010013', 'Nguyễn Phúc Duy', '2004-01-24', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122B'),
('222010014', 'Nguyễn Văn Đạt', '2004-01-21', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122B'),
('222010015', 'Phạm Hoàng Đạt', '2004-02-02', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010016', 'Nguyễn Nhật Đông', '2004-05-06', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010017', 'Hà Thu Giang', '2004-05-20', b'00', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122B'),
('222010018', 'Lê Thị Thu Hà', '2004-05-27', b'00', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0776538800', 'DCT0122B'),
('222010019', 'Trần Thị Ánh Hạ', '2004-02-07', b'00', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0816639022', 'DCT0122A'),
('222010020', 'Vũ Văn Hà Huy', '2004-02-09', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122B'),
('222010021', 'Nguyễn Quỳnh Như', '2004-04-18', b'00', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010022', 'Phạm Minh Huy', '2004-02-11', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122B'),
('222010023', 'Nguyễn Hồ Chí Hùng', '2004-02-13', b'01', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010024', 'Lâm văn Hùng', '2004-02-18', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122B'),
('222010025', 'Trương Gia Huệ', '2004-02-25', b'00', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010026', 'Nguyễn Thị Thu Huệ', '2004-02-28', b'00', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0816639022', 'DCT0122A'),
('222010027', 'Vũ Tiến Lợi', '2004-02-21', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010028', 'Trương Nguyễn Tấn Lộc', '2004-03-15', b'01', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010029', 'Hàng Quang Khải', '2004-03-11', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122A'),
('222010030', 'Hồ Khải', '2004-03-17', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122A'),
('222010031', 'Trương Tấn Khôi', '2004-03-19', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010032', 'Hà Lê Vũ Khôi', '2004-03-29', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122B'),
('222010033', 'Nguyến Bảo Minh', '2004-03-22', b'01', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010034', 'Trương Vũ Văn Minh', '2004-03-26', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0987666002', 'DCT0122A'),
('222010035', 'Hồ Khải Minh', '2004-03-28', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010036', 'Hà Thị Ánh My', '2004-03-12', b'00', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010037', 'Nguyễn Ngọc My', '2004-03-04', b'00', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0816639022', 'DCT0122A'),
('222010038', 'Vũ Tuấn Ngọc', '2004-03-07', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122A'),
('222010039', 'Trần Lê Bảo Ngọc', '2004-04-11', b'00', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010040', 'Hồ Thị Tuyết Như', '2004-04-16', b'00', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0816639022', 'DCT0122A'),
('222010042', 'Nguyễn Bảo Nhi', '2004-04-29', b'00', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010043', 'Hồ Trần Diệu Nhi', '2004-04-20', b'00', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010044', 'Nguyễn Thanh Phương', '2004-04-22', b'00', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0987666002', 'DCT0122A'),
('222010045', 'Trần Gia Phú', '2004-04-26', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122B'),
('222010046', 'Nguyễn Lê Hoàng Phúc', '2004-04-05', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122B'),
('222010047', 'Trần Thiện Phúc', '2004-04-03', b'01', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010048', 'Hà Văn Phúc', '2004-05-12', b'01', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010049', 'Lê Minh Quang', '2004-05-19', b'01', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0987666002', 'DCT0122A'),
('222010050', 'Nguyễn Ngọc Quang', '2004-05-14', b'01', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0816639022', 'DCT0122A'),
('222010052', 'Trương Ngọc Diễm Quỳnh', '2004-06-27', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0776538800', 'DCT0122B'),
('222010053', 'Ngô Hồng Sơn', '2004-08-26', b'01', '6464 Đường Trần Quốc Toản, Quận 3\n', '0816639022', 'DCT0122A'),
('222010054', 'Phạm Duy Sơn', '2004-09-11', b'01', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122A'),
('222010055', 'Vũ Thanh Sang', '2004-03-08', b'01', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010056', 'Trịnh Sang', '2004-09-11', b'01', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0816639022', 'DCT0122B'),
('222010057', 'Cao Thanh Tú', '2004-06-27', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0987666002', 'DCT0122B'),
('222010058', 'Hoàng Phan Duy Tú', '2004-09-11', b'01', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010059', 'Đặng Ngọc Tú', '2004-08-26', b'01', '1010 Đường Đồng Khởi, Quận 1\n', '0816639022', 'DCT0122B'),
('222010060', 'Vũ Ngọc Thanh Thu', '2004-10-10', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122B'),
('222010061', 'Trương Mỹ Thu', '2004-06-27', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122A'),
('222010062', 'Nguyễn Thị Minh Thu', '2004-08-26', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122B'),
('222010063', 'Hồ Thị Minh Thư', '2004-09-11', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0864792899', 'DCT0122A'),
('222010064', 'Ngô Anh Thư', '2004-11-13', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010065', 'Nguyễn Thị Ánh Thư', '2004-03-08', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0987666002', 'DCT0122B'),
('222010066', 'Nguyễn Đình Thông', '2004-08-26', b'01', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122A'),
('222010067', 'Hồ Viết Thông', '2004-11-13', b'01', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0816639022', 'DCT0122B'),
('222010068', 'Lê Hồ Mỹ Trang', '2004-10-10', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122B'),
('222010069', 'Vũ Khánh Trang', '2004-06-27', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122B'),
('222010070', 'Nguyễn Thị Phương Trang', '2004-08-26', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122B'),
('222010071', 'Trần Nguyễn Ngọc Trang', '2004-12-09', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0987666002', 'DCT0122B'),
('222010072', 'Phan Ngọc Trinh', '2004-03-08', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122B'),
('222010073', 'Nguyễn Thị Ngọc Trinh', '2004-11-13', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0816639022', 'DCT0122B'),
('222010074', 'Hà Mai Trinh', '2004-06-27', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010075', 'Đào Văn Trường', '2004-11-13', b'01', '1010 Đường Đồng Khởi, Quận 1\n', '0864792899', 'DCT0122A'),
('222010076', 'Lê Hồ Tuấn Trường', '2004-08-26', b'01', '6464 Đường Trần Quốc Toản, Quận 3\n', '0816639022', 'DCT0122A'),
('222010077', 'Cao Thanh Trường', '2004-10-10', b'01', '8888 Đường Võ Thị Sáu, Quận 5\n', '0776538800', 'DCT0122B'),
('222010078', 'Lê Sơn Trường', '2004-09-11', b'01', '1010 Đường Đồng Khởi, Quận 1\n', '0864792899', 'DCT0122B'),
('222010080', 'Lê Thanh Uyên', '2004-03-08', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122A'),
('222010081', 'Trương Thị Tân Uyên', '2004-08-26', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122A'),
('222010082', 'Nguyễn Phương Uyên', '2004-12-15', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0776538800', 'DCT0122A'),
('222010083', 'Mai Thị Tú Uyên', '2004-12-09', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0816639022', 'DCT0122A'),
('222010084', 'Hồ Trần Mỹ Uyên', '2004-11-13', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122A'),
('222010085', 'Ngô Dương Hồng Vân', '2004-03-08', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122B'),
('222010086', 'Nguyễn Ngọc Vân', '2004-12-09', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0987666002', 'DCT0122B'),
('222010087', 'Hà Thị Thanh Vân', '2004-09-11', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0816639022', 'DCT0122A'),
('222010088', 'Nguyễn Khắc Việt', '2004-06-27', b'01', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010089', 'Nguyễn Quốc Việt', '2004-03-08', b'01', '8888 Đường Võ Thị Sáu, Quận 5\n', '0987666002', 'DCT0122B'),
('222010090', 'Lê Trần Khánh Vy', '2004-06-27', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0864792899', 'DCT0122A'),
('222010091', 'Hà Tú Vy', '2004-08-26', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0816639022', 'DCT0122A'),
('222010092', 'Mai Ánh Vy', '2004-10-10', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122A'),
('222010093', 'Nguyễn Thị Ngọc Vy', '2004-08-26', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122B'),
('222010094', 'Lê Tường Vy', '2004-06-27', b'00', '60 Đường Trần Quốc Toản, Quận 3', '0987666002', 'DCT0122A'),
('222010095', 'Dương Ngọc Xuân', '2004-09-11', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0776538800', 'DCT0122A'),
('222010096', 'Hồ Thị Mỹ Xuân', '2004-03-08', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0864792899', 'DCT0122A'),
('222010097', 'Trương Thị Yên', '2004-10-10', b'00', '1010 Đường Đồng Khởi, Quận 1\n', '0987666002', 'DCT0122B'),
('222010098', 'Võ Ngọc Thanh Yến', '2004-08-26', b'00', '8888 Đường Võ Thị Sáu, Quận 5\n', '0816639022', 'DCT0122A'),
('222010099', 'Mai Như Ý', '2004-06-27', b'00', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0776538800', 'DCT0122A'),
('222010100', 'Võ Thị Như Ý', '2004-09-11', b'00', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122A');
--
-- Constraints for dumped tables
--

--
-- Constraints for table `account_gv`
--
ALTER TABLE `account_gv`
  ADD CONSTRAINT `account_gv_ibfk_1` FOREIGN KEY (`USERNAME`) REFERENCES `giangvien` (`MAGV`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `account_sv`
--
ALTER TABLE `account_sv`
  ADD CONSTRAINT `account_sv_ibfk_1` FOREIGN KEY (`USERNAME`) REFERENCES `sinhvien` (`MASV`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `bangdiem`
--
ALTER TABLE `bangdiem`
  ADD CONSTRAINT `bangdiem_ibfk_1` FOREIGN KEY (`MASV`) REFERENCES `sinhvien` (`MASV`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `chitietbangdiem`
--
ALTER TABLE `chitietbangdiem`
  ADD CONSTRAINT `chitietbangdiem_ibfk_1` FOREIGN KEY (`MABD`) REFERENCES `bangdiem` (`MABD`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `chitietbangdiem_ibfk_2` FOREIGN KEY (`MANHOM`) REFERENCES `nhommonhoc` (`MANHOM`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `dangkynhom`
--
ALTER TABLE `dangkynhom`
  ADD CONSTRAINT `dangkynhom_ibfk_1` FOREIGN KEY (`MANHOM`) REFERENCES `nhommonhoc` (`MANHOM`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `dangkynhom_ibfk_2` FOREIGN KEY (`MASV`) REFERENCES `sinhvien` (`MASV`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `giangvien`
--
ALTER TABLE `giangvien`
  ADD CONSTRAINT `giangvien_ibfk_1` FOREIGN KEY (`MAKHOA`) REFERENCES `khoa` (`MAKHOA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `lop`
--
ALTER TABLE `lop`
  ADD CONSTRAINT `lop_ibfk_1` FOREIGN KEY (`KHOA`) REFERENCES `khoa` (`MAKHOA`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `nhommonhoc`
--
ALTER TABLE `nhommonhoc`
  ADD CONSTRAINT `nhommonhoc_ibfk_1` FOREIGN KEY (`MAGV`) REFERENCES `giangvien` (`MAGV`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `nhommonhoc_ibfk_2` FOREIGN KEY (`MAMH`) REFERENCES `monhoc` (`MAMH`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sinhvien`
--
ALTER TABLE `sinhvien`
  ADD CONSTRAINT `sinhvien_ibfk_1` FOREIGN KEY (`LOP`) REFERENCES `lop` (`MALOP`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
