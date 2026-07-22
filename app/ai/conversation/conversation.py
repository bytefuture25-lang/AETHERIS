from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from app.ai.conversation.message import Message


DEFAULT_SYSTEM_PROMPT = """
You are ÆTHERIS, a private local AI operating intelligence.

Identity:
- Your name is ÆTHERIS.
- You are a helpful desktop AI assistant.
- You run locally and prioritize privacy.

Personality:
- Be clear, calm, confident, and useful.
- Keep replies natural and direct.
- Be friendly, but not overly chatty.
- When asked your name, say: "My name is ÆTHERIS."

Behavior:
- Answer the user’s question first.
- Do not reveal internal reasoning, hidden analysis, or chain-of-thought.
- Do not output long thinking text.
- If the user asks something simple, keep the answer short.
- If the user asks for code, provide clean working code.
- If the user asks for explanations, keep them structured and practical.

Memory:
- Use conversation context when relevant.
- Remember the current conversation only inside this session unless persistence is added later.

Safety:
- Do not pretend to have abilities you do not have.
- If a task is not supported, say so clearly.
- If something is uncertain, say that clearly.
""".strip()


@dataclass
class ConversationConfig:
    system_prompt: str = DEFAULT_SYSTEM_PROMPT
    max_messages: int = 20


class Conversation:
    """
    Stores one active conversation.
    """

    def __init__(
        self,
        system_prompt: str | None = None,
        max_messages: int = 20,
    ):
        self.config = ConversationConfig(
            system_prompt=(system_prompt or DEFAULT_SYSTEM_PROMPT).strip(),
            max_messages=max(1, int(max_messages)),
        )
        self.messages: list[Message] = []

    # ------------------------------
    # System Prompt
    # ------------------------------

    @property
    def system_prompt(self) -> str:
        return self.config.system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str) -> None:
        self.config.system_prompt = value.strip()

    def set_system_prompt(self, text: str) -> None:
        self.config.system_prompt = text.strip()

    # ------------------------------
    # Internal
    # ------------------------------

    def _trim_history(self) -> None:
        max_messages = self.config.max_messages
        if len(self.messages) > max_messages:
            overflow = len(self.messages) - max_messages
            del self.messages[:overflow]

    # ------------------------------
    # Add Messages
    # ------------------------------

    def add_user(self, text: str) -> None:
        text = text.strip()
        if not text:
            return

        self.messages.append(
            Message(
                role="user",
                content=text,
                timestamp=datetime.now(),
            )
        )
        self._trim_history()

    def add_assistant(self, text: str) -> None:
        text = text.strip()
        if not text:
            return

        self.messages.append(
            Message(
                role="assistant",
                content=text,
                timestamp=datetime.now(),
            )
        )
        self._trim_history()

    # ------------------------------
    # History Helpers
    # ------------------------------

    def clear(self) -> None:
        self.messages.clear()

    def last_messages(self, limit: int = 10) -> list[Message]:
        if limit <= 0:
            return []
        return self.messages[-limit:]

    def to_ollama_messages(
        self,
        include_system: bool = True,
        limit: int | None = None,
    ) -> list[dict[str, str]]:
        payload: list[dict[str, str]] = []

        if include_system and self.system_prompt:
            payload.append(
                {
                    "role": "system",
                    "content": self.system_prompt,
                }
            )

        source_messages = self.messages if limit is None else self.messages[-limit:]

        for msg in source_messages:
            content = msg.content.strip()
            if not content:
                continue

            payload.append(
                {
                    "role": msg.role,
                    "content": content,
                }
            )

        return payload