from dotenv import load_dotenv
from fastapi import FastAPI
import service
import constants
import os


load_dotenv()
constants.SCALYR_TOKEN = os.environ["SCALYR_TOKEN"]


app = FastAPI()


@app.get("/")
def about():
    return {"project_name": "spacelog", "version": 0.1}


@app.get("/logs")
def get_log_by_trace_id(trace_id: str):
    return service.get_log_by_trace_id(trace_id)
