"""
ÆTHERIS Ollama Provider
"""

from __future__ import annotations

from typing import Iterator

from app.ai.clients.ollama_client import OllamaClient
from app.ai.provider import AIProvider, PromptInput


class OllamaProvider(AIProvider):
    """
    Ollama AI Provider.
    """

    def __init__(
        self,
        model: str = "qwen3:4b",
        client: OllamaClient | None = None,
    ):
        super().__init__("Ollama")
        self.client = client or OllamaClient(model=model)

    def is_available(self) -> bool:
        return self.client.is_running()

    def chat(self, prompt: PromptInput) -> str:
        return self.client.chat(prompt)

    def stream_chat(self, prompt: PromptInput) -> Iterator[str]:
        yield from self.client.stream_chat(prompt)

    def models(self) -> list[str]:
        return self.client.get_models()