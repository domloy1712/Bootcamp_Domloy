from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

db = SQLAlchemy()


def crear_app():
    app = Flask(__name__)
    app.config.from_object(Config)
  
    db.init_app(app)
    migrate = Migrate (app, db)
  
    from .routes.usuarios import usuarios_bp
    app.register_blueprint(usuarios_bp)
  
    return app