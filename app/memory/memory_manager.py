from __future__ import annotations

from app.memory.models import MemoryCategory, MemoryImportance, MemoryItem
from app.memory.long_term_memory import LongTermMemory
from app.memory.session_memory import SessionMemory


class MemoryManager:
    """
    Coordinates session memory and long-term memory.
    """

    def __init__(
        self,
        session_memory: SessionMemory,
        long_term_memory: LongTermMemory,
    ):
        self.session_memory = session_memory
        self.long_term_memory = long_term_memory

    def remember(
        self,
        key: str,
        value: str,
        category: MemoryCategory = MemoryCategory.OTHER,
        importance: MemoryImportance = MemoryImportance.MEDIUM,
        persist: bool = True,
    ) -> MemoryItem:
        item = MemoryItem(
            key=key.strip(),
            value=value.strip(),
            category=category,
            importance=importance,
        )

        self.session_memory.add(item)

        if persist:
            item = self.long_term_memory.add(item)

        return item

    def recall(self, query: str, limit: int = 10) -> list[MemoryItem]:
        session_results = self.session_memory.search(query, limit=limit)
        persistent_results = self.long_term_memory.search(query, limit=limit)

        combined: list[MemoryItem] = []
        seen: set[tuple[str, str]] = set()

        for item in session_results + persistent_results:
            key = (item.key.lower(), item.value.lower())
            if key in seen:
                continue
            seen.add(key)
            combined.append(item)

        return combined[:limit]

    def clear_session(self) -> None:
        self.session_memory.clear()

    def clear_persistent(self) -> None:
        self.long_term_memory.clear()