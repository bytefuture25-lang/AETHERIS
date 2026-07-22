from __future__ import annotations

from app.memory.models import (
    MemoryCategory,
    MemoryImportance,
    MemoryItem,
)
from app.memory.rules import MemoryRule


class MemoryClassifier:
    """
    Converts an extracted value into a MemoryItem.
    """

    @staticmethod
    def classify(
        rule: MemoryRule,
        value: str,
    ) -> MemoryItem:
        """
        Build a MemoryItem using the matched rule.
        """

        value = value.strip()

        return MemoryItem(
            key=rule.key,
            value=value,
            category=rule.category,
            importance=rule.importance,
            source="conversation",
        )

    @staticmethod
    def is_valid(value: str | None) -> bool:
        """
        Basic validation before saving.
        """

        if value is None:
            return False

        value = value.strip()

        if len(value) == 0:
            return False

        if len(value) > 200:
            return False

        invalid_values = {
            "yes",
            "no",
            "ok",
            "okay",
            "hello",
            "hi",
        }

        if value.lower() in invalid_values:
            return False

        return True