from app.ai.registry import ProviderRegistry
from app.ai.router import AIRouter

from app.ai.providers.ollama_provider import (
    OllamaProvider,
)

from app.controllers.ai_chat_controller import (
    AIChatController,
)

registry = ProviderRegistry()

registry.register(
    OllamaProvider()
)

router = AIRouter(registry)

router.use("Ollama")

controller = AIChatController(router)

print(
    controller.send_message(
        "Hello"
    )
)