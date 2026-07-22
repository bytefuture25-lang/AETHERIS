from app.ai.provider import AIProvider


class ProviderRegistry:
    """
    Stores and manages AI providers.
    """

    def __init__(self):
        self._providers = {}

    # ==========================================
    # Register
    # ==========================================

    def register(self, provider: AIProvider):
        """
        Register a provider.
        """

        self._providers[provider.name] = provider

    # ==========================================
    # Get Provider
    # ==========================================

    def get(self, name: str) -> AIProvider | None:
        """
        Return provider by name.
        """

        return self._providers.get(name)

    # ==========================================
    # All Providers
    # ==========================================

    def all(self):
        """
        Return all registered providers.
        """

        return list(self._providers.values())

    # ==========================================
    # Available Providers
    # ==========================================

    def available(self):
        """
        Return only available providers.
        """

        return [
            provider
            for provider in self._providers.values()
            if provider.is_available()
        ]