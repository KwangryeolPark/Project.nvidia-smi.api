# %%
from nvidia_monitor import Status, Process, STATUS_QUERY
from fastapi import FastAPI

status = Status()
process = Process()
api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/nvidia_status")
async def nvidia_status():
    return status.get(verbose=False)

@api.get("/nvidia_process")
async def nvidia_process():
    return process.get(verbose=False)

