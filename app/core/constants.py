"""
ÆTHERIS Core Constants

This module contains application-wide constant values.
These values should not be modified during runtime.
"""

from pathlib import Path

# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "ÆTHERIS"
APP_VERSION = "0.1.0"
APP_CODENAME = "Genesis"

APP_DESCRIPTION = "Personal AI Operating Intelligence"

APP_AUTHOR = "Harsh Kumar Sharma"

APP_LICENSE = "MIT"

# ==========================================================
# Directory Paths
# ==========================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

APP_DIR = ROOT_DIR / "app"

CONFIG_DIR = APP_DIR / "config"

DATA_DIR = ROOT_DIR / "data"

LOG_DIR = ROOT_DIR / "logs"

MODELS_DIR = ROOT_DIR / "models"

PLUGINS_DIR = ROOT_DIR / "plugins"

ASSETS_DIR = ROOT_DIR / "assets"

DOCS_DIR = ROOT_DIR / "docs"

# ==========================================================
# Supported Platforms
# ==========================================================

SUPPORTED_OS = [
    "Windows"
]

# ==========================================================
# Supported AI Providers
# ==========================================================

SUPPORTED_AI_MODELS = [
    "Claude",
    "ChatGPT",
    "Gemini",
    "DeepSeek",
    "Qwen",
    "Ollama",
    "LM Studio",
    "Local Llama"
]

# ==========================================================
# Theme
# ==========================================================

DEFAULT_THEME = "dark"

DEFAULT_LANGUAGE = "en"

# ==========================================================
# Logging
# ==========================================================

DEFAULT_LOG_LEVEL = "INFO"

# ==========================================================
# Project Status
# ==========================================================

PROJECT_STATUS = "Development"

CURRENT_PHASE = "Core Foundation"