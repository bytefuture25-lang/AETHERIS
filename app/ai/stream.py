from dataclasses import dataclass


@dataclass
class StreamChunk:
    """
    Represents a streamed AI response chunk.
    """

    text: str
    finished: bool = False