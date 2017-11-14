# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap as Bootstrap
from flask_moment import Moment as Moment
from flask_sqlalchemy import SQLAlchemy as SQLAlchemy
from flask_login import LoginManager as LoginManager
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u'请您先登录再访问页面'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    from .coal_chp import coal_chp as coalchp_blueprint
    app.register_blueprint(coalchp_blueprint, url_prefix='/coal_chp')

    app.debug = False

    return app
