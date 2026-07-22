from app.ai.providers.ollama_provider import (
    OllamaProvider,
)

provider = OllamaProvider()

print("Available:", provider.is_available())

print()

response = provider.chat(
    "Reply with exactly one word: Hello"
)

print(response)