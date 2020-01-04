from app import r
from app.logs import Log
# from app import Logger
# Logger = Log(__name__).Logger
import logging

def get_cache_by_name(key_name= ''):
    mes='1' * 20 + key_name
    logging.info(str(mes))
    return r.get(key_name)

def save_cache(key_name, value, expire_time=7*24*60*60):
    r.set(key_name, value)
    if expire_time:  # 可能传None， 表示不过期
        r.expire(key_name, expire_time)