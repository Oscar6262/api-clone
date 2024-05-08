from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)  # Habilitar CORS para toda la aplicación
MASTER_USER = 'admindb'
MASTER_PASSWORD = 'admin'
DATABASE_NAME = 'asteriskcdrdb'
DATABASE_IP = '192.168.1.68'


app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{MASTER_USER}:{MASTER_PASSWORD}@{DATABASE_IP}/{DATABASE_NAME}'
db = SQLAlchemy(app)