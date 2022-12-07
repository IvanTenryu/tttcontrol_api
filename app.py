from sys import prefix
from flask import Flask
from routes.change_log import blueprint_change_log
from routes.gps import blueprint_gps
from routes.installation import blueprint_installation
from routes.maintenance import blueprint_maintenance
from routes.sim import blueprint_sim
from routes.user import blueprint_user
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

### Swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### End swagger specific ###

# Register app blueprints
app.register_blueprint (blueprint_change_log, url_prefix="/change_log")
app.register_blueprint (blueprint_gps, url_prefix="/gps")
app.register_blueprint (blueprint_installation, url_prefix="/installation")
app.register_blueprint (blueprint_maintenance, url_prefix="/maintenance")
app.register_blueprint (blueprint_sim, url_prefix="/sim")
app.register_blueprint (blueprint_user, url_prefix="/user")

# Home endpoint
@app.route ("/", methods=["GET"])
def index ():
    """ Show all endpoints details """

    endpoints_data = {
        "endpoints": {
                "/user": "(post and get) Main endpoint of the 'user' table from database",
                "/sim": "(post and get) Main endpoint of the 'sim' table from database",
                "/gps": "(post and get) Main endpoint of the 'gps' table from database",
                "/change_log": "(post and get) Main endpoint of the 'change_log' table from database",
                "/installation": "(post and get) Main endpoint of the 'installation' table from database",
                "/maintenance": "(post and get) Main endpoint of the 'maintenance' table from database",
            } 
        }

    return endpoints_data



