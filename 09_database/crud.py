from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException

# teacher를 저장하는 서비스 로직
def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(
        name = teacher.name,
        is_active = teacher.is_active,
        nickname = teacher.nickname,
        description = teacher.description
    )
    
    db.add(db_teacher)
    db.commit()
    
    return db_teacher

# ID로 teacher 찾기
def get_teacher_by_id(db: Session, teacher_id: int):
    found_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    return found_teacher

def get_all_teachers(db: Session):
    # 모든 Teacher 모델 가져오기
    all_teachers = db.query(models.Teacher).all()
    return all_teachers

def update_teacher(db: Session, teacher_id: int, teacher: schemas.TeacherUpdate):
    found_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    
    if found_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher Not Found")
    
    if teacher.name is not None:
        found_teacher.name = teacher.name
    if teacher.is_active is not None:
        found_teacher.is_active = teacher.is_active
    if teacher.nickname is not None:
        found_teacher.nickname = teacher.nickname
    if teacher.description is not None:
        found_teacher.description = teacher.description
    
    db.commit()
    return found_teacher

def delete_teacher(db: Session, teacher_id: int):
    found_teacher = db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()
    
    if found_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher Not Found")
    
    db.delete(found_teacher)
    db.commit()

# =============================================================================
# student를 저장하는 서비스 로직
def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name = student.name,
        lunch_menu = student.lunch_menu,
        nickname = student.nickname,
        description = student.description
    )
    
    db.add(db_student)
    db.commit()
    
    return db_student

# ID로 student 찾기
def get_student_by_id(db: Session, student_id: int):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    return found_student

def get_all_students(db: Session):
    # 모든 Student 모델 가져오기
    all_students = db.query(models.Student).all()
    return all_students

def update_student(db: Session, student_id: int, student: schemas.StudentUpdate):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if found_student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    if student.name is not None:
        found_student.name = student.name
    if student.lunch_menu is not None:
        found_student.lunch_menu = student.lunch_menu
    if student.nickname is not None:
        found_student.nickname = student.nickname
    if student.description is not None:
        found_student.description = student.description
    
    db.commit()
    return found_student

def delete_student(db: Session, student_id: int):
    found_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    
    if found_student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    db.delete(found_student)
    db.commit()