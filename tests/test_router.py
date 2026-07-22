from app.ai.registry import ProviderRegistry
from app.ai.router import AIRouter
from app.ai.providers.ollama_provider import OllamaProvider


registry = ProviderRegistry()

registry.register(
    OllamaProvider()
)

router = AIRouter(registry)

router.use("Ollama")

print(router.provider().name)

print()

print(
    router.chat("Hello ÆTHERIS")
)