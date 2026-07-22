from __future__ import annotations

import re


class MemoryParser:
    """
    Extracts values from user messages based on matched patterns.
    """

    @staticmethod
    def parse(pattern: str, text: str) -> str | None:
        """
        Example:
            pattern = "my name is"
            text = "My name is Harsh"

            Returns:
                "Harsh"
        """

        if not pattern or not text:
            return None

        pattern = pattern.strip().lower()
        original = text.strip()

        lower = original.lower()

        index = lower.find(pattern)

        if index == -1:
            return None

        value = original[index + len(pattern):].strip()

        value = re.sub(r"^[\s:=-]+", "", value)
        value = re.sub(r"[.!?]+$", "", value)

        value = value.strip()

        if not value:
            return None

        return value