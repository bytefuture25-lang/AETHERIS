"""
ÆTHERIS AI Router
Routes AI requests to the active provider.
"""

from __future__ import annotations

from typing import Iterator

from app.ai.provider import PromptInput
from app.ai.registry import ProviderRegistry


class AIRouter:
    """
    Central AI Router.
    Every AI request passes through here.
    """

    def __init__(self, registry: ProviderRegistry):
        self.registry = registry
        self.current_provider = None
        self.current_provider_name: str | None = None

    # =====================================================
    # Provider Selection
    # =====================================================

    def use(self, provider_name: str):
        provider = self.registry.get(provider_name)

        if provider is None:
            raise ValueError(f"Unknown provider: {provider_name}")

        self.current_provider = provider
        self.current_provider_name = provider_name

    # =====================================================
    # Active Provider
    # =====================================================

    def provider(self):
        return self.current_provider

    def _require_provider(self):
        if self.current_provider is None:
            raise RuntimeError("No AI provider selected.")

    # =====================================================
    # Normal Chat
    # =====================================================

    def chat(self, prompt: PromptInput) -> str:
        self._require_provider()
        return self.current_provider.chat(prompt)

    # =====================================================
    # Streaming Chat
    # =====================================================

    def stream_chat(self, prompt: PromptInput) -> Iterator[str]:
        self._require_provider()
        yield from self.current_provider.stream_chat(prompt)