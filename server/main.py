from fastapi import FastAPI, responses
from random import uniform
import time

app = FastAPI()


@app.get("/async")
async def async_response():
    sleep_time = uniform(0.0, 0.2)
    time.sleep(sleep_time)
    return responses.JSONResponse({"response_time": sleep_time})
