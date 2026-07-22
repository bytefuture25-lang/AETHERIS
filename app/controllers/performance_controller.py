from app.services.system_monitor import SystemMonitorService


class PerformanceController:
    """
    Handles all live performance data.
    """

    def __init__(self):
        self.system = SystemMonitorService()

    def get_performance_data(self):
        """
        Returns all live system statistics.
        """

        ram = self.system.get_ram_usage()
        disk = self.system.get_disk_usage()

        return {
            "cpu": self.system.get_cpu_usage(),

            "ram": {
                "percent": ram["percent"],
                "used": ram["used_gb"],
                "total": ram["total_gb"],
            },

            "disk": {
                "percent": disk["percent"],
            },

            "internet": self.system.check_internet(),

            "hostname": self.system.get_hostname(),

            "os": self.system.get_os(),

            "python": self.system.get_python_version(),
        }