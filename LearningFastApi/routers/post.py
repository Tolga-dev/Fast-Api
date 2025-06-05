import json
from http.client import HTTPException
from typing import List
from fastapi import Response, status, Depends, APIRouter
from sqlalchemy import func, inspect

from LearningFastApi import oauth2
from LearningFastApi.model import models
from LearningFastApi.db.database import get_db
from LearningFastApi.schema.schemas import PostCreate, Post, PostOut
from SqlAlchemy.main import Session

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# @router.get("/", response_model=List[Post])
@router.get("/", response_model=List[PostOut])
async def get_all_posts(db: Session = Depends(get_db), 
                      current_user: int =Depends(oauth2.get_current_user),
    limit: int = 10, skip: int = 0, search: str = ""):
    # cursor.execute("""SELECT * FROM posts""")W
    # posts = cursor.fetchall()
    
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
 
    results = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .filter(models.Post.title.contains(search))
        .group_by(models.Post.id)
        .limit(limit)
        .offset(skip)
        .all()
    )

    for post, votes in results:
        post_dict = {c.key: getattr(post, c.key) for c in inspect(post).mapper.column_attrs}
        print(post_dict, votes)
    
    return results

@router.get("/{id}")
async def get_post(ID: int, response: Response, db: Session = Depends(get_db), 
                      current_user: int =Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(ID),))
    # res = cursor.fetchone()

    res = db.query(models.Post).filter(models.Post.owner_id == current_user.id).first()

    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    return res


@router.post("/", response_model=Post)
async def create_post(post: PostCreate, db: Session = Depends(get_db), 
                      current_user: int =Depends(oauth2.get_current_user)):
    
    # cursor.execute("""
    #     INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #     (post.title, post.content, post.published))
    # 
    # new_post = cursor.fetchone()
    # 
    # conn.commit()
    new_post = models.Post(owner_id = current_user.id, **post.model_dump())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.put("/{id}", response_model=Post)
async def update_post(id: int, post: PostCreate, db: Session = Depends(get_db), 
                      current_user: int =Depends(oauth2.get_current_user)):
    # cursor.execute("""
    #     UPDATE posts set title = %s, content = %s, published = %s 
    #     WHERE posts.id = %s
    #     returning * """, 
    #                (post.title, post.content, post.published, str(id)))
    # 
    # updated_post = cursor.fetchone()
    # 
    # conn.commit()

    updated_post = db.query(models.Post).filter(models.Post.id == id)

    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    updated_post.update(post.model_dump(), synchronize_session=False)

    db.commit()

    return updated_post.first()

    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(ID: int, db: Session = Depends(get_db), 
                      current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning *""", (str(ID),))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == ID)

    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Found")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

