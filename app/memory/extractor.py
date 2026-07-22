from __future__ import annotations

from app.memory.classifier import MemoryClassifier
from app.memory.models import MemoryItem
from app.memory.parser import MemoryParser
from app.memory.rules import MEMORY_RULES


class MemoryExtractor:
    """
    Extracts structured memories from natural language.

    Example:

        User:
            My name is Harsh.

        Returns:

            MemoryItem(
                key="user_name",
                value="Harsh"
            )
    """

    def __init__(self):
        self.rules = MEMORY_RULES

    def extract(self, text: str) -> list[MemoryItem]:
        """
        Extract every memory found inside a message.
        """

        if not text:
            return []

        original = text.strip()
        lower = original.lower()

        results: list[MemoryItem] = []

        for rule in self.rules:

            for pattern in rule.patterns:

                if pattern not in lower:
                    continue

                value = MemoryParser.parse(pattern, original)

                if not MemoryClassifier.is_valid(value):
                    continue

                item = MemoryClassifier.classify(
                    rule,
                    value,
                )

                results.append(item)

                # Only one value per rule
                break

        return results

    def extract_first(self, text: str) -> MemoryItem | None:
        """
        Return only the first extracted memory.
        """

        memories = self.extract(text)

        if memories:
            return memories[0]

        return None

    def has_memory(self, text: str) -> bool:
        """
        Check whether a sentence contains any memory.
        """

        return len(self.extract(text)) > 0