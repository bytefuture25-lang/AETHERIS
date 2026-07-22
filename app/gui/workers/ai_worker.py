"""
ÆTHERIS AI Worker

Runs AI requests in a background thread.

Supports:
- Normal responses
- Streaming responses
"""

from __future__ import annotations

import traceback

from PySide6.QtCore import QObject, Signal, Slot


class AIWorker(QObject):
    """
    Executes AI requests in a background thread.
    """

    finished = Signal(str)
    chunk = Signal(str)
    error = Signal(str)

    def __init__(self, controller, message, streaming=True):
        super().__init__()
        self.controller = controller
        self.message = message
        self.streaming = streaming

    @Slot()
    def run(self):
        """
        Execute the AI request.
        """

        print("\n" + "=" * 70)
        print("🤖 AIWorker Started")
        print(f"Message   : {self.message}")
        print(f"Streaming : {self.streaming}")
        print("=" * 70)

        try:
            if self.streaming:
                print("[Worker] Calling controller.stream_message()")

                full_response = ""

                for piece in self.controller.stream_message(self.message):
                    if not piece:
                        continue

                    print("[Chunk]", repr(piece))
                    full_response += piece
                    self.chunk.emit(piece)

                full_response = full_response.strip()
                if not full_response:
                    raise RuntimeError("Empty streamed response received.")

                print("[Worker] Streaming Completed")
                print("[Worker] Final Length:", len(full_response))
                self.finished.emit(full_response)

            else:
                print("[Worker] Calling controller.send_message()")

                response = self.controller.send_message(self.message)
                response = str(response).strip()

                if not response:
                    raise RuntimeError("Empty response received.")

                print("[Worker] Response Received")
                print(repr(response))
                self.finished.emit(response)

        except Exception:
            error_text = traceback.format_exc()

            print("\n" + "=" * 70)
            print("❌ AIWorker ERROR")
            print(error_text)
            print("=" * 70)

            self.error.emit(error_text)

        finally:
            print("🤖 AIWorker Finished")
            print("=" * 70 + "\n")