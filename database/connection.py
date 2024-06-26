from sqlmodel import SQLModel, Session, create_engine
from models.events import Event

# 데이터베이스 파일의 위치, 연결 문자열, 생성된 SQL 데이터베이스의 인스턴스를 변수에 저장
database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"
connect_args = {"check_same_thread": False}
engine_url = create_engine(database_connection_string, echo=True, connect_args=connect_args)

# 데이터베이스와 테이블 생성
def conn():
    SQLModel.metadata.create_all(engine_url)

# 데이터베이스 세션을 애플리케이션 내에서 유지    
def get_session():
    with Session(engine_url) as session:
        yield session

