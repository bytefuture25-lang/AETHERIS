from __future__ import annotations

from app.memory.models import MemoryItem


class SessionMemory:
    """
    In-memory memory store for the current session only.
    """

    def __init__(self):
        self.items: list[MemoryItem] = []

    def add(self, item: MemoryItem) -> None:
        self.items.append(item)

    def clear(self) -> None:
        self.items.clear()

    def all(self) -> list[MemoryItem]:
        return list(self.items)

    def search(self, query: str, limit: int = 10) -> list[MemoryItem]:
        query = query.strip().lower()
        if not query:
            return self.items[-limit:]

        scored: list[tuple[int, MemoryItem]] = []
        for item in self.items:
            hay = f"{item.key} {item.value} {item.category.value}".lower()
            score = 0
            for token in query.split():
                if token in hay:
                    score += 1
            if score > 0:
                scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:limit]]