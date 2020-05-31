import os
from flask import Flask
from flask_cors import CORS
from . import db
from .db.models import User

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True,static_url_path='',static_folder='dist')
    app.config.from_mapping(
        TIMEZONE='Asia/Shanghai',
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI= 'sqlite:///'+('/' if os.name != 'nt' else '')+os.path.join(app.instance_path, 'myblog.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    if test_config is None:
        # load the instance config, if it exists
        # app.config.from_envvar('MYBLOG_CONFIG',silent=True)
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    CORS(app)
    db.init_app(app)

    # main page
    @app.route('/')
    def hello():
        return app.send_static_file('index.html')

    # auth api
    from .api import auth
    app.register_blueprint(auth.bp)

    return app
