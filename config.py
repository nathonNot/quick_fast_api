import logging
import os
import sys

DATABASE_URI = 'mysql://root:123456@mysql:3306/hello?charset=utf8mb4'

logging_level = logging.INFO
# if sys.platform == 'win32':
#     logging_level = logging.DEBUG
# 系统日志设置
LOGGING_SETTING = {'level': logging_level,
                   'format': '[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s] [%(lineno)d] %(message)s',
                   'datefmt': '%Y-%m-%d %H:%M:%S',
                   'filename': os.path.join('logs', 'app.log'),
                   'filemode': 'a'
                   # 'open_stream_heandler': False,
                   # 'max_bytes': 5 * 1024 * 1024,
                   # 'backup_count': 10,
                   }

# REDIS数据库配置
if sys.platform == 'win32':
    REDIS_SETTING = {
        'host': '192.168.1.45',
        'port': '26379',
        'password': '123456'
    }
else:
    REDIS_SETTING = {
        'host': 'redis',
        'port': '6379',
        'password': '123456'
    }
