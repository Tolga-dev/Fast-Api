﻿import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from LearningFastApi.model import models
from LearningFastApi.db.database import engine
from LearningFastApi.routers import post, user, auth, vote

# models.base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

app.include_router(vote.router)

@app.get("/")
async def root_hello_world():
    return {"message": "Hello World"}


# if __name__ == "__main__":
#     uvicorn.run("E2:app", host="127.0.0.1", port=8000, reload=True)

