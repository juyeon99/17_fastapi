from fastapi import FastAPI, Depends
from database import session_local, engine
from sqlalchemy.orm import Session
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Generator 함수
# 함수가 generate한 객체를 반환하게 하는 키워드
def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post("/teachers", response_model=schemas.TeacherResponse)
async def create_teacher(
    teacher: schemas.TeacherCreate,
    db: Session=Depends(get_db)
):
    response = crud.create_teacher(db, teacher)
    return response

@app.get("/teacher/{teacher_id}", response_model=schemas.TeacherResponse)
async def find_teacher_by_id(teacher_id: int, db: Session=Depends(get_db)):
    db_teacher = crud.get_teacher_by_id(db, teacher_id)
    return db_teacher

# teacher 전체 조회
@app.get("/teachers", response_model=list[schemas.TeacherResponse])
async def find_all_teachers(db: Session=Depends(get_db)):
    all_teachers = crud.get_all_teachers(db)
    return all_teachers

# teacher 수정
@app.put("/teachers/{teacher_id}", response_model=schemas.TeacherResponse)
async def update_teacher(
    teacher_id: int,
    teacher: schemas.TeacherUpdate,
    db: Session=Depends(get_db)
):
    updated_teacher = crud.update_teacher(db, teacher_id, teacher)
    return updated_teacher

# teacher 삭제
@app.delete("/teachers/{teacher_id}", status_code=204)
async def delete_teacher(teacher_id: int, db: Session=Depends(get_db)):
    crud.delete_teacher(db, teacher_id)
    return None

# =========================================================================
@app.post("/students", response_model=schemas.StudentResponse)
async def create_student(
    student: schemas.StudentCreate,
    db: Session=Depends(get_db)
):
    response = crud.create_student(db, student)
    return response

@app.get("/student/{student_id}", response_model=schemas.StudentResponse)
async def find_student_by_id(student_id: int, db: Session=Depends(get_db)):
    db_student = crud.get_student_by_id(db, student_id)
    return db_student

# student 전체 조회
@app.get("/students", response_model=list[schemas.StudentResponse])
async def find_all_students(db: Session=Depends(get_db)):
    all_students = crud.get_all_students(db)
    return all_students

# student 수정
@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
async def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session=Depends(get_db)
):
    updated_student = crud.update_student(db, student_id, student)
    return updated_student

# student 삭제
@app.delete("/students/{student_id}", status_code=204)
async def delete_student(student_id: int, db: Session=Depends(get_db)):
    crud.delete_student(db, student_id)
    return None