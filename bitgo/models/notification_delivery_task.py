from dataclasses import dataclass
from uuid import uuid4
from models.notifications import Notification
from enum import IntEnum
from time import time

class NotificationDeliveryStatus(IntEnum):
    PENDING = 1
    SENT = 2
    FAILED = 3


@dataclass
class NotificationDeliveryTask:
    id: str = str(uuid4())
    created_at: float = time()
    delivered_at: float = time()
    notification: Notification = None
    email_id: str = None
    status: NotificationDeliveryStatus = NotificationDeliveryStatus.PENDING
