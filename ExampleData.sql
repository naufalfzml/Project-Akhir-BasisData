USE Database_Hotel

INSERT INTO KamarHotel (tipe_kamar, harga_kamar, nomor_kamar, status_kamar) VALUES
('standard', 300000.00, 'A1', 'booked'),
('deluxe', 750000.00, 'B1', 'booked'),
('suite', 900000.00, 'C1', 'booked'),
('standard', 300000.00, 'A2', 'booked'),
('suite', 900000.00, 'C2', 'booked'),
('deluxe', 750000.00, 'B2', 'booked'),
('standard', 300000.00, 'A3', 'booked'),
('suite', 900000.00, 'C3', 'booked'),
('deluxe', 750000.00, 'B3', 'booked'),
('suite', 900000.00, 'C4', 'booked'),
('suite', 900000.00, 'C5', 'booked'),
('deluxe', 750000.00, 'B4', 'booked'),
('standard', 300000.00, 'A4', 'booked'),
('standard', 300000.00, 'A5', 'booked'),
('deluxe', 750000.00, 'B5', 'booked'),
('meeting room', 1000000.00, 'D1', 'booked'),
('deluxe', 750000.00, 'B6', 'booked'),
('deluxe', 750000.00, 'B7', 'booked'),
('deluxe', 750000.00, 'B8', 'booked'),
('deluxe', 750000.00, 'B9', 'booked');


INSERT INTO TabelKaryawan (nama_karyawan, jabatan, hp_karyawan, alamat_karyawan, gaji) VALUES
('Jennifer Prima Sifabella', 'Resepsionis', '6285623148279', 'Jl. Dupak V', 4000000.00),
('Jovanka Orlin Pradipa', 'Chef', '6287829183023', 'Jl. Hayam Wuruk No. 17', 5200000.00),
('Laila Sasikirana Zahira', 'Chef', '6281000227332', 'Jl. Bhayangkara', 5200000.00),
('Andriel Arkana', 'Chef', '6287200093000', 'Jl. Pisang Ambon', 5200000.00),
('Brian Lukman Nugroho', 'Housekeeper', '6285289920019', 'Jl. Dringo No. 147', 3000000.00),
('Fatin Colleen Delisia', 'Resepsionis', '6285772001264', 'Jl. Rusak No. 98', 4000000.00),
('Gauri Anum Basimah', 'Housekeeper', '6287966111282', 'Jl. WR. Supratman III', 3000000.00),
('Luthfi Oemar', 'Housekeeper', '6285100028393', 'Jl. Mpok Nori No. 8', 3000000.00),
('Prataya Mahardika', 'Cleaning Service', '6287819000211', 'Jl. Agus Salim', 4600000.00),
('Rafa Fauzan', 'Cleaning Service', '6285117729980', 'Jl. Slamet Riyadi', 4600000.00),
('Cristiano Ronaldo', 'Housekeeper', '6282110095411', 'Jl. Ahmad Yani No. 3', 3000000.00),
('Lionel Messi', 'Housekeeper', '6281677729905', 'Jl. Goyang', 3000000.00),
('Kumis De Bruyne', 'Housekeeper', '6287816502124', 'Jl. Rejeki No. 7', 3000000.00),
('Imam Surya', 'Cleaning Service', '6287111092222', 'Jl. Plaosan IV', 4600000.00),
('Kaisar Nava', 'Cleaning Service', '6285100099922', 'Jl. Karonsih No. 15', 4600000.00);


INSERT INTO TamuHotel (nama_tamu, jenis_kelamin, alamat_tamu, hp_tamu, tanggal_lahir) VALUES
('Indra Kevin Filo', 'Laki-laki', 'Jl. Ahmad Yani', '6281234567890', '2003-11-13'),
('Prajana Zayan', 'Laki-laki', 'Jl. Gubeng', '6281122334455', '2004-05-12'),
('Alana Liora Gantari', 'Perempuan', 'Jl. Diponegoro', '6281398765432', '2005-09-12'),
('Farhan Cahya', 'Laki-laki', 'Jl. Kalianak', '6281566778899', '1998-02-11'),
('Sigit Ade Putra', 'Laki-laki', 'Jl. Sidorame', '6281723456789', '2001-04-13'),
('Afira Rainey Keysa', 'Perempuan', 'Jl. Hayam Wuruk', '6281112233444', '2002-11-04'),
('Naufal Daran', 'Laki-laki', 'Jl. Goyang', '6281955667788', '2000-12-09'),
('Citra Liala Zanna', 'Perempuan', 'Jl. Kranggan', '6281911112222', '2002-12-03'),
('Aisha Aileen Nathania', 'Perempuan', 'Jl. Sumberan', '6281333445566', '2001-07-23'),
('Dimas Rafan', 'Laki-laki', 'Jl. Wonoyu', '6281376543210', '2001-09-04'),
('Zinan Prayoga Aditama', 'Laki-laki', 'Jl. Deles', '6281599887766', '2005-10-13'),
('Riordan Kevin', 'Laki-laki', 'Jl. Kalisari', '6281575443322', '2005-11-13'),
('Dalila Sena Gawrita', 'Perempuan', 'Jl. Manyar', '6281678123456', '2003-03-01'),
('Eliana Askana', 'Perempuan', 'Jl. Airlangga', '6281922334455', '2003-04-01'),
('Indira Nuria', 'Perempuan', 'Jl. Keputran', '6281299887766', '1999-08-12'),
('Idul Fitri', 'Perempuan', 'Jl Ir Sutami no 36, Jebres, Surakarta', '628123456789', '1994-04-21'),
('Idul Adha', 'Laki-laki', 'Jl Ir Tentara pelajar no 36, Mojosongo, Surakarta', '6281133335555', '1990-10-28');


INSERT INTO LayananTambahan (id_karyawan, nama_layanan, biaya_layanan)
VALUES
    (202212, 'Extra Bed', 75000),
    (202215, 'Room Service', 50000),
    (202213, 'Extra Pillow', 30000),
    (202202, 'Paket Makanan', 100000);

INSERT INTO ReservasiKamar (id_service, id_tamu, id_kamar, jumlah_layanan, tanggal_check_in, tanggal_check_out, tanggal_reservasi, tanggal_pembayaran, metode_pembayaran, total_harga)
VALUES
(786001, 30301, 10001, 1, '2024-07-11', '2024-07-12', '2024-07-10', '2024-07-12', 'cash', 375000.00),
(786003, 30302, 10002, 1, '2024-03-25', '2024-03-26', '2024-03-21', '2024-03-26', 'cash', 800000.00),
(786001, 30303, 10003, 1, '2024-03-03', '2024-03-04', '2024-03-01', '2024-03-04', 'debit', 975000.00),
(786002, 30304, 10004, 1, '2024-06-13', '2024-06-15', '2024-06-10', '2024-06-15', 'cash', 350000.00),
(786004, 30305, 10005, 1, '2024-03-02', '2024-03-03', '2024-03-01', '2024-03-03', 'debit', 1000000.00),
(786001, 30306, 10006, 1, '2024-04-13', '2024-04-14', '2024-04-12', '2024-04-14', 'debit', 825000.00),
(786003, 30307, 10007, 1, '2024-04-07', '2024-04-08', '2024-04-05', '2024-04-08', 'debit', 330000.00),
(786003, 30308, 10008, 1, '2024-06-29', '2024-06-30', '2024-06-27', '2024-06-30', 'debit', 930000.00),
(786001, 30309, 10009, 1, '2024-05-13', '2024-05-15', '2024-05-11', '2024-05-15', 'cash', 825000.00),
(786004, 30310, 10010, 1, '2024-05-30', '2024-05-31', '2024-05-27', '2024-05-31', 'debit', 1000000.00),
(786004, 30311, 10011, 1, '2024-07-12', '2024-07-13', '2024-07-10', '2024-07-13', 'cash', 1000000.00),
(786001, 30312, 10012, 1, '2024-04-09', '2024-04-11', '2024-03-29', '2024-04-11', 'debit', 825000.00),
(786002, 30313, 10013, 1, '2024-04-01', '2024-04-02', '2024-02-29', '2024-04-02', 'cash', 350000.00),
(786001, 30314, 10014, 1, '2024-06-08', '2024-06-09', '2024-06-06', '2024-06-09', 'debit', 375000.00),
(786001, 30315, 10015, 1, '2024-05-01', '2024-05-03', '2024-04-29', '2024-05-03', 'debit', 825000.00),
(786004, 30316, 10016, 25, '2024-05-20', '2024-05-21', '2024-05-03', '2024-05-21', 'cash', 8500000.00),
(NULL, 30317, 10017, 0, '2024-06-05', '2024-06-06', '2024-05-30', '2024-06-06', 'cash', 750000.00),
(NULL, 30317, 10018, 0, '2024-06-05', '2024-06-06', '2024-05-30', '2024-06-06', 'cash', 750000.00),
(NULL, 30317, 10019, 0, '2024-06-05', '2024-06-06', '2024-05-30', '2024-06-06', 'cash', 750000.00),
(NULL, 30317, 10020, 0, '2024-06-05', '2024-06-06', '2024-05-30', '2024-06-06', 'cash', 750000.00);

-- Insert data into PivotFG (Many-to-Many relationship)
DECLARE @fgId INT = 1, @gfId INT = 1;
WHILE @fgId <= 10
BEGIN
    WHILE @gfId <= 10
    BEGIN
        INSERT INTO PivotFG (id_fg, id_gf)
        VALUES (@fgId, @gfId);
        SET @gfId = @gfId + 1;
    END;
    SET @fgId = @fgId + 1;
    SET @gfId = 1;
END;
