from database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# String    => 고정된 길이 (길이 제한)
# Text      => 길이 제한 X

class Teacher(Base):
    __tablename__ = 'teachers'
    
    # 컬럼 설정
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    is_active = Column(Boolean, default=True)
    description = Column(Text)
    
    # Student와 관계 설정 - 1 Teacher는 Many Students를 가질 수 있음
    # students = relationship("Student", back_populates="teacher")

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    nickname = Column(String(50))
    lunch_menu = Column(String(100))
    description = Column(Text)

    # 관계 설정 가능 (ex. 일대다)
    # FK
    # teacher_id = Column(Integer, ForeignKey('teachers.id'))

    # Teacher와 관계 설정 - 1 Student는 1 선생님에게 속함
    # teacher = relationship("Teacher", back_populates="students")
