
import typing
from app.logs import Log
Logger = Log(__name__).Logger
from app import database, get_session
from pandas import DataFrame

class awit_dbconn():

    @staticmethod
    async def get_data_sql_all(sql)-> typing.List[typing.Mapping]:
        data = await database.fetch_all(sql)
        return data

    @staticmethod
    async def get_sql_one(query_sql)-> typing.Optional[typing.Mapping]:
        data = await database.fetch_one(query_sql)
        return data

    @staticmethod
    async def get_sql_datafame(query_str) -> DataFrame:
        data = await database.fetch_one(query_str)
        return DataFrame(data)