from app.services.system_monitor import SystemMonitorService

print("CPU:", SystemMonitorService.get_cpu_usage())

print("RAM:", SystemMonitorService.get_ram_usage())

print("DISK:", SystemMonitorService.get_disk_usage())

print("HOST:", SystemMonitorService.get_hostname())

print("OS:", SystemMonitorService.get_os())

print("PYTHON:", SystemMonitorService.get_python_version())

print("CPU NAME:", SystemMonitorService.get_processor())