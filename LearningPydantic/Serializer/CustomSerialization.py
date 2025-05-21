from datetime import datetime, timedelta, timezone
from typing import Any

from pydantic import BaseModel, ConfigDict, field_serializer, model_serializer


#  @field_serializer('dt')
class WithCustomEncoders(BaseModel):
    model_config = ConfigDict(ser_json_timedelta='iso8601')

    dt: datetime
    diff: timedelta

    @field_serializer('dt')
    def serialize_dt(self, dt: datetime, _info):
        return dt.timestamp()


m = WithCustomEncoders(
    dt=datetime(2032, 6, 1, tzinfo=timezone.utc), diff=timedelta(hours=100)
)
print(m.model_dump_json())


# use model serializer
class Model(BaseModel):
    x : str
    
    @model_serializer
    def serialize_x(self) -> dict[str, Any]:
        return {'x': f'done {self.x}'}

print(Model(x='test value').model_dump_json())