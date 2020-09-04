#Memanggil library Flask
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

#Inisialisasi JWT
from flask_jwt_extended import JWTManager

#Untuk menjelaskan nama modul yang digunakan, sehingga ketika folder lain memanggil folder app akan otomatis teridentifikasi.
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

seeder = FlaskSeeder()
seeder.init_app(app, db)

#Memanggil file routes
from app.model import todo, user
from app import routes