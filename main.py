from time import sleep
from fastapi import FastAPI
from autoapi.core.database import DatabaseConnection
from autoapi.routes import upload

db = DatabaseConnection()
while True:
    try:
        sleep(0.2)
        if db.connect():
            print('DB:Connection:Successful.')
            break
    except:
        pass

print('DB:Bootstrap:', db.bootstrap_database())
app = FastAPI()
app.include_router(upload.router)
