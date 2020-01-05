import sys
from fastapi import APIRouter

from app.util.db_util import awit_dbconn
from app.models.Hello.view_data_model import Hello

version = f"{sys.version_info.major}.{sys.version_info.minor}"

hello = APIRouter()


@hello.get("/")
async def read_root(Hello):
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    message = Hello.message
    return {"message": message}

@hello.get("/index")
async def read_db(Hello):
    sql = '''select * from table_hello;'''
    data = await awit_dbconn.get_data_sql_all(sql)
    return {"message": data}
