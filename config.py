# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


# 程序配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEV_DATABASE_URL = \
        'postgresql://postgres:postgres@192.168.33.133:5432/postgres'
        # 'postgresql://postgres:postgres@10.167.23.60:5432/postgres'
        # 'postgresql://postgres:postgres@192.168.33.133:5432/postgres'
        

    @staticmethod
    def init_app(app):
        pass


# 开发程序配置
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DEV_DATABASE_URL


# 测试程序配置
class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    SQLALCHEMY_DATABASE_URI = Config.DEV_DATABASE_URL
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class IpandPortConfig(Config):
    APP_IP = "127.0.0.1"
    APP_PORT = "5000"

    # APP_IP = "117.36.73.154"
    # APP_PORT = "6008"


class MarkToDocx(Config):
    MAIN_OUTFILE_FOR_DOWNLOAD_DOCX_PATH = "mark_to_docx/outfile/"
    MAIN_SOURCE_DOCX_PATH = "mark_to_docx/source/"
    MAIN_INPUTFILE_MD_PATH = "mark_to_docx/inputfile/md/"
    MAIN_INPUTFILE_HTML_PATH = "mark_to_docx/inputfile/html/"


class ImgConfig(Config):
    MAIN_IMG_PATH = "app/static/img"
    CCPP_IMG_PATH_SOURCE = "app/ccpp/service/imgdealwith/ccppimg"
    CCPP_IMG_PATH_RESULT = "app/ccpp/service/imgdealwith/resultimg"
    GPG_IMG_PATH_SOURCE = "app/gpg/service/imgdealwith/gpg_img"
    GPG_IMG_PATH_RESULT = "app/gpg/service/imgdealwith/result_img"
    BIOMASS_IMG_PATH_SOURCE = "app/biomass_chp/service/imgdealwith/biomass_img"
    BIOMASS_IMG_PATH_RESULT = "app/biomass_chp/service/imgdealwith/result_img"
    COAL_IMG_PATH_SOURCE = "app/coal_chp/service/imgProcessing/model"
    COAL_IMG_PATH_RESULT = "app/coal_chp/service/imgProcessing/result"


class ExcleConfig(Config):
    CCPP_EXCLE_ECONOMIC_PATH_SOURCE = "app/ccpp/service/excledealwith/ccppbaseexcle"
    CCPP_EXCLE_ECONOMIC_PATH_RESULT = "app/ccpp/service/excledealwith/economicresultexcle"


class LogConfig(Config):
    LOG_FILE_PATH = "energyisland.log"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'ipandport': IpandPortConfig,
    'imgConfig': ImgConfig,
    'excleConfig': ExcleConfig,
    'markToDocx': MarkToDocx,
    'logconfig': LogConfig
}
