from app.services.system_monitor import SystemMonitorService
from app.services.internet_service import InternetService


class DashboardController:
    """
    Handles all dashboard data and acts as the bridge
    between the GUI and backend services.
    """

    def __init__(self):
        # Services
        self.system = SystemMonitorService()
        self.internet = InternetService()

    def get_dashboard_data(self):
        """
        Collect all dashboard information in one place.
        """

        return {
            # ------------------------
            # System Information
            # ------------------------
            "cpu": self.system.get_cpu_usage(),
            "ram": self.system.get_ram_usage(),
            "disk": self.system.get_disk_usage(),
            "hostname": self.system.get_hostname(),
            "os": self.system.get_os(),
            "python": self.system.get_python_version(),
            "processor": self.system.get_processor(),

            # ------------------------
            # Network
            # ------------------------
            "internet": self.internet.get_status(),
        }