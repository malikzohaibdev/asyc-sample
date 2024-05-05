from fastapi import FastAPI
from fastapi.responses import JSONResponse
from random import uniform
import time

app = FastAPI()


@app.get("/async")
async def async_response():
    sleep_time = uniform(0.0, 2.0)
    time.sleep(sleep_time)
    return JSONResponse({"response_time": sleep_time})
