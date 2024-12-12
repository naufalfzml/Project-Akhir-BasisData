from flask import Blueprint, render_template, redirect, url_for, request, flash
from connect import create_connection

# Create a blueprint for modular routing
routesReservasiKamar = Blueprint('routesReservasiKamar', __name__)

@routesReservasiKamar.route('/')
def index():
    return render_template('home.html')

@routesReservasiKamar.route('/tableLayananTambahan')
def LayananTambahan():
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
            SELECT * FROM LayananTambahan
            ORDER BY id_service  
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
        ''', (offset, per_page))

        # cursor.execute('SELECT * FROM LayananTambahan')
        
        # Fetch the results
        table = cursor.fetchall()
        
        # Get the total count of rows to calculate the number of pages
        cursor.execute('SELECT COUNT(*) FROM LayananTambahan')
        total_count = cursor.fetchone()[0]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Calculate total number of pages
        total_pages = (total_count + per_page - 1) // per_page
        
        # Pass the results, total pages, and current page to the template
        return render_template('tableLayananTambahan.html', table=table, total_pages=total_pages, current_page=page)
    else:
        return render_template('tableLayananTambahan.html', table=None)

@routesReservasiKamar.route('/tableLayananTambahan/create', methods=['GET', 'POST'])
def create_LayananTambahan():
    # Handle the form submission when the method is POST
    if request.method == 'POST':
        # properti input digunakan disini
        layanan_idKaryawan = request.form['id-karyawan_Layanan']
        layanan_nama = request.form['nama_Layanan']
        layanan_biaya = request.form['biaya_Layanan']

        
        # Get a connection to the database
        conn = create_connection()
        
        # Check if the connection was successful
        if conn:
            cursor = conn.cursor()
            try:
                # Insert the new tableA into the database
                cursor.execute('INSERT INTO LayananTambahan (id_karyawan, nama_layanan, biaya_layanan) VALUES (?, ?, ?)', 
                               (layanan_idKaryawan, layanan_nama, layanan_biaya))
                conn.commit()  # Commit the transaction
                
                # Redirect to the tableA list with a success message
                flash('LayananTambahan added successfully!', 'success')
                return redirect(url_for('routesLayananTambahan.LayananTambahan'))
            except Exception as e:
                flash(f'Error: {str(e)}', 'danger')  # Flash error message
                print(f"Database error: {e}")  
            finally:
                cursor.close()
                conn.close()
        
        flash('Failed to connect to the database', 'danger')  # Error if connection failed

    # Render the form for GET request
    return render_template('createLayananTambahan.html')

@routesReservasiKamar.route('/tableLayananTambahan/update/<id_service>', methods=['GET', 'POST'])
def update_LayananTambahan(id_service):
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
                return redirect(url_for('routesKamarHotel.KamarHotel'))

            # For GET request, fetch current data to pre-fill the form
            cursor.execute('SELECT id_karyawan, nama_layanan, biaya_layanan FROM LayananTambahan WHERE id_service = ?', (id_service,))
            table = cursor.fetchone()
            if not table:
                flash('Table not found!', 'danger')
                return redirect(url_for('routesLayananTambahan.LayananTambahan'))

            # Pass the current data to the form
            return render_template('editLayananTambahan.html', LayananTambahan={
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
        return redirect(url_for('routesLayananTambahan.continents'))

@routesReservasiKamar.route('/tableLayananTambahan/delete/<id_service>', methods=['POST'])
def delete_continent(id_service):
    # Get a connection to the database
    conn = create_connection()
    
    # Check if the connection was successful
    if conn:
        cursor = conn.cursor()
        try:
            # Delete the tableA from the database
            cursor.execute('DELETE FROM LayananTambahan WHERE id_service = ?', (id_service,))
            conn.commit()  # Commit the transaction
            
            # Redirect to the tableA list with a success message
            flash('Table LayananTambahan deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()  # Ensure the connection is closed
    else:
        flash('Error: Unable to connect to the database.', 'danger')
    
    return redirect(url_for('routesLayananTambahan.LayananTambahan'))