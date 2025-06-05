from fastapi import APIRouter, status, Depends, HTTPException

from LearningFastApi import oauth2
from LearningFastApi.db.database import get_db
from LearningFastApi.model import models
from LearningFastApi.schema.schemas import Vote
from SqlAlchemy.main import Session

router = APIRouter(
    prefix="/vote",
    tags=["vote"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: Vote, db: Session = Depends(get_db),
                        current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter_by(models.Post.id==vote.post_id).first()
    
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    
    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, 
        models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()
    
    if(vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=409, detail="Vote conflict")
         
        new_vote = models.Vote(post_id=vote.post_id, user_id= current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added"}
    else: 
        if not found_vote:
            raise HTTPException(status_code=404, detail="Vote not found")
        
        vote_query.delete(synchronize_session=False)
        db.commit()
        
        return {"message": "Vote deleted"}
        