from datetime import datetime

import logfire
from pydantic import BaseModel

logfire.configure()
logfire.instrument_pydantic()


class DeliveryModel(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]

m = DeliveryModel(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(m.timestamp)
print(m.dimensions)
