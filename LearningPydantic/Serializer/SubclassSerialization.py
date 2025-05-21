from pydantic import BaseModel, SerializeAsAny

class User(BaseModel):
    name: str
class UserLogin(User):
    password: str
class OuterModel(BaseModel):
    user: User

user = UserLogin(name='pydantic', password='hunter2')
m = OuterModel(user=user)
print(m)
print(m.model_dump())  # note: the password field is not included


