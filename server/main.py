from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from random import uniform
import time

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins = ["http://localhost:5173"]
)

@app.get("/async")
async def async_response():
    start_time = time.time()
    # sleep for random time between 0 and 2 seconds
    sleep_time = uniform(0.0, 2.0)
    time.sleep(sleep_time)
    end_time = time.time()
    return JSONResponse({"elapsed": end_time - start_time})
