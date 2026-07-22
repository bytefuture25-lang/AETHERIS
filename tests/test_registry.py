from app.ai.registry import ProviderRegistry
from app.ai.providers.ollama_provider import OllamaProvider


registry = ProviderRegistry()

registry.register(
    OllamaProvider()
)

print("Providers:")

for provider in registry.all():
    print(provider.name)

print()

print("Available:")

for provider in registry.available():
    print(provider.name)