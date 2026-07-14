class EventEngine:
    """
    Detects important dashboard events.
    """

    def __init__(self):
        self.previous = {}

    def has_changed(self, key, value):

        old = self.previous.get(key)

        self.previous[key] = value

        return old != value