from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config_app import Config

app = Flask(__name__)
app.config.from_object(Config)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)