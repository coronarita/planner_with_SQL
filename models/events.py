from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int             # id : 자동 생성되는 고유 식별자
    title: str          # title : 이벤트 타이틀
    image: str          # image : 이벤트 이미지 배너의 링크
    description: str    # description : 이벤트 설명
    tags: List[str]     # tags: 그룹화를 위한 이벤트 태그
    location: str       # location : 이벤트 위치
    
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