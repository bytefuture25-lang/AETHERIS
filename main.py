"""
ÆTHERIS
Personal AI Operating Intelligence

Application Entry Point
"""

import sys

from app.core.app import Application
from app.core.logger import logger


def main() -> int:
    """
    Main entry point of the application.
    """
    try:
        logger.info("Starting ÆTHERIS...")

        app = Application()
        app.run()

        logger.info("ÆTHERIS exited successfully.")
        return 0

    except KeyboardInterrupt:
        logger.warning("Application interrupted by user.")
        return 0

    except Exception as error:
        logger.exception(f"Unhandled exception: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())