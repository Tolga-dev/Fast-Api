from pydantic import BaseModel


class User(BaseModel):
    name: str
class UserLogin(User):
    password: str
class OuterModel(BaseModel):
    user: User
    
user = UserLogin(name='pydantic', password='hunter2')
m = OuterModel(user=user)
print(m.model_dump())
print(m)



