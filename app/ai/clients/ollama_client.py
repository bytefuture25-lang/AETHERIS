"""
ÆTHERIS Ollama Client
Handles all communication with the local Ollama server.
"""

from __future__ import annotations

import json
from typing import Iterator, Union, Any

import requests


PromptInput = Union[str, list[dict[str, str]]]


class OllamaClient:
    """
    Low-level client for communicating with Ollama.
    """

    BASE_URL = "http://127.0.0.1:11434"
    DEFAULT_TIMEOUT = (5, 300)

    DEFAULT_OPTIONS: dict[str, Any] = {
        "temperature": 0.4,
        "num_predict": 1536,
        "top_p": 0.9,
        "repeat_penalty": 1.1,
    }

    def __init__(
        self,
        model: str = "qwen3:4b",
        base_url: str | None = None,
        timeout: tuple[int, int] | None = None,
        options: dict[str, Any] | None = None,
    ):
        self.model = model
        self.base_url = (base_url or self.BASE_URL).rstrip("/")
        self.timeout = timeout or self.DEFAULT_TIMEOUT

        self.options = dict(self.DEFAULT_OPTIONS)
        if options:
            self.options.update(options)

        self.session = requests.Session()

    def close(self) -> None:
        self.session.close()

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    # ======================================================
    # Helpers
    # ======================================================

    def _normalize_messages(self, prompt: PromptInput) -> list[dict[str, str]]:
        if isinstance(prompt, str):
            prompt = [
                {
                    "role": "user",
                    "content": prompt,
                }
            ]

        messages: list[dict[str, str]] = []

        for item in prompt:
            if isinstance(item, dict):
                role = str(item.get("role", "user")).strip() or "user"
                content = str(item.get("content", "")).strip()
            else:
                role = str(getattr(item, "role", "user")).strip() or "user"
                content = str(getattr(item, "content", "")).strip()

            if not content:
                continue

            if role not in {"system", "user", "assistant", "tool"}:
                role = "user"

            messages.append(
                {
                    "role": role,
                    "content": content,
                }
            )

        if not messages:
            raise ValueError("No valid messages were provided to Ollama.")

        return messages

    def _build_payload(
        self,
        messages: list[dict[str, str]],
        *,
        stream: bool,
    ) -> dict[str, Any]:
        return {
            "model": self.model,
            "messages": messages,
            "stream": stream,
            "options": dict(self.options),
        }

    # ======================================================
    # Health Check
    # ======================================================

    def is_running(self) -> bool:
        try:
            response = self.session.get(
                f"{self.base_url}/api/tags",
                timeout=(3, 3),
            )
            return response.status_code == 200
        except Exception:
            return False

    # ======================================================
    # Normal Chat
    # ======================================================

    def chat(self, prompt: PromptInput) -> str:
        messages = self._normalize_messages(prompt)
        payload = self._build_payload(messages, stream=False)

        try:
            response = self.session.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()

            data = response.json()
            message = data.get("message") or {}

            content = str(message.get("content", "") or "").strip()
            done_reason = data.get("done_reason")
            thinking = str(message.get("thinking", "") or "").strip()

            if content:
                return content

            if done_reason == "length":
                raise RuntimeError(
                    "Ollama stopped because the output limit was reached "
                    "before a final answer was produced. "
                    "Increase num_predict or shorten the prompt/history."
                )

            if thinking:
                raise RuntimeError(
                    "Ollama returned thinking text but no final answer. "
                    "Try reducing history or increasing num_predict."
                )

            raise RuntimeError("Ollama returned an empty response.")

        except Exception as e:
            raise RuntimeError(f"Ollama chat failed:\n{e}")

    # ======================================================
    # Streaming Chat
    # ======================================================

    def stream_chat(self, prompt: PromptInput) -> Iterator[str]:
        messages = self._normalize_messages(prompt)
        payload = self._build_payload(messages, stream=True)

        try:
            with self.session.post(
                f"{self.base_url}/api/chat",
                json=payload,
                stream=True,
                timeout=self.timeout,
            ) as response:
                response.raise_for_status()

                saw_content = False

                for line in response.iter_lines(decode_unicode=True):
                    if not line:
                        continue

                    try:
                        data = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    message = data.get("message") or {}
                    chunk = str(message.get("content", "") or "")

                    if chunk:
                        saw_content = True
                        yield chunk

                    if data.get("done", False):
                        if data.get("done_reason") == "length" and not saw_content:
                            raise RuntimeError(
                                "Ollama stopped because the output limit was reached "
                                "before any streamed answer was produced. "
                                "Increase num_predict or shorten the prompt/history."
                            )
                        break

        except Exception as e:
            raise RuntimeError(f"Ollama streaming failed:\n{e}")

    # ======================================================
    # Available Models
    # ======================================================

    def get_models(self) -> list[str]:
        try:
            response = self.session.get(
                f"{self.base_url}/api/tags",
                timeout=(3, 3),
            )
            response.raise_for_status()

            data = response.json()

            return [
                model.get("name", "")
                for model in data.get("models", [])
                if model.get("name")
            ]

        except Exception:
            return []