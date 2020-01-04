from app.models.Hello.views import hello
from app import app, database

app.include_router(hello,
                   prefix="/api/hello",
                   tags=["hello"])

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()