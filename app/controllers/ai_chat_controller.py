from __future__ import annotations

from typing import Iterator

from app.ai.conversation import Conversation
from app.ai.router import AIRouter


class AIChatController:
    """
    Handles AI Chat requests.
    """

    def __init__(self, router: AIRouter):
        self.router = router
        self.conversation = Conversation()

    # =====================================================
    # Normal Chat
    # =====================================================

    def send_message(self, message: str) -> str:
        """
        Send a message and return the complete response.
        """

        message = message.strip()
        if not message:
            return ""

        self.conversation.add_user(message)

        prompt = self.conversation.to_ollama_messages()
        response = self.router.chat(prompt)

        response = str(response).strip()
        if not response:
            raise RuntimeError("Empty response received from AI provider.")

        self.conversation.add_assistant(response)
        return response

    # =====================================================
    # Streaming Chat
    # =====================================================

    def stream_message(self, message: str) -> Iterator[str]:
        """
        Stream the AI response.
        """

        message = message.strip()
        if not message:
            return

        self.conversation.add_user(message)

        prompt = self.conversation.to_ollama_messages()
        assistant_reply = ""

        for chunk in self.router.stream_chat(prompt):
            if not chunk:
                continue

            assistant_reply += chunk
            yield chunk

        assistant_reply = assistant_reply.strip()
        if not assistant_reply:
            raise RuntimeError("Empty streamed response received from AI provider.")

        self.conversation.add_assistant(assistant_reply)

    # =====================================================
    # Conversation
    # =====================================================

    def clear_conversation(self):
        """
        Clear current conversation.
        """

        self.conversation.clear()