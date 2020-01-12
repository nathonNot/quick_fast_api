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

# 路由缓存
def redis_view_cached(time=7 * 24 * 60 * 60):
    def set_cache(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if request.method != 'GET':
                response = func(*args, **kwargs)
                return response
            path = request.url
            path = path.split('//')[1]
            path = path.replace('/', '_')
            path = path.replace('.', '_')
            response = get_cache_by_name(path)
            if response:
                return to__response(json.loads(response))
            else:
                response = func(*args, **kwargs)
                if getattr(response, "status_code", None) == 200:
                    save_cache(path, json.dumps(response.json), time)
                return response

        return decorated_function

    return set_cache
