from flask import Blueprint, render_template, redirect, url_for, request, flash
from connect import create_connection

# Create a blueprint for modular routing
routesReservasiLayanan = Blueprint('routesReservasiLayanan', __name__)

@routesReservasiLayanan.route('/tableReservasiLayanan')
def ReservasiLayanan():
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
        # Join to get more meaningful information
        cursor.execute('''
            SELECT 
                RL.id_reservasi AS id_reservasi, 
                RK.id_service AS id_service, 
                RK.jumlah_layanan AS jumlah_layanan,
                LT.nama_layanan AS nama_layanan,
                RK.id_tamu AS id_tamu, 
                TH.nama_tamu AS nama_tamu
            FROM Reservasi_Layanan RL
            JOIN ReservasiKamar RK ON RL.id_reservasi = RK.id_reservasi
            JOIN LayananTambahan LT ON RL.id_service = LT.id_service
            JOIN TamuHotel TH ON RK.id_tamu = TH.id_tamu
            ORDER BY RL.id_reservasi  
            OFFSET ? ROWS
            FETCH NEXT ? ROWS ONLY
        ''', (offset, per_page))
        
        # Fetch the results
        table = cursor.fetchall()
        
        # Get the total count of rows to calculate the number of pages
        cursor.execute('SELECT COUNT(*) FROM Reservasi_Layanan')
        total_count = cursor.fetchone()[0]
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Calculate total number of pages
        total_pages = (total_count + per_page - 1) // per_page
        
        # Pass the results, total pages, and current page to the template
        return render_template('tableReservasiLayanan.html', table=table, total_pages=total_pages, current_page=page)
    else:
        return render_template('tableReservasiLayanan.html', table=None)

# Note: No separate create/update/delete routes for Reservasi_Layanan
# As this will be handled automatically in ReservasiKamar routes