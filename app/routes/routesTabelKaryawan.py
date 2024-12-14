from flask import Blueprint, render_template, redirect, url_for, request, flash
from connect import create_connection

# Create a blueprint for modular routing
routesTabelKaryawan = Blueprint('routesTabelKaryawan', __name__)

@routesTabelKaryawan.route('/')
def index():
    return render_template('home.html')

@routesTabelKaryawan.route('/tableKaryawan')
def TabelKaryawan():
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
            SELECT * FROM TabelKaryawan
            ORDER BY id_karyawan 
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
        ''', (offset, per_page))

        # cursor.execute('SELECT * FROM TamuHotel')
        
        # Fetch the results
        table = cursor.fetchall()
        
        # Get the total count of rows to calculate the number of pages
        cursor.execute('SELECT COUNT(*) FROM TabelKaryawan')
        total_count = cursor.fetchone()[0]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Calculate total number of pages
        total_pages = (total_count + per_page - 1) // per_page
        
        # Pass the results, total pages, and current page to the template
        return render_template('/TabelKaryawan/tableKaryawan.html', table=table, total_pages=total_pages, current_page=page)
    else:
        return render_template('/TabelKaryawan/tableKaryawan.html', table=None)

@routesTabelKaryawan.route('/tableKaryawan/create', methods=['GET', 'POST'])
def create_TabelKaryawan():
    # Handle the form submission when the method is POST
    if request.method == 'POST':
        # properti input digunakan disini
        karyawanHotel_nama = request.form['nama_KaryawanHotel']
        karyawanHotel_jabatan = request.form['jabatan_KaryawanHotel']
        karyawanHotel_nohp = request.form['nohp_KaryawanHotel']
        karyawanHotel_alamat = request.form['alamat_KaryawanHotel']
        karyawanHotel_gaji = request.form['gaji_KaryawanHotel']

        
        # Get a connection to the database
        conn = create_connection()
        
        # Check if the connection was successful
        if conn:
            cursor = conn.cursor()
            try:
                # Insert the new tableA into the database
                cursor.execute('INSERT INTO TabelKaryawan (nama_karyawan, jabatan, hp_karyawan, alamat_karyawan, gaji) VALUES (?, ?, ?, ?, ?)', 
                               (karyawanHotel_nama, karyawanHotel_jabatan, karyawanHotel_nohp, karyawanHotel_alamat, karyawanHotel_gaji))
                conn.commit()  # Commit the transaction
                
                # Redirect to the tableA list with a success message
                flash('TabelKaryawan added successfully!', 'success')
                return redirect(url_for('routesTabelKaryawan.TabelKaryawan'))
            except Exception as e:
                flash(f'Error: {str(e)}', 'danger')  # Flash error message
                print(f"Database error: {e}")  
            finally:
                cursor.close()
                conn.close()
        
        flash('Failed to connect to the database', 'danger')  # Error if connection failed

    # Render the form for GET request
    return render_template('/TabelKaryawan/createTabelKaryawan.html')

@routesTabelKaryawan.route('/tableKaryawan/update/<id_karyawan>', methods=['GET', 'POST'])
def update_TabelKaryawan(id_karyawan):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            if request.method == 'POST':
                # Get updated data from the form
                new_namaKaryawanHotel = request.form['nama_KaryawanHotel']
                new_jabatanKaryawanHotel = request.form['jabatan_KaryawanHotel']
                new_nohpKaryawanHotel = request.form['nohp_KaryawanHotel']
                new_alamatKaryawanHotel = request.form['alamat_KaryawanHotel']
                new_gajiKaryawanHotel = request.form['gaji_KaryawanHotel']

                # Update the Table Karyawan in the database
                cursor.execute('''UPDATE TabelKaryawan 
                                SET nama_karyawan = ?,
                                    jabatan = ?,
                                    hp_karyawan = ?,
                                    alamat_karyawan = ?,
                                    gaji = ?
                                WHERE id_karyawan = ?''', (new_namaKaryawanHotel, new_jabatanKaryawanHotel, new_nohpKaryawanHotel, new_alamatKaryawanHotel, new_gajiKaryawanHotel, id_karyawan))
                conn.commit()

                flash('Table Karyawan updated successfully!', 'success')
                return redirect(url_for('routesTabelKaryawan.TabelKaryawan'))

            # For GET request, fetch current data to pre-fill the form
            cursor.execute('SELECT nama_karyawan, jabatan, hp_karyawan, alamat_karyawan, gaji FROM TabelKaryawan WHERE id_karyawan = ?', (id_karyawan,))
            table = cursor.fetchone()
            if not table:
                flash('Table not found!', 'danger')
                return redirect(url_for('routesTabelKaryawan.TabelKaryawan'))

            # Pass the current data to the form
            return render_template('/TabelKaryawan/editTabelKaryawan.html', TabelKaryawan={
                'nama_karyawan'     : table[0],
                'jabatan'           : table[1],
                'hp_karyawan'       : table[2],
                'alamat_karyawan'   : table[3],
                'gaji'              : table[4]
            })
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()
    else:
        flash('Error: Unable to connect to the database.', 'danger')
        return redirect(url_for('routesTabelKaryawan.continents'))

@routesTabelKaryawan.route('/tableKaryawan/delete/<id_karyawan>', methods=['POST'])
def delete_continent(id_karyawan):
    # Get a connection to the database
    conn = create_connection()
    
    # Check if the connection was successful
    if conn:
        cursor = conn.cursor()
        try:
            # Delete the TabelKaryawan from the database
            cursor.execute('DELETE FROM TabelKaryawan WHERE id_karyawan = ?', (id_karyawan,))
            conn.commit()  # Commit the transaction
            
            # Redirect to the TabelKaryawan list with a success message
            flash('Table TabelKaryawan deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()  # Ensure the connection is closed
    else:
        flash('Error: Unable to connect to the database.', 'danger')
    
    return redirect(url_for('routesTabelKaryawan.TabelKaryawan'))