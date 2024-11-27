from dataclasses import dataclass
from uuid import uuid4
from time import time

@dataclass
class Notification:
    id: str = str(uuid4())
    created_at: float = time()
    current_price: float = 0.0
    trading_volume: float = 0.0
    daily_percentage_change: float = 0.0
