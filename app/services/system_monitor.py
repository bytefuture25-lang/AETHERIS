"""
ÆTHERIS System Monitor Service
Provides real-time system information.
"""

import os
import platform
import socket
import psutil


class SystemMonitorService:
    """
    Service responsible for retrieving system information.
    """

    @staticmethod
    def get_cpu_usage() -> float:
        return psutil.cpu_percent(interval=0.5)

    @staticmethod
    def get_ram_usage() -> dict:
        memory = psutil.virtual_memory()

        return {
            "percent": memory.percent,
            "used_gb": round(memory.used / (1024 ** 3), 2),
            "total_gb": round(memory.total / (1024 ** 3), 2),
        }

    @staticmethod
    def get_disk_usage() -> dict:
        disk = psutil.disk_usage("/")

        return {
            "percent": disk.percent,
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "total_gb": round(disk.total / (1024 ** 3), 2),
        }

    @staticmethod
    def get_hostname() -> str:
        return socket.gethostname()

    @staticmethod
    def get_os() -> str:
        return f"{platform.system()} {platform.release()}"

    @staticmethod
    def get_python_version() -> str:
        return platform.python_version()

    @staticmethod
    def get_processor() -> str:
        return platform.processor()

    @staticmethod
    def get_boot_time():
        return psutil.boot_time()