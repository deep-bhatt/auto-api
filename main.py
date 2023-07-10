import uvicorn
from time import sleep
from fastapi import FastAPI
from autoapi.core.database import DatabaseConnection
from autoapi.routes import upload, api

db = DatabaseConnection()
while True:
    try:
        sleep(0.5)
        if db.connect():
            print('DB:Connection:Successful.')
            break
    except Exception as e:
        print('attempting to connect to database', e)
        print('retrying...')

print('DB:Bootstrap:', db.bootstrap_database())
app = FastAPI()
app.include_router(upload.router)
app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
