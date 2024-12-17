USE Database_Hotel
CREATE TRIGGER tr_update_room_status
ON ReservasiKamar
AFTER INSERT
AS
BEGIN
    DECLARE @id_kamar INT;
	DECLARE @tanggal_checkin DATE;
    DECLARE @tanggal_sekarang DATE;

    -- Mendapatkan id_kamar dan tanggal c dari reservasi yang baru
    SELECT @id_kamar = id_kamar, @tanggal_checkin = tanggal_check_in FROM INSERTED;

    -- Mendapatkan tanggal sekarang
    SET @tanggal_sekarang = GETDATE();

    IF @tanggal_checkin >= @tanggal_sekarang
    BEGIN
        -- Mengupdate status kamar menjadi 'Tidak Tersedia'
        UPDATE KamarHotel
        SET status_kamar = 'Booked'
        WHERE id_kamar = @id_kamar;
    END
END;

CREATE TRIGGER tr_update_status_kamar
ON ReservasiKamar
AFTER UPDATE
AS
BEGIN
    DECLARE @id_kamar INT;
    DECLARE @tanggal_checkout DATE;
    DECLARE @tanggal_sekarang DATE;

    -- Mendapatkan id_kamar dan tanggal_checkout dari baris yang diupdate
    SELECT @id_kamar = id_kamar, @tanggal_checkout = tanggal_check_out FROM INSERTED;

    -- Mendapatkan tanggal sekarang
    SET @tanggal_sekarang = GETDATE();

    -- Jika tanggal checkout sudah lewat dan status kamar belum diubah
    IF @tanggal_checkout < @tanggal_sekarang
    BEGIN
        -- Memperbarui status kamar menjadi 'Not Booked'
        UPDATE KamarHotel
        SET status_kamar = 'Not Booked'
        WHERE id_kamar = @id_kamar;
    END
END;