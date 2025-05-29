from fastapi import FastAPI
from app.api import router as shape_router
from app.shapes import *

app = FastAPI(title="Shape Service API")
app.include_router(shape_router, prefix="", tags=["shapes"])