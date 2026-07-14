from app.config import settings

print(settings.get("application", "name"))
print(settings.get("application", "version"))
print(settings.get("theme", "mode?"))
