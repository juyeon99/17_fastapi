from typing import List
from pydantic import BaseModel
from typing_extensions import Optional

# request 받거나, response를 받을 때
# 기본 형식을 만들어 놓을 수 있다.
class TeacherBase(BaseModel):
    name: str
    is_active: bool
    nickname: Optional[str] = None
    description: Optional[str] = None

class StudentBase(BaseModel):
    name: str
    lunch_menu: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None

# SqlAlchemy 모델: DB의 통신을 위한 데이터 구조 정의
# Pydantic 모델: API 요청과 응답을 위한 데이터 구조 정의

# Teacher request 요청 모델
class TeacherCreate(TeacherBase):
    pass

# Student request 요청 모델
class StudentCreate(StudentBase):
    teacher_id: int

# Student response 응답 모델
class StudentResponse(StudentBase):
    id: int
    teacher_id: Optional[int]

# Teacher response 응답 모델
class TeacherResponse(TeacherBase):
    id: int
    students: List[StudentResponse]

# Teacher 업데이트 시 사용되는 모델
class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None
    nickname: Optional[str] = None
    description: Optional[str] = None

# Student 업데이트 시 사용되는 모델
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    lunch_menu: Optional[str] = None
    nickname: Optional[str] = None
    description: Optional[str] = None