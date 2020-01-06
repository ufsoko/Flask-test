from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
mg = Migrate()

def init_exts(app):
    db.init_app(app)
    mg.init_app(app,db)

