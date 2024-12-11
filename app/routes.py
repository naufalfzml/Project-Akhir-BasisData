from flask import Blueprint, render_template, redirect, url_for, request, flash
from connect import create_connection

# Create a blueprint for modular routing
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('home.html')

@routes.route('/tableA')
def tableA():
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
            SELECT * FROM KamarHotel
            ORDER BY id_kamar  
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
        ''', (offset, per_page))

        # cursor.execute('SELECT * FROM TableA')
        
        # Fetch the results
        table = cursor.fetchall()
        
        # Get the total count of rows to calculate the number of pages
        cursor.execute('SELECT COUNT(*) FROM KamarHotel')
        total_count = cursor.fetchone()[0]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Calculate total number of pages
        total_pages = (total_count + per_page - 1) // per_page
        
        # Pass the results, total pages, and current page to the template
        return render_template('tableA.html', table=table, total_pages=total_pages, current_page=page)
    else:
        return render_template('tableA.html', table=None)

@routes.route('/tableA/create', methods=['GET', 'POST'])
def create_tableA():
    # Handle the form submission when the method is POST
    if request.method == 'POST':
        # properti input digunakan disini
        kamarHotel_tipe = request.form['tipe_KamarHotel']
        kamarHotel_harga = request.form['harga_KamarHotel']
        kamarHotel_no = request.form['no_KamarHotel']

        
        # Get a connection to the database
        conn = create_connection()
        
        # Check if the connection was successful
        if conn:
            cursor = conn.cursor()
            try:
                # Insert the new tableA into the database
                cursor.execute('INSERT INTO KamarHotel (tipe_kamar, harga_kamar, nomor_kamar) VALUES (?, ?, ?)', 
                               (kamarHotel_tipe, kamarHotel_harga, kamarHotel_no))
                conn.commit()  # Commit the transaction
                
                # Redirect to the tableA list with a success message
                flash('TableA added successfully!', 'success')
                return redirect(url_for('routes.tableA'))
            except Exception as e:
                flash(f'Error: {str(e)}', 'danger')  # Flash error message
                print(f"Database error: {e}")  
            finally:
                cursor.close()
                conn.close()
        
        flash('Failed to connect to the database', 'danger')  # Error if connection failed

    # Render the form for GET request
    return render_template('createTableA.html')

@routes.route('/tableA/update/<id>', methods=['GET', 'POST'])
def update_tableA(id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        try:
            if request.method == 'POST':
                # Get updated data from the form
                new_name = request.form['nameTableA']

                # Update the tableA in the database
                cursor.execute('UPDATE tableA SET name = ? WHERE id = ?', (new_name, id))
                conn.commit()

                flash('Table A updated successfully!', 'success')
                return redirect(url_for('routes.tableA'))

            # For GET request, fetch current data to pre-fill the form
            cursor.execute('SELECT name FROM tableA WHERE id = ?', (id))
            table = cursor.fetchone()
            if not table:
                flash('Table not found!', 'danger')
                return redirect(url_for('routes.tableA'))

            # Pass the current data to the form
            return render_template('editTableA.html', table={'name': table[0]})
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()
    else:
        flash('Error: Unable to connect to the database.', 'danger')
        return redirect(url_for('routes.continents'))

@routes.route('/tableA/delete/<id>', methods=['POST'])
def delete_continent(id):
    # Get a connection to the database
    conn = create_connection()
    
    # Check if the connection was successful
    if conn:
        cursor = conn.cursor()
        try:
            # Delete the tableA from the database
            cursor.execute('DELETE FROM TableA WHERE id = ?', (id))
            conn.commit()  # Commit the transaction
            
            # Redirect to the tableA list with a success message
            flash('Table A deleted successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()  # Ensure the connection is closed
    else:
        flash('Error: Unable to connect to the database.', 'danger')
    
    return redirect(url_for('routes.tableA'))