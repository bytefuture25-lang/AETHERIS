from __future__ import annotations

import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Any

from app.memory.models import MemoryCategory, MemoryImportance, MemoryItem


class SQLiteMemoryStore:
    """
    SQLite-backed persistent memory store.
    """

    def __init__(self, db_path: str | Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key TEXT NOT NULL,
                    value TEXT NOT NULL,
                    category TEXT NOT NULL,
                    importance TEXT NOT NULL,
                    source TEXT NOT NULL DEFAULT 'conversation',
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
                """
            )
            conn.commit()

    def add_memory(self, item: MemoryItem) -> MemoryItem:
        now = datetime.now().isoformat()

        with self._connect() as conn:
            cur = conn.execute(
                """
                INSERT INTO memories
                (key, value, category, importance, source, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.key,
                    item.value,
                    item.category.value,
                    item.importance.value,
                    item.source,
                    item.created_at.isoformat(),
                    now,
                ),
            )
            conn.commit()
            item.id = cur.lastrowid
            item.updated_at = datetime.fromisoformat(now)
            return item

    def update_memory(self, item: MemoryItem) -> None:
        if item.id is None:
            raise ValueError("Cannot update memory without id.")

        now = datetime.now().isoformat()
        with self._connect() as conn:
            conn.execute(
                """
                UPDATE memories
                SET key = ?, value = ?, category = ?, importance = ?, source = ?, updated_at = ?
                WHERE id = ?
                """,
                (
                    item.key,
                    item.value,
                    item.category.value,
                    item.importance.value,
                    item.source,
                    now,
                    item.id,
                ),
            )
            conn.commit()
            item.updated_at = datetime.fromisoformat(now)

    def delete_memory(self, memory_id: int) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
            conn.commit()

    def clear_memories(self) -> None:
        with self._connect() as conn:
            conn.execute("DELETE FROM memories")
            conn.commit()

    def list_memories(self, limit: int = 100) -> list[MemoryItem]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT *
                FROM memories
                ORDER BY updated_at DESC, id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [self._row_to_item(row) for row in rows]

    def search_memories(self, query: str, limit: int = 10) -> list[MemoryItem]:
        query = query.strip()
        if not query:
            return self.list_memories(limit=limit)

        like = f"%{query}%"
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT *
                FROM memories
                WHERE key LIKE ? OR value LIKE ? OR category LIKE ? OR importance LIKE ?
                ORDER BY updated_at DESC, id DESC
                LIMIT ?
                """,
                (like, like, like, like, limit),
            ).fetchall()

        return [self._row_to_item(row) for row in rows]

    def get_memory_by_key(self, key: str) -> list[MemoryItem]:
        with self._connect() as conn:
            rows = conn.execute(
                """
                SELECT *
                FROM memories
                WHERE key = ?
                ORDER BY updated_at DESC, id DESC
                """,
                (key,),
            ).fetchall()

        return [self._row_to_item(row) for row in rows]

    def set_setting(self, key: str, value: str) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO settings (key, value)
                VALUES (?, ?)
                ON CONFLICT(key) DO UPDATE SET value = excluded.value
                """,
                (key, value),
            )
            conn.commit()

    def get_setting(self, key: str, default: str = "") -> str:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT value FROM settings WHERE key = ?",
                (key,),
            ).fetchone()

        if row is None:
            return default
        return str(row["value"])

    def _row_to_item(self, row: sqlite3.Row) -> MemoryItem:
        return MemoryItem(
            id=row["id"],
            key=row["key"],
            value=row["value"],
            category=MemoryCategory(row["category"]),
            importance=MemoryImportance(row["importance"]),
            source=row["source"],
            created_at=datetime.fromisoformat(row["created_at"]),
            updated_at=datetime.fromisoformat(row["updated_at"]),
        )