from fastapi import APIRouter, Body, HTTPException, status
from fastapi import Depends, Request
from database.connection import get_session
from models.events import Event, EventUpdate
from typing import List
from sqlmodel import select

event_router = APIRouter(
    tags=["Events"]
)

events = []

# 모든 이벤트 추출하는 라우트
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

# 특정 ID 이벤트 추출하는 라우트
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event :
        return event
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
    
# 이벤트 생성 라우트
@event_router.post("/new")
async def create_event(new_event: Event,
    session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return {
        "message": "Event created successfully."
    }

# 단일 이벤트 업데이트 라우트
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        # event_data = new_data.dict(exclude_unset=True) # Deprecated
        event_data = new_data.model_dump(exclude_unset=True)
        for key, value in event_data.items():
            # event에 존재하는 속성의 값을 새로운 값으로 업데이트 해준다. (object)
            setattr(event, key, value)    
        session.add(event)
        session.commit()
        session.refresh(event)
        
        return event
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

    
# 단일 이벤트 삭제 라우트
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()        
        return {
            "message": "Event deleted successfully."
        }    
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

# 전체 이벤트 삭제 라우트
@event_router.delete("/")
async def delete_all_events() -> dict :
    events.clear()
    return {
        "message": "Events deleted successfully."
    }
