from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app.models import Patient

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/patients/")
async def create_patient(patient: Patient, db: AsyncSession = Depends(get_db)):
    db.add(patient)
    await db.commit()
    await db.refresh(patient)
    return patient

@router.get("/patients/{patient_id}")
async def read_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    patient = await db.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
