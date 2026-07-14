from pathlib import Path

from loguru import logger

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "aetheris.log"

# Remove default logger
logger.remove()

# Console Logger
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan> - "
           "<level>{message}</level>",
)

# File Logger
logger.add(
    LOG_FILE,
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    encoding="utf-8",
)

__all__ = ["logger"]