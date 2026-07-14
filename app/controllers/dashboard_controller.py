from app.services.system_monitor import SystemMonitorService


class DashboardController:
    """
    Handles dashboard data.
    """

    def __init__(self):
        self.system = SystemMonitorService()

    def get_dashboard_data(self):
        return {
            "cpu": self.system.get_cpu_usage(),
            "ram": self.system.get_ram_usage(),
            "disk": self.system.get_disk_usage(),
            "hostname": self.system.get_hostname(),
            "os": self.system.get_os(),
            "python": self.system.get_python_version(),
        }