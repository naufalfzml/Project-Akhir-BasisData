CREATE DATABASE Database_Hotel

USE Database_Hotel

SELECT @@NAUFAL\SQLEXPRESS

-CREATE TABLE KamarHotel (
    id_kamar INT NOT NULL PRIMARY KEY IDENTITY(10001, 1),
    tipe_kamar VARCHAR(50) NOT NULL,
    harga_kamar DECIMAL(10, 2) NOT NULL,
    nomor_kamar VARCHAR(10) UNIQUE NOT NULL,
    status_kamar VARCHAR(20) NOT NULL
);

CREATE TABLE TabelKaryawan (
    id_karyawan INT NOT NULL PRIMARY KEY IDENTITY(202201, 1),
    nama_karyawan VARCHAR(100) NOT NULL,
    jabatan VARCHAR(50) NOT NULL,
    hp_karyawan VARCHAR(20) UNIQUE NOT NULL,
    alamat_karyawan VARCHAR(100) NOT NULL,
    gaji DECIMAL(10, 2) NOT NULL
);

CREATE TABLE TamuHotel (
    id_tamu INT NOT NULL PRIMARY KEY IDENTITY(30301, 1),
    nama_tamu VARCHAR(100) NOT NULL,
    jenis_kelamin VARCHAR(10) NOT NULL,
    alamat_tamu VARCHAR(100) NOT NULL,
    hp_tamu VARCHAR(20) UNIQUE NOT NULL,
    tanggal_lahir DATE NOT NULL
);

CREATE TABLE LayananTambahan (
    id_service INT NOT NULL PRIMARY KEY IDENTITY(786001, 1),
    id_karyawan INT NOT NULL,
    nama_layanan VARCHAR(50) NOT NULL,
    biaya_layanan DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_karyawan) REFERENCES TabelKaryawan(id_karyawan)
);

CREATE TABLE ReservasiKamar (
    id_reservasi INT NOT NULL PRIMARY KEY IDENTITY(47401, 1),
    id_service INT,
    id_tamu INT NOT NULL,
    id_kamar INT NOT NULL,
    jumlah_layanan INT DEFAULT 0 CHECK (jumlah_layanan >= 0),
    tanggal_check_in DATE NOT NULL,
    tanggal_check_out DATE NOT NULL,
    tanggal_reservasi DATE NOT NULL,
    tanggal_pembayaran DATE NOT NULL,
    metode_pembayaran VARCHAR(50) NOT NULL,
    total_harga DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_service) REFERENCES LayananTambahan(id_service),
    FOREIGN KEY (id_tamu) REFERENCES TamuHotel(id_tamu),
    FOREIGN KEY (id_kamar) REFERENCES KamarHotel(id_kamar)
);

CREATE TABLE Reservasi_Layanan (
    id_reservasi INT NOT NULL,
    id_service INT NOT NULL,
    PRIMARY KEY (id_reservasi, id_service),
    FOREIGN KEY (id_reservasi) REFERENCES ReservasiKamar(id_reservasi),
    FOREIGN KEY (id_service) REFERENCES LayananTambahan(id_service)
);