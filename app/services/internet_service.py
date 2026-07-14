import socket


class InternetService:
    """
    Check internet connectivity.
    """

    @staticmethod
    def is_online() -> bool:
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            return True
        except OSError:
            return False

    @staticmethod
    def get_status() -> str:
        return "Online" if InternetService.is_online() else "Offline"