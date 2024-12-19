from flask import Flask
from app.routes.routesKamarHotel import routesKamarHotel
from app.routes.routesTamuHotel import routesTamuHotel
from app.routes.routesTabelKaryawan import routesTabelKaryawan
from app.routes.routesReservasiKamar import routesReservasiKamar
from app.routes.routesReservasiLayanan import routesReservasiLayanan
from dotenv import load_dotenv
import os

def create_app():
    # Load the environment variables from .env file
    load_dotenv()

    # Create the Flask app
    from app.routes.routesLayananTambahan import routesLayananTambahan
    app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

    # Set the secret key using an environment variable
    app.config['SECRET_KEY'] = '1234'

    # Register the routes blueprint
    app.register_blueprint(routesKamarHotel)
    app.register_blueprint(routesTamuHotel)
    app.register_blueprint(routesTabelKaryawan)
    app.register_blueprint(routesLayananTambahan)
    app.register_blueprint(routesReservasiKamar)
    app.register_blueprint(routesReservasiLayanan)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)