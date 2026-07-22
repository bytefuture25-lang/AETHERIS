from __future__ import annotations

from pathlib import Path

from app.memory.long_term_memory import LongTermMemory
from app.memory.memory_manager import MemoryManager
from app.memory.models import MemoryCategory, MemoryImportance, MemoryItem
from app.memory.session_memory import SessionMemory
from app.memory.sqlite_store import SQLiteMemoryStore


class MemoryService:
    """
    High-level memory service used by AI logic.
    """

    def __init__(self, db_path: str | Path):
        self.session_memory = SessionMemory()
        self.store = SQLiteMemoryStore(db_path)
        self.long_term_memory = LongTermMemory(self.store)
        self.manager = MemoryManager(self.session_memory, self.long_term_memory)

    def remember(
        self,
        key: str,
        value: str,
        category: MemoryCategory = MemoryCategory.OTHER,
        importance: MemoryImportance = MemoryImportance.MEDIUM,
        persist: bool = True,
    ) -> MemoryItem:
        return self.manager.remember(
            key=key,
            value=value,
            category=category,
            importance=importance,
            persist=persist,
        )

    def recall(self, query: str, limit: int = 10) -> list[MemoryItem]:
        return self.manager.recall(query, limit=limit)

    def build_memory_context(self, query: str, limit: int = 10) -> str:
        memories = self.recall(query, limit=limit)
        if not memories:
            return ""

        lines = ["Relevant memories:"]
        for item in memories:
            lines.append(f"- {item.key}: {item.value}")
        return "\n".join(lines)

    def clear_session(self) -> None:
        self.manager.clear_session()

    def clear_persistent(self) -> None:
        self.manager.clear_persistent()