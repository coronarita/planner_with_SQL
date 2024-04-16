from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.users import user_router
from routes.events import event_router
from database.connection import conn # 함수 임포트
from contextlib import asynccontextmanager

import uvicorn

# @app.on_event("startup") 의 용례가 바뀜(Deprecated)
# @app.on_event("startup")
@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # Execute to make database
    conn()
    yield # discriminate startup and shutdown with keword yield
    
    # What to execute after shutdown
    
app = FastAPI(lifespan=lifespan)

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
    
@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                reload=True)