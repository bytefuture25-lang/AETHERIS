from __future__ import annotations

from app.memory.models import MemoryItem
from app.memory.sqlite_store import SQLiteMemoryStore


class LongTermMemory:
    """
    Persistent memory access layer.
    """

    def __init__(self, store: SQLiteMemoryStore):
        self.store = store

    def add(self, item: MemoryItem) -> MemoryItem:
        return self.store.add_memory(item)

    def update(self, item: MemoryItem) -> None:
        self.store.update_memory(item)

    def delete(self, memory_id: int) -> None:
        self.store.delete_memory(memory_id)

    def clear(self) -> None:
        self.store.clear_memories()

    def all(self, limit: int = 100) -> list[MemoryItem]:
        return self.store.list_memories(limit=limit)

    def search(self, query: str, limit: int = 10) -> list[MemoryItem]:
        return self.store.search_memories(query, limit=limit)

    def find_by_key(self, key: str) -> list[MemoryItem]:
        return self.store.get_memory_by_key(key)