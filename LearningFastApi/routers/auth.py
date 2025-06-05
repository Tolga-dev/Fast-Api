from http.client import HTTPException

from fastapi import status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from LearningFastApi import oauth2
from LearningFastApi.model import models
from LearningFastApi.db.database import get_db
from LearningFastApi.schema import schemas
from LearningFastApi.utility import utilities
from SqlAlchemy.main import Session

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login", status_code=status.HTTP_201_CREATED, response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    
    if not user:
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    
    if not utilities.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=403, detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data= {"user_id": user.id})    
    
    return {"access_token": access_token, "token_type": "bearer"}
