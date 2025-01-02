from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app.models import Doctor
from sqlalchemy.future import select



router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session
        
@router.post("/doctors/")
async def create_doctor(doctor: Doctor, db: AsyncSession = Depends(get_db)):
    db.add(doctor)
    await db.commit()
    await db.refresh(doctor)
    return doctor

@router.get("/doctors/{doctor_id}")
async def read_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    doctor = await db.execute(select(Doctor).where(Doctor.id == doctor_id))
    doctor = doctor.scalar_one_or_none()   
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@router.put("/doctors/{doctor_id}")
async def update_doctor(doctor_id: int, doctor: Doctor, db: AsyncSession = Depends(get_db)):
    db_doctor = await  db.execute(select(Doctor).where(Doctor.id == doctor_id))
    doctor = result.scalar_one_or_none()
    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    db_doctor.name = doctor.name
    db_doctor.specialty = doctor.specialty
    db_doctor.available = doctor.available
    await db.commit()
    await db.refresh(db_doctor)
    return db_doctor




@router.delete("/doctors/{doctor_id}")
async def delete_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Doctor).where(Doctor.id == doctor_id))
    doctor = result.scalar_one_or_none()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    await db.delete(doctor)
    await db.commit()
    return {"message": "Doctor deleted successfully"}