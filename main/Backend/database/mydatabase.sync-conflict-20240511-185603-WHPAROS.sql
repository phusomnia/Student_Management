CREATE DATABASE DULIEU;
USE DULIEU;
DROP DATABASE DULIEU;

CREATE TABLE ACCOUNT(
	USERNAME VARCHAR(10),
    PASS VARCHAR(10),
    PRIMARY KEY (USERNAME)
);

CREATE TABLE BAITHI(
	MAMH VARCHAR(10),
    MASV VARCHAR(10),
    SOPHACH VARCHAR(10),
    TINHTRANG VARCHAR(10)
);

CREATE TABLE SINHVIEN(
	MASV VARCHAR(10) NOT NULL,
	HOTENSV VARCHAR(50) NOT NULL,
    NGSINH DATE NOT NULL,
    GTINH VARCHAR(5) NOT NULL,
    DCHI VARCHAR(250) NOT NULL,
    SDT VARCHAR(12) NOT NULL,
    LOP VARCHAR(10) NOT NULL,
    PRIMARY KEY (MASV)
);

CREATE TABLE LOP(
	MALOP VARCHAR(10) NOT NULL,
	TENLOP VARCHAR(50) NOT NULL,
    KHOA VARCHAR(50) NOT NULL, # FK
    KHOAHOC VARCHAR(10) NOT NULL,
    HEDAOTAO VARCHAR(100) NOT NULL,
    PRIMARY KEY (MALOP)
);

CREATE TABLE KHOA(
	MAKHOA VARCHAR(10) NOT NULL,
    TENKHOA VARCHAR(50) NOT NULL,
    SDT VARCHAR(12) NOT NULL,
	PHONG VARCHAR(10) NOT NULL,
    TRGKHOA VARCHAR(10) NOT NULL,
    PRIMARY KEY (MAKHOA)
);

CREATE TABLE GIANGVIEN(
	MAGV VARCHAR(10) NOT NULL,
    HOTENGV VARCHAR(50) NOT NULL,
    NGSINH DATE NOT NULL,
    GTINH VARCHAR(5) NOT NULL,
    KHOA VARCHAR(10) NOT NULL,
    PRIMARY KEY(MAGV)
);

CREATE TABLE NHOMMONHOC(
	MANHOM VARCHAR(10) NOT NULL,
    GV VARCHAR(10) NOT NULL, 
    MH VARCHAR(10) NOT NULL,
    TENNHOM VARCHAR(150) NOT NULL,
    PRIMARY KEY (MANHOM)
);

CREATE TABLE DANGKYNHOM(
	SV VARCHAR(10) NOT NULL,
    NHOM VARCHAR(10) NOT NULL
);

CREATE TABLE MONHOC(
	MAMH VARCHAR(10) NOT NULL,
    TENMH VARCHAR(50) NOT NULL,
    SOTC INT NOT NULL,
    PRIMARY KEY (MAMH)
);

CREATE TABLE CHITIETBANGDIEM(
	BD VARCHAR(10) NOT NULL,
    NHOM VARCHAR(10) NOT NULL, 
    DIEM_QT VARCHAR(10), 
    HESO_QT DECIMAL(3,2) NOT NULL,
    DIEMTHI DECIMAL(4,2),
    HESO_THI DECIMAL(3,2) NOT NULL,
    DIEMTB_HE10 DECIMAL(4,2),
    DIEMTB_HE4 DECIMAL(4,2),
    XEPLOAI VARCHAR(10),
    TINHTRANG VARCHAR(10)
);

CREATE TABLE BANGDIEM (
    MABD VARCHAR(10) NOT NULL,
    HOCKY VARCHAR(10) NOT NULL,
    NAMHOC VARCHAR(4) NOT NULL,
    DIEMTK_HE4 DECIMAL(3,2),
    DIEMTK_HE10 DECIMAL(3,2),
    XEPLOAIHK VARCHAR(10),
    DIEMTB_TL DECIMAL(3,2) NOT NULL,
    TONGTINCHI INT NOT NULL,
    SV VARCHAR(10) NOT NULL,
    PRIMARY KEY (MABD)
);

INSERT INTO ACCOUNT (USERNAME, PASS) VALUES
('222010001', '123456'),
('GV01001', '123456'),
('GV01002', '123456'),
('ADMIN', 'admin');

## DATASET
INSERT INTO SINHVIEN (MASV, HOTENSV, NGSINH, GTINH, DCHI, SDT, LOP) VALUES 
('222010001', 'Ngô Trí Hoàng An', '2004-12-04', 'Nam', '106106 Đường Lê Hồng Phong, Quận 5\n', '0816639022', 'DCT0122B'),
('222010002', 'Phạm Hoàng Anh', '2004-04-25', 'Nam', '8080 Đường Huỳnh Mẫn Đạt, Quận 5\n', '0864792899', 'DCT0122A'),
('222010003', 'Trần Thế Huy', '2004-05-25', 'Nam', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0864792899', 'DCT0122A'),
('222010004', 'Trần Thế An', '2004-01-12', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0776538800', 'DCT0122A'),
('222010005', 'Đỗ Lê Trí Ân', '2004-01-17', 'Nam', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0816639022', 'DCT0122B'),
('222010006', 'Trương Thế Bảo', '2004-05-17', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010007', 'Nguyễn Hoàng Bách', '2004-05-03', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122B'),
('222010008', 'Lê Thiện Chí', '2004-01-05', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1', '0864792899', 'DCT0122A'),
('222010009', 'Ngô Gia Cường', '2004-01-02', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122A'),
('222010010', 'Lê Ngọc Quỳnh Chi', '2004-05-28', 'Nữ', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0816639022', 'DCT0122A'),
('222010011', 'Hồ Lê Minh Chi', '2004-01-26', 'Nữ', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010012', 'Hà Duy', '2004-05-05', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0776538800', 'DCT0122A'),
('222010013', 'Nguyễn Phúc Duy', '2004-01-24', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122B'),
('222010014', 'Nguyễn Văn Đạt', '2004-01-21', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122B'),
('222010015', 'Phạm Hoàng Đạt', '2004-02-02', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010016', 'Nguyễn Nhật Đông', '2004-05-06', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010017', 'Hà Thu Giang', '2004-05-20', 'Nữ', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122B'),
('222010018', 'Lê Thị Thu Hà', '2004-05-27', 'Nữ', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0776538800', 'DCT0122B'),
('222010019', 'Trần Thị Ánh Hạ', '2004-02-07', 'Nữ', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0816639022', 'DCT0122A'),
('222010020', 'Vũ Văn Hà Huy', '2004-02-09', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122B'),
('222010021', 'Nguyễn Quỳnh Như', '2004-04-18', 'Nữ', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010022', 'Phạm Minh Huy', '2004-02-11', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122B'),
('222010023', 'Nguyễn Hồ Chí Hùng', '2004-02-13', 'Nam', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010024', 'Lâm văn Hùng', '2004-02-18', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122B'),
('222010025', 'Trương Gia Huệ', '2004-02-25', 'Nữ', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010026', 'Nguyễn Thị Thu Huệ', '2004-02-28', 'Nữ', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0816639022', 'DCT0122A'),
('222010027', 'Vũ Tiến Lợi', '2004-02-21', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010028', 'Trương Nguyễn Tấn Lộc', '2004-03-15', 'Nam', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010029', 'Hàng Quang Khải', '2004-03-11', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122A'),
('222010030', 'Hồ Khải', '2004-03-17', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122A'),
('222010031', 'Trương Tấn Khôi', '2004-03-19', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010032', 'Hà Lê Vũ Khôi', '2004-03-29', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0816639022', 'DCT0122B'),
('222010033', 'Nguyến Bảo Minh', '2004-03-22', 'Nam', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010034', 'Trương Vũ Văn Minh', '2004-03-26', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0987666002', 'DCT0122A'),
('222010035', 'Hồ Khải Minh', '2004-03-28', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010036', 'Hà Thị Ánh My', '2004-03-12', 'Nữ', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122A'),
('222010037', 'Nguyễn Ngọc My', '2004-03-04', 'Nữ', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0816639022', 'DCT0122A'),
('222010038', 'Vũ Tuấn Ngọc', '2004-03-07', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0864792899', 'DCT0122A'),
('222010039', 'Trần Lê Bảo Ngọc', '2004-04-11', 'Nữ', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010040', 'Hồ Thị Tuyết Như', '2004-04-16', 'Nữ', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0816639022', 'DCT0122A'),
('222010042', 'Nguyễn Bảo Nhi', '2004-04-29', 'Nữ', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122A'),
('222010043', 'Hồ Trần Diệu Nhi', '2004-04-20', 'Nữ', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010044', 'Nguyễn Thanh Phương', '2004-04-22', 'Nữ', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0987666002', 'DCT0122A'),
('222010045', 'Trần Gia Phú', '2004-04-26', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0776538800', 'DCT0122B'),
('222010046', 'Nguyễn Lê Hoàng Phúc', '2004-04-05', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0987666002', 'DCT0122B'),
('222010047', 'Trần Thiện Phúc', '2004-04-03', 'Nam', '4646 Đường Hồ Huấn Nghiệp, Quận 1\n', '0864792899', 'DCT0122A'),
('222010048', 'Hà Văn Phúc', '2004-05-12', 'Nam', '4242 Đường Nguyễn An Ninh, Quận 1\n', '0776538800', 'DCT0122A'),
('222010049', 'Lê Minh Quang', '2004-05-19', 'Nam', '100100 Đường Đinh Tiên Hoàng, Quận 5\n', '0987666002', 'DCT0122A'),
('222010050', 'Nguyễn Ngọc Quang', '2004-05-14', 'Nam', '6868 Đường Cách Mạng Tháng Tám, Quận 3\n', '0816639022', 'DCT0122A'),
('222010052', 'Trương Ngọc Diễm Quỳnh', '2004-06-27', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0776538800', 'DCT0122B'),
('222010053', 'Ngô Hồng Sơn', '2004-08-26', 'Nam', '6464 Đường Trần Quốc Toản, Quận 3\n', '0816639022', 'DCT0122A'),
('222010054', 'Phạm Duy Sơn', '2004-09-11', 'Nam', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122A'),
('222010055', 'Vũ Thanh Sang', '2004-03-08', 'Nam', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010056', 'Trịnh Sang', '2004-09-11', 'Nam', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0816639022', 'DCT0122B'),
('222010057', 'Cao Thanh Tú', '2004-06-27', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0987666002', 'DCT0122B'),
('222010058', 'Hoàng Phan Duy Tú', '2004-09-11', 'Nam', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010059', 'Đặng Ngọc Tú', '2004-08-26', 'Nam', '1010 Đường Đồng Khởi, Quận 1\n', '0816639022', 'DCT0122B'),
('222010060', 'Vũ Ngọc Thanh Thu', '2004-10-10', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122B'),
('222010061', 'Trương Mỹ Thu', '2004-06-27', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122A'),
('222010062', 'Nguyễn Thị Minh Thu', '2004-08-26', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122B'),
('222010063', 'Hồ Thị Minh Thư', '2004-09-11', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0864792899', 'DCT0122A'),
('222010064', 'Ngô Anh Thư', '2004-11-13', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010065', 'Nguyễn Thị Ánh Thư', '2004-03-08', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0987666002', 'DCT0122B'),
('222010066', 'Nguyễn Đình Thông', '2004-08-26', 'Nam', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122A'),
('222010067', 'Hồ Viết Thông', '2004-11-13', 'Nam', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0816639022', 'DCT0122B'),
('222010068', 'Lê Hồ Mỹ Trang', '2004-10-10', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122B'),
('222010069', 'Vũ Khánh Trang', '2004-06-27', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122B'),
('222010070', 'Nguyễn Thị Phương Trang', '2004-08-26', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122B'),
('222010071', 'Trần Nguyễn Ngọc Trang', '2004-12-09', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0987666002', 'DCT0122B'),
('222010072', 'Phan Ngọc Trinh', '2004-03-08', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122B'),
('222010073', 'Nguyễn Thị Ngọc Trinh', '2004-11-13', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0816639022', 'DCT0122B'),
('222010074', 'Hà Mai Trinh', '2004-06-27', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010075', 'Đào Văn Trường', '2004-11-13', 'Nam', '1010 Đường Đồng Khởi, Quận 1\n', '0864792899', 'DCT0122A'),
('222010076', 'Lê Hồ Tuấn Trường', '2004-08-26', 'Nam', '6464 Đường Trần Quốc Toản, Quận 3\n', '0816639022', 'DCT0122A'),
('222010077', 'Cao Thanh Trường', '2004-10-10', 'Nam', '8888 Đường Võ Thị Sáu, Quận 5\n', '0776538800', 'DCT0122B'),
('222010078', 'Lê Sơn Trường', '2004-09-11', 'Nam', '1010 Đường Đồng Khởi, Quận 1\n', '0864792899', 'DCT0122B'),
('222010080', 'Lê Thanh Uyên', '2004-03-08', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122A'),
('222010081', 'Trương Thị Tân Uyên', '2004-08-26', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122A'),
('222010082', 'Nguyễn Phương Uyên', '2004-12-15', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0776538800', 'DCT0122A'),
('222010083', 'Mai Thị Tú Uyên', '2004-12-09', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0816639022', 'DCT0122A'),
('222010084', 'Hồ Trần Mỹ Uyên', '2004-11-13', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122A'),
('222010085', 'Ngô Dương Hồng Vân', '2004-03-08', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0864792899', 'DCT0122B'),
('222010086', 'Nguyễn Ngọc Vân', '2004-12-09', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0987666002', 'DCT0122B'),
('222010087', 'Hà Thị Thanh Vân', '2004-09-11', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0816639022', 'DCT0122A'),
('222010088', 'Nguyễn Khắc Việt', '2004-06-27', 'Nam', '6464 Đường Trần Quốc Toản, Quận 3\n', '0776538800', 'DCT0122B'),
('222010089', 'Nguyễn Quốc Việt', '2004-03-08', 'Nam', '8888 Đường Võ Thị Sáu, Quận 5\n', '0987666002', 'DCT0122B'),
('222010090', 'Lê Trần Khánh Vy', '2004-06-27', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0864792899', 'DCT0122A'),
('222010091', 'Hà Tú Vy', '2004-08-26', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0816639022', 'DCT0122A'),
('222010092', 'Mai Ánh Vy', '2004-10-10', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0776538800', 'DCT0122A'),
('222010093', 'Nguyễn Thị Ngọc Vy', '2004-08-26', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122B'),
('222010094', 'Lê Tường Vy', '2004-06-27', 'Nữ', '60 Đường Trần Quốc Toản, Quận 3', '0987666002', 'DCT0122A'),
('222010095', 'Dương Ngọc Xuân', '2004-09-11', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0776538800', 'DCT0122A'),
('222010096', 'Hồ Thị Mỹ Xuân', '2004-03-08', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0864792899', 'DCT0122A'),
('222010097', 'Trương Thị Yên', '2004-10-10', 'Nữ', '1010 Đường Đồng Khởi, Quận 1\n', '0987666002', 'DCT0122B'),
('222010098', 'Võ Ngọc Thanh Yến', '2004-08-26', 'Nữ', '8888 Đường Võ Thị Sáu, Quận 5\n', '0816639022', 'DCT0122A'),
('222010099', 'Mai Như Ý', '2004-06-27', 'Nữ', '6262 Đường Lê Văn Sỹ, Quận 3\n', '0776538800', 'DCT0122A'),
('222010100', 'Võ Thị Như Ý', '2004-09-11', 'Nữ', '6464 Đường Trần Quốc Toản, Quận 3\n', '0987666002', 'DCT0122A');

INSERT INTO LOP (MALOP, TENLOP, KHOA, KHOAHOC, HEDAOTAO) VALUES 
('DCT0122A', 'Công nghệ thông tin - Lớp A', 'CNTT01', 'K22', 'Đại Học Chính Quy'),
('DCT0122B', 'Công nghệ thông tin - Lớp B', 'CNTT01', 'K22', 'Đại Học Chính Quy');

INSERT INTO KHOA (MAKHOA, TENKHOA, SDT, PHONG, TRGKHOA) VALUES 
('CNTT01', 'Công nghệ thông tin', '0876555829', 'A.A101', 'GV01001'),
('LUAT02', 'Luật', '0978645727', 'D.A101', 'GV02001'),
('NN03', 'Ngoại ngữ', '0987999634', 'D.A102', 'GV03001');

INSERT INTO GIANGVIEN (MAGV, HOTENGV, NGSINH, GTINH, KHOA) VALUES
('GV01001', 'Trương Thanh Tùng', '1986-12-03', 'Nam', 'CNTT01'),
('GV01002', 'Hồ Thanh Việt', '1992-05-27', 'Nam', 'CNTT01'),
('GV01003', 'Nguyễn Thị Hương', '1989-09-03', 'Nữ', 'CNTT01'),
('GV01004', 'Nguyến Thanh Thuận', '1972-05-03', 'Nữ', 'CNTT01'),
('GV02001', 'Phan Duy Khương', '1988-08-03', 'Nam', 'CNTT01'),
('GV02002', 'Trần Mỹ Lan', '1993-05-11', 'Nữ', 'CNTT01'),
('GV02003', 'Trần Hồ Khải ', '1981-01-03', 'Nam', 'CNTT01'),
('GV02004', 'Hồ Thị Mỹ Ngọc', '1991-05-03', 'Nữ', 'CNTT01'),
('GV03001', 'Nguyễn Phú Trọng Nam', '1977-03-03', 'Nam', 'CNTT01'),
('GV03002', 'TLê Thị Thanh Thảo', '1986-05-01', 'Nữ', 'CNTT01'),
('GV03003', 'Nguyễn Thanh Việt', '1974-11-03', 'Nam', 'CNTT01'),
('GV03004', 'Phan Tuấn An', '1986-05-20', 'Nam', 'CNTT01');

INSERT INTO NHOMMONHOC (MANHOM, GV, MH, TENNHOM) VALUES
('N010101', 'GV01001', '2010001', 'Cơ sở trí tuệ nhân tạo - Nhóm 1'),
('N010102', 'GV01002', '2010001', 'Cơ sở trí tuệ nhân tạo - Nhóm 2'),
('N010201', 'GV01001', '2010002', 'Ngôn ngữ lập trình Python - Nhóm 1'),
('N010202', 'GV01002', '2010002', 'Ngôn ngữ lập trình Python - Nhóm 2'),
('N010301', 'GV01003', '2010003', 'Ngôn Ngữ lập trình Java - Nhóm 1'),
('N010401', 'GV01004', '2010004', 'Lập trình Web và ứng dụng - Nhóm 1');

INSERT INTO DANGKYNHOM (SV, NHOM) VALUES
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

INSERT INTO MONHOC (MAMH, TENMH, SOTC) VALUES
('2010001', 'Cơ sở trí tuệ nhân tạo ', 4),
('2010002', 'Ngôn ngữ lập trình Python', 4),
('2010003', 'Ngôn ngữ lập trình Java', 4),
('2010004', 'Lập trình Web và ứng dụng', 4),
('2010005', 'Xác xuất thống kê ', 4),
('2010006', 'Hệ điều hành ', 4);

INSERT INTO CHITIETBANGDIEM (BD, NHOM, DIEM_QT, HESO_QT, DIEMTHI, HESO_THI, DIEMTB_HE10, DIEMTB_HE4, XEPLOAI, TINHTRANG) VALUES
('D22201001', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201001', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201001', 'N010301', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201001', 'N010401', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201002', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201002', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201003', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201003', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201004', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201004', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201005', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201005', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201006', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201006', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201007', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201007', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201008', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 2.00, 'C', NULL),
('D22201008', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201009', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201009', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201010', 'N010101', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201010', 'N010201', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, NULL, NULL),
('D22201011', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201012', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201013', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 2.00, 'C', NULL),
('D22201014', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201015', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 3.00, 'B', NULL),
('D22201016', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201017', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'A', NULL),
('D22201018', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 1.00, 'D', NULL),
('D22201019', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'F', NULL),
('D22201020', 'N010102', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 'F', NULL);


INSERT INTO BANGDIEM (MABD, HOCKY, NAMHOC, DIEMTK_HE4, DIEMTK_HE10, XEPLOAIHK, DIEMTB_TL, TONGTINCHI, SV) VALUES
('D22201001', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010001'),
('D22201002', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010002'),
('D22201003', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010003'),
('D22201004', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010004'),
('D22201005', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010005'),
('D22201006', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010006'),
('D22201007', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010007'),
('D22201008', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010008'),
('D22201009', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010009'),
('D22201010', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010010'),
('D22201011', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010011'),
('D22201012', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010012'),
('D22201013', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010013'),
('D22201014', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010014'),
('D22201015', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010015'),
('D22201016', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010016'),
('D22201017', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010017'),
('D22201018', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010018'),
('D22201019', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010019'),
('D22201020', '1', '2024', 0.00, 0.00, NULL, 0.00, 0, '222010020');

