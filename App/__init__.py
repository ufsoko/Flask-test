from flask import Flask
from App.views import init_views
from App.setting import envs
from App.ext import init_exts

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(envs.get(env))
    init_exts(app)
    init_views(app)
    return app