from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from aio_pika import connect_robust, Message
from app.database import async_session
from app.models import Appointment

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/appointments/")
async def create_appointment(appointment: Appointment, db: AsyncSession = Depends(get_db)):
    db.add(appointment)
    await db.commit()
    await db.refresh(appointment)

    # Publish event to RabbitMQ
    connection = await connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    exchange = await channel.default_exchange
    await exchange.publish(
        Message(body=f"Appointment {appointment.id} scheduled.".encode()),
        routing_key="appointments",
    )
    await connection.close()

    return appointment

@router.get("/appointments/{appointment_id}")
async def read_appointment(appointment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Appointment).where(Appointment.id == appointment_id))
    appointment = result.scalar_one_or_none()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment
