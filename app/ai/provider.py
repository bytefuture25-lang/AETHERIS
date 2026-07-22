"""
ÆTHERIS AI Provider Base
"""

from typing import Iterator, Union


PromptInput = Union[str, list[dict[str, str]]]


class AIProvider:
    """
    Base class for every AI provider.

    Concrete providers can support:
    - chat()
    - stream_chat()
    - models()
    - is_available()
    """

    def __init__(self, name: str):
        self.name = name

    def is_available(self) -> bool:
        raise NotImplementedError

    def chat(self, prompt: PromptInput) -> str:
        raise NotImplementedError

    def stream_chat(self, prompt: PromptInput) -> Iterator[str]:
        raise NotImplementedError

    def models(self) -> list[str]:
        raise NotImplementedError