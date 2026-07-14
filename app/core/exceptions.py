"""
ÆTHERIS Custom Exceptions

Centralized exception hierarchy for the application.
"""


class AetherisError(Exception):
    """Base exception for all ÆTHERIS errors."""


class ConfigurationError(AetherisError):
    """Raised when configuration loading or validation fails."""


class LoggerError(AetherisError):
    """Raised when logger initialization fails."""


class GUIError(AetherisError):
    """Raised for GUI related errors."""


class VoiceError(AetherisError):
    """Raised for voice engine errors."""


class AIRouterError(AetherisError):
    """Raised for AI routing errors."""


class MemoryError(AetherisError):
    """Raised for memory subsystem errors."""


class PluginError(AetherisError):
    """Raised for plugin related errors."""


class AutomationError(AetherisError):
    """Raised for Windows automation errors."""


class SecurityError(AetherisError):
    """Raised for security related issues."""