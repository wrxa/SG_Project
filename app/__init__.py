# -*- coding: utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap as Bootstrap
from flask_moment import Moment as Moment
from flask_sqlalchemy import SQLAlchemy as SQLAlchemy
from flask_login import LoginManager as LoginManager
from config import config
import logging

# client = MongoClient('mongodb://192.168.33.133:27017/')
# db_energy_island_mongo = client['energy_island']
# collection = db_energy_island_mongo['test']
handler = logging.FileHandler(config['logconfig'].LOG_FILE_PATH)
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_message = u'请您先登录再访问页面'


def mylen(arg):
    # 实现一个可以求长度的函数
    if arg is None:
        return 0
    return len(arg)


# 该函数实现给定一个区间返回区间的内容
def interval(arg, start, end=None):
    # 过滤器中传递多个参数，第一个参数为被过滤的内容，第二第三个参数需要自己传入
    if arg is None:
        return u''
    if end is None:
        return arg[int(start):]
    return arg[int(start):int(end)]


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    logging_format = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)

    env = app.jinja_env
    env.filters['strlen'] = mylen
    # 注册自定义过滤器
    env.filters['interval'] = interval
    # 注册自定义过滤器

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .ccpp.ccppviews import ccppviews as ccppviews_blueprint
    app.register_blueprint(ccppviews_blueprint, url_prefix='/ccpp')

    from .coal_chp.view import coalviews as coalviews_blueprint
    app.register_blueprint(coalviews_blueprint)
    
    from gpg.view import gpg_view as gpg_blueprint
    app.register_blueprint(gpg_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    from .biomass_chp.views import biomassviews
    app.register_blueprint(biomassviews)
    
    from .energy_island import energy_island as energy_island_blueprint
    app.register_blueprint(energy_island_blueprint)

    app.debug = False

    return app
