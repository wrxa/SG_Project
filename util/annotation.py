# -*- coding:UTF-8 -*-
from app import db
from flask import current_app
import time
from functools import wraps
import inspect


# 有返回值
def use_logging(func):
    @wraps(func)
    def userlog(*args, **kwargs):
        # current_app.logger.info(inspect.getsourcefile(func) + "----------------------------------------------")
        current_app.logger.info("%s - - - - %s is starting - - - - %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), func.__name__, inspect.getsourcefile(func)))
        fun = func(*args)
        current_app.logger.info("%s - - - - %s  is ending - - - - %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), func.__name__, inspect.getsourcefile(func)))
        return fun
    return userlog


# 无返回值
def db_transaction(func):
    def wrapper(*args, **kwargs):
        try:
            print("start del:" + "%s is running" % func.__name__)
            func(*args)
            print("del table:" + "%s is running" % func.__name__)
            db.session.commit()
            print("end del:" + "%s is running" % func.__name__)
        except Exception as e:
            db.session.rollback()
            print("Error %s" % e)
            raise e
        finally:
            pass
    return wrapper


def main():
    pass


if __name__ == '__main__':
    main()

