from sqlalchemy import Column, Integer, Boolean, Text
from database import Base

# DB에 저장될 Todo 테이블 만들기
class Todo(Base):
    # 테이블 이름 설정
    __tablename__ = 'todos'
    # 컬럼 설정
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False)
