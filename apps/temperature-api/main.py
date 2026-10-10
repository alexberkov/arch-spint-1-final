from fastapi import FastAPI

from api.v1 import temperature


app = FastAPI(
    title='Temperature Service',
    description='Get random temperature sensor data',
    openapi_url='/api/openapi.json',
    servers=[
        {"url": "http://127.0.0.1:8081"}
    ],
)


app.include_router(temperature.router, prefix='', tags=['temperature'])
