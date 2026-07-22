from __future__ import annotations

from dataclasses import dataclass
from app.memory.models import MemoryCategory, MemoryImportance


@dataclass(frozen=True)
class MemoryRule:
    key: str
    patterns: tuple[str, ...]
    category: MemoryCategory
    importance: MemoryImportance


MEMORY_RULES: tuple[MemoryRule, ...] = (
    MemoryRule(
        key="user_name",
        patterns=(
            "my name is",
            "my name's",
        ),
        category=MemoryCategory.PERSONAL,
        importance=MemoryImportance.CRITICAL,
    ),

    MemoryRule(
        key="current_project",
        patterns=(
            "my project is",
            "i'm building",
            "i am building",
            "working on",
        ),
        category=MemoryCategory.PROJECT,
        importance=MemoryImportance.HIGH,
    ),

    MemoryRule(
        key="favorite_language",
        patterns=(
            "i like",
            "i love",
            "my favorite language is",
        ),
        category=MemoryCategory.PREFERENCE,
        importance=MemoryImportance.HIGH,
    ),

    MemoryRule(
        key="device",
        patterns=(
            "i use",
            "my laptop is",
            "my computer is",
        ),
        category=MemoryCategory.DEVICE,
        importance=MemoryImportance.MEDIUM,
    ),
)