import os
from flask import Flask
from flask_migrate import Migrate

from flask_wtf.csrf import CSRFProtect, generate_csrf

# from .seeds import seed_commands
from .config import Config

from .models import db

# API ROUTES

app = Flask(__name__)

# Uncomment if you want to use the terminal commands 
# app.cli.add_command(seed_commands)

# Place Registred Routes in here according to the following structure
# app.register_blueprint(<Your Route>, url_prefix="/api/<Your Route>")
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)



# Need this to actually post data 
@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route("/")
def hello():
	return {"message":"Hello World"},200