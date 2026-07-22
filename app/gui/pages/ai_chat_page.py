from PySide6.QtCore import QThread

from app.ai.providers.ollama_provider import OllamaProvider
from app.ai.registry import ProviderRegistry
from app.ai.router import AIRouter

from app.controllers.ai_chat_controller import AIChatController

from app.gui.pages.base_page import BasePage

from app.gui.components.chat.chat_header import ChatHeader
from app.gui.components.chat.chat_history import ChatHistory
from app.gui.components.chat.chat_input import ChatInput

from app.gui.workers.ai_worker import AIWorker


class AIChatPage(BasePage):
    """
    ÆTHERIS AI Chat Page
    """

    def __init__(self):
        super().__init__(
            "AI Chat",
            "Talk with your local AI assistant",
        )

        # ==================================================
        # AI Backend
        # ==================================================

        registry = ProviderRegistry()
        registry.register(OllamaProvider())

        router = AIRouter(registry)
        router.use("Ollama")

        self.controller = AIChatController(router)

        # ==================================================
        # UI
        # ==================================================

        self.header = ChatHeader()
        self.history = ChatHistory()
        self.input = ChatInput()

        self.content_layout.addWidget(self.header)
        self.content_layout.addWidget(self.history, 1)
        self.content_layout.addWidget(self.input)

        self.input.message_sent.connect(self.send_message)

        self.thread = None
        self.worker = None

    # ==================================================
    # Send Message
    # ==================================================

    def send_message(self, message: str):
        message = message.strip()

        if not message:
            return

        # Prevent duplicate requests while one is running
        if self.thread is not None:
            return

        # Add user message
        self.history.add_user_message(message)

        # Clear input
        self.input.input.clear()

        # Show typing indicator
        self.history.show_typing()

        # Disable UI
        self.input.send_button.setEnabled(False)
        self.input.input.setEnabled(False)

        # Thread
        self.thread = QThread()

        self.worker = AIWorker(
            controller=self.controller,
            message=message,
            streaming=True,
        )

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        # Streaming
        self.worker.chunk.connect(self.on_chunk)

        # Finish
        self.worker.finished.connect(self.on_response)

        # Error
        self.worker.error.connect(self.on_error)

        # Thread cleanup
        self.worker.finished.connect(self.thread.quit)
        self.worker.error.connect(self.thread.quit)

        self.thread.finished.connect(self.cleanup_thread)

        self.thread.start()

    # ==================================================
    # Streaming
    # ==================================================

    def on_chunk(self, chunk: str):
        self.history.append_ai_stream(chunk)

    # ==================================================
    # Success
    # ==================================================

    def on_response(self, response: str):
        self.history.hide_typing()
        self.history.finish_ai_stream()

        # In streaming mode, the bubble is already filled by on_chunk().
        # If you ever switch streaming=False, this keeps it usable too.
        if self.worker and not self.worker.streaming:
            if response.strip():
                self.history.add_ai_message(response)
            else:
                self.history.add_ai_message("⚠️ Empty response received.")

        self.input.send_button.setEnabled(True)
        self.input.input.setEnabled(True)
        self.input.input.setFocus()

    # ==================================================
    # Error
    # ==================================================

    def on_error(self, error: str):
        self.history.hide_typing()
        self.history.finish_ai_stream()

        self.history.add_ai_message(
            "❌ Error\n\n" + error
        )

        self.input.send_button.setEnabled(True)
        self.input.input.setEnabled(True)
        self.input.input.setFocus()

    # ==================================================
    # Cleanup
    # ==================================================

    def cleanup_thread(self):
        if self.worker is not None:
            self.worker.deleteLater()
            self.worker = None

        if self.thread is not None:
            self.thread.deleteLater()
            self.thread = None