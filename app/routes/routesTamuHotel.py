from flask import Blueprint, render_template, redirect, url_for, request, flash
from connect import create_connection

# Create a blueprint for modular routing
routesTamuHotel = Blueprint('routesTamuHotel', __name__)

@routesTamuHotel.route('/')
def index():
    return render_template('home.html')

@routesTamuHotel.route('/tableTamuHotel')
def TamuHotel():
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
            SELECT * FROM TamuHotel
            ORDER BY id_tamu  
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
        ''', (offset, per_page))

        # cursor.execute('SELECT * FROM TamuHotel')
        
        # Fetch the results
        table = cursor.fetchall()
        
        # Get the total count of rows to calculate the number of pages
        cursor.execute('SELECT COUNT(*) FROM TamuHotel')
        total_count = cursor.fetchone()[0]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Calculate total number of pages
        total_pages = (total_count + per_page - 1) // per_page
        
        # Pass the results, total pages, and current page to the template
        return render_template('tableTamuHotel.html', table=table, total_pages=total_pages, current_page=page)
    else:
        return render_template('tableTamuHotel.html', table=None)

@routesTamuHotel.route('/tableTamuHotel/create', methods=['GET', 'POST'])
def create_TamuHotel():
    # Handle the form submission when the method is POST
    if request.method == 'POST':
        # properti input digunakan disini
        tamuHotel_nama = request.form['nama_TamuHotel']
        tamuHotel_jenisKelamin = request.form['jenisKelamin_TamuHotel']
        tamuHotel_alamat = request.form['alamat_TamuHotel']
        tamuHotel_nohp = request.form['nohp_TamuHotel']
        tamuHotel_tanggalLahir = request.form['tanggalLahir_TamuHotel']

        
        # Get a connection to the database
        conn = create_connection()
        
        # Check if the connection was successful
        if conn:
            cursor = conn.cursor()
            try:
                # Insert the new tableA into the database
                cursor.execute('INSERT INTO TamuHotel (nama_tamu, jenis_kelamin, alamat_tamu, hp_tamu, tanggal_lahir) VALUES (?, ?, ?, ?, ?)', 
                               (tamuHotel_nama, tamuHotel_jenisKelamin, tamuHotel_alamat, tamuHotel_nohp, tamuHotel_tanggalLahir))
                conn.commit()  # Commit the transaction
                
                # Redirect to the tableA list with a success message
                flash('TamuHotel added successfully!', 'success')
                return redirect(url_for('routesTamuHotel.TamuHotel'))
            except Exception as e:
                flash(f'Error: {str(e)}', 'danger')  # Flash error message
                print(f"Database error: {e}")  
            finally:
                cursor.close()
                conn.close()
        
        flash('Failed to connect to the database', 'danger')  # Error if connection failed

    # Render the form for GET request
    return render_template('createTamuHotel.html')

@routesTamuHotel.route('/tableTamuHotel/update/<id_tamu>', methods=['GET', 'POST'])
def update_TamuHotel(id_tamu):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            if request.method == 'POST':
                # Get updated data from the form
                new_namaTamu = request.form['nama_TamuHotel']
                new_jenisKelaminTamu = request.form['jenisKelamin_TamuHotel']
                new_alamatTamu = request.form['alamat_TamuHotel']
                new_hpTamu = request.form['nohp_TamuHotel']
                new_tanggalLahirTamu = request.form['tanggalLahir_TamuHotel']


                # Update the Table TamuHotel in the database
                cursor.execute('''UPDATE TamuHotel 
                                SET nama_tamu = ?,
                                    jenis_kelamin = ?,
                                    alamat_tamu = ?,
                                    hp_tamu = ?,
                                    tanggal_lahir = ?
                                WHERE id_tamu = ?''', (new_namaTamu, new_jenisKelaminTamu, new_alamatTamu, new_hpTamu, new_tanggalLahirTamu, id_tamu))
                conn.commit()

                flash('Table TamuHotel updated successfully!', 'success')
                return redirect(url_for('routesTamuHotel.TamuHotel'))

            # For GET request, fetch current data to pre-fill the form
            cursor.execute('SELECT nama_tamu, jenis_kelamin, alamat_tamu, hp_tamu, tanggal_lahir FROM TamuHotel WHERE id_tamu = ?', (id_tamu,))
            table = cursor.fetchone()
            if not table:
                flash('Table not found!', 'danger')
                return redirect(url_for('routesTamuHotel.TamuHotel'))

            # Pass the current data to the form
            return render_template('editTamuHotel.html', TamuHotel={
                'nama_tamu'     : table[0],
                'jenis_kelamin' : table[1],
                'alamat_tamu'   : table[2],
                'hp_tamu'       : table[3],
                'tanggal_lahir' : table[4]
            })
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()
    else:
        flash('Error: Unable to connect to the database.', 'danger')
        return redirect(url_for('routesTamuHotel.continents'))

@routesTamuHotel.route('/tableTamuHotel/delete/<id_tamu>', methods=['POST'])
def delete_continent(id_tamu):
    # Get a connection to the database
    conn = create_connection()
    
    # Check if the connection was successful
    if conn:
        cursor = conn.cursor()
        try:
            # Delete the tableA from the database
            cursor.execute('DELETE FROM TamuHotel WHERE id_tamu = ?', (id_tamu,))
            conn.commit()  # Commit the transaction
            
            # Redirect to the tableA list with a success message
            flash('Table TamuHotel deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()  # Ensure the connection is closed
    else:
        flash('Error: Unable to connect to the database.', 'danger')
    
    return redirect(url_for('routesTamuHotel.TamuHotel'))