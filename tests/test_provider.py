from app.ai.providers.ollama_provider import OllamaProvider

provider = OllamaProvider()

print(provider.name)
print(provider.is_available())
print(provider.chat("Hello"))
print(provider.models())