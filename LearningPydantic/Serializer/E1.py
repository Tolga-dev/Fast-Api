from datetime import datetime

from pydantic import BaseModel

class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str= "No idea"

m = Meeting(when='2020-01-01T12:00', where='home')

# model dump
print(m.model_dump(exclude_unset=True)) 
print(m.model_dump(include= {'why'})) 
print(m.model_dump(exclude= {'where'}))
print(m.model_dump(by_alias= True))

# model dump json
class Bar(BaseModel):
    Bar: Meeting
    foo: int

m = Bar(Bar=m, foo = 3)
print(m.model_dump_json())
print(m.model_dump_json(indent=2))

# dict model and iteration
print(dict(m))
