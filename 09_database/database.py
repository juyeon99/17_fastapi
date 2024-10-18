# SQLAlchemy를 사용한 DB 연동

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///class.sqlite3"

# DB 엔진 설정
# sqlite는 동시에 한 스레드에서만 접근이 가능하기 때문에 여러 스레드에서 접근 가능하도록 옵션 설정
engine = create_engine(DB_URL, connect_args={"check_same_thread":False})

# DB 연결 세션 설정
session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# 모델 클래스가 상속받을 기본 모델 클래스 지정
Base = declarative_base()