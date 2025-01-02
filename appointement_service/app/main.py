from fastapi import FastAPI
from app.routers import appointments

app = FastAPI()

app.include_router(appointments.router, prefix="/api/appointment", tags=["Appointment"])
