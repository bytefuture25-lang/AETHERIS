from app.services.internet_service import InternetService

print("Checking Internet...\n")

print(
    "Internet Status:",
    InternetService.get_status()
)