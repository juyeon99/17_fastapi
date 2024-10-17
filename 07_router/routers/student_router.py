from fastapi import APIRouter

student = APIRouter(
    prefix="/api/students",
    tags=["students"]
)

@student.get("/")
async def get_student():
    return {"message":"학생입니다!"}