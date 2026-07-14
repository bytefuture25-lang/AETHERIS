from app.core.event_engine import EventEngine

engine = EventEngine()

print(engine.has_changed("cpu", 10))

print(engine.has_changed("cpu", 10))

print(engine.has_changed("cpu", 25))

print(engine.has_changed("cpu", 25))

print(engine.has_changed("cpu", 80))