from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

# 기존 모델 클래스를 SQL테이블 클래스로 변경
class Event(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True) # id : 자동 생성되는 고유 식별자
    title: str          # title : 이벤트 타이틀
    image: str          # image : 이벤트 이미지 배너의 링크
    description: str    # description : 이벤트 설명
    tags: List[str] = Field(sa_column=Column(JSON)) # tags: 그룹화를 위한 이벤트 태그
    location: str       # location : 이벤트 위치
    
    model_config = {
        "arbitrary_types_allowed": True,
        "json_schema_extra": {
            "example":
                {
                 "title": "FastAPI Book Launch",
                 "image": "https://linktomyimage.com/image.png",
                 "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                 "tags": ["python", "fastapi", "book", "launch"],
                 "location": "Google Meet",   
                }
        }
    }

# UPDATE 처리의 바디 유형으로 추가
class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
        
    model_config = {
        "json_schema_extra": {
            "example":
                {
                 "title": "FastAPI Book Launch",
                 "image": "https://linktomyimage.com/image.png",
                 "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                 "tags": ["python", "fastapi", "book", "launch"],
                 "location": "Google Meet",   
                }
        }
    }