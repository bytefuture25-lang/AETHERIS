from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Message:
    """
    Single conversation message.
    """

    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)