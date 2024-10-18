# SQLAlchemy
# 파이썬에서 사용하는 ORM(Object-Relational-Mapping) 라이브러리

# ORM
# => 객체와 관계형 DB를 연결하는 라이브러리

# 엔진 생성을 위한 함수
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite
# 파이썬에 내장되어있는 DB 라이브러리
DB_URL = 'sqlite:///todo.sqlite3'

# DB 엔진 생성
engine = create_engine(DB_URL)

# 연결 세션을 생성하기 위한 객체
# autocommit: 자동 커밋을 비활성화
# autoflush: 자동 플러시 비활성화 (플러시: 세션의 변경사항을 DB에 동기화)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델 클래스가 상속받을 기본 모델 클래스 지정
Base = declarative_base()