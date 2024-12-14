from flask import Blueprint, render_template, redirect, url_for, request, flash
from connect import create_connection
from datetime import date, datetime

# Create a blueprint for modular routing
routesReservasiKamar = Blueprint('routesReservasiKamar', __name__)

@routesReservasiKamar.route('/')
def index():
    return render_template('home.html')

@routesReservasiKamar.route('/tableReservasiKamar')
def ReservasiKamar():
    # Get the current page number from the query string (default to page 1)
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of items per page
    
    # Calculate the starting row for the query (offset)
    offset = (page - 1) * per_page
    
    # Get a connection to the database
    conn = create_connection()
    
    if conn:
        # Create a cursor from the connection
        cursor = conn.cursor()
        
        # Execute a query with pagination using OFFSET and FETCH NEXT
        cursor.execute('''
            SELECT * FROM ReservasiKamar
            ORDER BY id_reservasi  
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
        ''', (offset, per_page))

        # cursor.execute('SELECT * FROM LayananTambahan')
        
        # Fetch the results
        table = cursor.fetchall()
        
        # Get the total count of rows to calculate the number of pages
        cursor.execute('SELECT COUNT(*) FROM ReservasiKamar')
        total_count = cursor.fetchone()[0]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Calculate total number of pages
        total_pages = (total_count + per_page - 1) // per_page
        
        # Pass the results, total pages, and current page to the template
        return render_template('tableReservasiKamar.html', table=table, total_pages=total_pages, current_page=page)
    else:
        return render_template('tableReservasiKamar.html', table=None)

@routesReservasiKamar.route('/tableReservasiKamar/create', methods=['GET', 'POST'])
def create_ReservasiKamar():
    # Handle the form submission when the method is POST
    if request.method == 'POST':
        # properti input digunakan disini
        id_serviceReservasi = request.form['id_serviceReservasi']
        id_tamuReservasi = request.form['id_tamuReservasi']
        id_kamarReservasi = request.form['id_kamarReservasi']
        jml_layananReservasi = int(request.form['jml_layananReservasi'])
        tanggal_check_in = request.form['tgl_checkInReservasi']
        tanggal_check_out = request.form['tgl_checkOutReservasi']
        tanggal_pembayaran = request.form['tgl_bayarReservasi']
        metode_pembayaranReservasi = request.form['metode_bayarReservasi']

        today_date = date.today().isoformat()
        durasi_menginap = (datetime.strptime(tanggal_check_out, '%Y-%m-%d') - datetime.strptime(tanggal_check_in, '%Y-%m-%d')).days
        
        #Ketika check-in dan check-out di hari yang sama, durasi menginap dihitung 1 hari
        if durasi_menginap == 0 :
            durasi_menginap = 1

        #Validasi tanggal check-in tidak boleh lebih awal dari tanggal reservasi
        if tanggal_check_in < today_date:
            flash('Tanggal Check-In tidak boleh lebih awal dari tanggal reservasi!', 'danger')
            return redirect(request.url)
        
        #Validasi tanggal pembayaran tidak boleh lebih awal dari tanggal reservasi
        if tanggal_pembayaran < today_date:
            flash('Tanggal Pembayaran tidak boleh lebih awal dari tanggal reservasi!', 'danger')
            return redirect(request.url)
        
        # Validasi tanggal check-out tidak boleh lebih awal dari tanggal check-in
        if tanggal_check_out < tanggal_check_in :
            flash('Tanggal Check-Out tidak boleh lebih awal dari Tanggal Check-In. Silahkan input yang benar!', 'danger')
            return redirect(request.url)

        # Simpan data ke database
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    SELECT COUNT(*) FROM ReservasiKamar 
                    WHERE id_kamar = ? AND 
                        (
                            (tanggal_check_in <= ? AND tanggal_check_out >= ?) OR 
                            (tanggal_check_in <= ? AND tanggal_check_out >= ?) OR
                            (tanggal_check_in >= ? AND tanggal_check_out <= ?)
                        )
                ''', (id_kamarReservasi, tanggal_check_in, tanggal_check_in, tanggal_check_out, tanggal_check_out, tanggal_check_in, tanggal_check_out))
                reservation_count = cursor.fetchone()[0]

                if reservation_count > 0:
                    flash('Kamar ini sudah dipesan untuk tanggal check-in dan check-out yang sama. Silakan pilih kamar lain.', 'danger')
                    return redirect(request.url)
                
                #Menghitung biaya layanan tambahan berdasarkan id_service
                cursor.execute('SELECT biaya_layanan FROM LayananTambahan WHERE id_service = ?', (id_serviceReservasi,))
                harga_service = cursor.fetchone()

                if not harga_service:
                    flash('Service ID tidak valid!', 'danger')
                    return redirect(request.url)
                harga_service = harga_service[0]

                #Menghitung harga kamar berdasarkan id_kamar
                cursor.execute('SELECT harga_kamar FROM KamarHotel WHERE id_kamar = ?', (id_kamarReservasi,))
                harga_kamar = cursor.fetchone()
                if not harga_kamar:
                    flash('Kamar ID tidak valid!', 'danger')
                    return redirect(request.url)
                harga_kamar = harga_kamar[0]

                #Menghitung total harga reservasi kamar
                total_harga = (harga_service * jml_layananReservasi) + (harga_kamar * durasi_menginap)

                cursor.execute('''INSERT INTO ReservasiKamar
                               (id_service, id_tamu, id_kamar, jumlah_layanan, tanggal_check_in, tanggal_check_out, tanggal_reservasi, tanggal_pembayaran, metode_pembayaran, total_harga) 
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                               (id_serviceReservasi, id_tamuReservasi, id_kamarReservasi, jml_layananReservasi, tanggal_check_in, tanggal_check_out, today_date,  tanggal_pembayaran, metode_pembayaranReservasi, total_harga))
                conn.commit()
                flash('Reservasi Kamar added successfully!', 'success')
                return redirect(url_for('routesReservasiKamar.ReservasiKamar'))
            except Exception as e:
                flash(f'Error: {str(e)}', 'danger')
            finally:
                cursor.close()
                conn.close()
        else:
            flash('Failed to connect to the database', 'danger')

    today_date = date.today()

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id_service, nama_layanan FROM LayananTambahan')
        service_list = cursor.fetchall()

        cursor.execute('SELECT id_tamu, nama_tamu FROM TamuHotel')
        tamu_list = cursor.fetchall()

        cursor.execute('SELECT id_kamar, tipe_kamar FROM KamarHotel')
        kamar_list = cursor.fetchall()
    
        cursor.close()
        conn.close()
    else:
        service_list = []
        tamu_list = []
        kamar_list = []
        
    # Render the form for GET request
    return render_template('createReservasiKamar.html', 
                           today_date=today_date, 
                           service_list=service_list, 
                           tamu_list=tamu_list, 
                           kamar_list=kamar_list)

@routesReservasiKamar.route('/tableReservasiKamar/update/<id_reservasi>', methods=['GET', 'POST'])
def update_ReservasiKamar(id_reservasi):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            if request.method == 'POST':
                # Get updated data from the form
                new_idKaryawan = request.form['id-karyawan_Layanan']
                new_namaLayanan = request.form['nama_Layanan']
                new_biayaLayanan = request.form['biaya_Layanan']


                # Update the tableA in the database
                cursor.execute('''UPDATE KamarHotel 
                                SET id_karyawan = ?,
                                    nama_layanan = ?,
                                    biaya_layanan = ?
                                WHERE id_service = ?''', (new_idKaryawan, new_namaLayanan, new_biayaLayanan, id_service))
                conn.commit()

                flash('Table A updated successfully!', 'success')
                return redirect(url_for('routesReservasiKamar.ReservasiKamar'))

            # For GET request, fetch current data to pre-fill the form
            cursor.execute('SELECT id_karyawan, nama_layanan, biaya_layanan FROM LayananTambahan WHERE id_service = ?', (id_service,))
            table = cursor.fetchone()
            if not table:
                flash('Table not found!', 'danger')
                return redirect(url_for('routesReservasiKamar.ReservasiKamar'))

            # Pass the current data to the form
            return render_template('editReservasiKamar.html', ReservasiKamar={
                'id_karyawan'    : table[0],
                'nama_layanan'   : table[1],
                'biaya_layanan'      : table[2]
            })
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()
    else:
        flash('Error: Unable to connect to the database.', 'danger')
        return redirect(url_for('routesReservasiKamar.continents'))


@routesReservasiKamar.route('/tableReservasiKamar/delete/<id_reservasi>', methods=['POST'])
def delete_continent(id_reservasi):
    # Get a connection to the database
    conn = create_connection()
    
    # Check if the connection was successful
    if conn:
        cursor = conn.cursor()
        try:
            # Delete the tableA from the database
            cursor.execute('DELETE FROM ReservasiKamar WHERE id_reservasi = ?', (id_reservasi,))
            conn.commit()  # Commit the transaction
            
            # Redirect to the tableA list with a success message
            flash('Table ReservasiKamar deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()  # Ensure the connection is closed
    else:
        flash('Error: Unable to connect to the database.', 'danger')
    
    return redirect(url_for('routesReservasiKamar.ReservasiKamar'))