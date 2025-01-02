from fastapi import FastAPI
from app.routers import patients

app = FastAPI()

app.include_router(patients.router, prefix="/api/patient", tags=["Patient"])
