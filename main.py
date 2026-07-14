import sys

from app.core.app import Application
from app.core.logger import logger


def main():

    try:

        logger.info("Starting ÆTHERIS...")

        app = Application()

        exit_code = app.run()

        logger.info("Application closed.")

        return exit_code

    except Exception:

        logger.exception("Fatal startup error.")

        return 1


if __name__ == "__main__":
    sys.exit(main())