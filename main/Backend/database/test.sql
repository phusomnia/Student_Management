SELECT DISTINCT GV.MAGV, MH.MAMH, K.MAKHOA, MH.SOTC, NMH.MANHOM, SV.MASV, SV.HOTEN , CTBD.* , BD.*
FROM GIANGVIEN GV
JOIN KHOA K ON GV.KHOA = K.MAKHOA
JOIN LOP L ON L.KHOA = K.MAKHOA
JOIN NHOMMONHOC NMH ON NMH.GV = GV.MAGV
JOIN CHITIETBANGDIEM CTBD ON CTBD.MANHOM = NMH.MANHOM 
JOIN BANGDIEM BD ON CTBD.BD = BD.MABD
JOIN DANGKYNHOM DKN ON DKN.NHOM = NMH.MANHOM
JOIN SINHVIEN SV ON DKN.SV = SV.MASV AND BD.MASV = SV.MASV
JOIN MONHOC MH ON NMH.MH = MH.MAMH
WHERE
MH.MAMH LIKE '2010002'
AND NMH.MANHOM LIKE 'N010201'
AND SV.MASV LIKE '222010001';

SELECT DISTINCT CTBD.*
FROM CHITIETBANGDIEM CTBD
JOIN BANGDIEM BD ON CTBD.BD = BD.MABD
JOIN SINHVIEN SV ON SV.MASV = BD.MASV
JOIN NHOMMONHOC NMH ON NMH.MANHOM = CTBD.MANHOM
JOIN MONHOC MH ON NMH.MH = MH.MAMH
JOIN GIANGVIEN GV ON GV.MAGV = NMH.GV
JOIN KHOA K ON GV.KHOA = K.MAKHOA
JOIN LOP L ON L.KHOA = K.MAKHOA
JOIN DANGKYNHOM DKN ON DKN.NHOM = NMH.MANHOM
WHERE -- GV.MAGV =  '' AND
MH.MAMH = '2010002'
AND CTBD.MANHOM = 'N010201'
AND SV.MASV = '222010001';



UPDATE CHITIETBANGDIEM CTBD
JOIN BANGDIEM BD ON CTBD.BD = BD.MABD
JOIN SINHVIEN SV ON SV.MASV = BD.MASV
JOIN NHOMMONHOC NMH ON NMH.MANHOM = CTBD.MANHOM
JOIN MONHOC MH ON NMH.MH = MH.MAMH
JOIN GIANGVIEN GV ON GV.MAGV = NMH.GV
JOIN KHOA K ON GV.KHOA = K.MAKHOA
JOIN LOP L ON L.KHOA = K.MAKHOA
JOIN DANGKYNHOM DKN ON DKN.NHOM = NMH.MANHOM
SET 
    CTBD.DIEM_QT = '10',
    CTBD.HESO_QT = '0.5',
    CTBD.DIEMTHI = '10',
    CTBD.HESO_THI = '0.5',
    CTBD.DIEMTB_HE10 = ('10' * '0.5') + ('10' * '0.5')
WHERE 
    MH.MAMH = '2010002'
    AND CTBD.MANHOM = 'N010201'
    AND SV.MASV = '222010001';
    
SELECT *
FROM ACCOUNT
WHERE USERNAME = '222010001';

SELECT CTBD.DIEMTB_HE10 
FROM BANGDIEM BD, CHITIETBANGDIEM CTBD 
WHERE BD.MASV = '222010001' AND BD.MABD = CTBD.BD;

SELECT sinhvien.MASV, sinhvien.HOTEN, sinhvien.NGSINH, sinhvien.GTINH, sinhvien.SDT, sinhvien.DCHI, sinhvien.LOP, khoa.TENKHOA
from sinhvien, lop, khoa
where sinhvien.LOP = lop.MALOP and lop.KHOA = khoa.MAKHOA and MASV = '222010001';

SELECT K.*
FROM KHOA K
WHERE K.TRGKHOA = 'GV01001';

SELECT *
FROM ACCOUNT;

SELECT *
FROM SINHVIEN SV, BANGDIEM BD
WHERE SV.MASV = '222010001' AND BD.MASV = '222010001'






