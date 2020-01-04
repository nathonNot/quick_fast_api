import logging
import logging.handlers
import os
import sys

import redis
from starlette.middleware.gzip import GZipMiddleware

import config
import databases
import sqlalchemy
from fastapi import FastAPI
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


database = databases.Database(config.DATABASE_URI)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    config.DATABASE_URI
)

Session_factory = sessionmaker(bind=engine)
Session = scoped_session(Session_factory)

# 连接redis数据库
print("========连接redis========")
redis_poll = redis.ConnectionPool(host=config.REDIS_SETTING.get('host'),
                                  port=config.REDIS_SETTING.get('port'),
                                  password=config.REDIS_SETTING.get('password'))
r = redis.StrictRedis(connection_pool=redis_poll)

def get_session():
    session = Session()
    return session


app = FastAPI()

# 初始化系统日志
print("==========初始化系统日志==========")
# formatter = logging.Formatter(fmt=config.LOGGING_SETTING.get('format'),
#                               datefmt=config.LOGGING_SETTING.get('datefmt'))
# logging.basicConfig(**config.LOGGING_SETTING)


# gzip中间件
app.add_middleware(GZipMiddleware)


from app import view
from app.logs import Log

log = Log(__name__)
log.info('启动服务器')