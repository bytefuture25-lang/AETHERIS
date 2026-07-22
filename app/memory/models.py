from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class MemoryCategory(str, Enum):
    PERSONAL = "personal"
    PREFERENCE = "preference"
    PROJECT = "project"
    DEVICE = "device"
    TASK = "task"
    FACT = "fact"
    OTHER = "other"


class MemoryImportance(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(slots=True)
class MemoryItem:
    id: int | None = None
    key: str = ""
    value: str = ""
    category: MemoryCategory = MemoryCategory.OTHER
    importance: MemoryImportance = MemoryImportance.MEDIUM
    source: str = "conversation"
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def to_prompt_line(self) -> str:
        return f"{self.key}: {self.value}"