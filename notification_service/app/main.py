import asyncio
from fastapi import FastAPI
from app.notification_handler import consume
from app.routers import notifications


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """
    Startup event for the Notification Service:
    - Initializes the RabbitMQ consumer to process messages.
    """
    print("Starting Notification Service...")
    asyncio.create_task(consume())
# Include the notifications router

app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])



@app.get("/")
async def root():
    return {"message": "Notification Service is running"}
