from http.client import HTTPException

from fastapi import status, Depends, APIRouter
from LearningFastApi.model import models
from LearningFastApi.db.database import get_db
from LearningFastApi.schema.schemas import UserCreate, UserOut
from LearningFastApi.utility import utilities
from SqlAlchemy.main import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = utilities.user_hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", response_model=UserOut)
async def get_user(ID: int, db: Session = Depends(get_db)):
    res = db.query(models.User).filter(models.User.id == ID).first()

    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    return res
