from pathlib import Path
import yaml


class Settings:
    """
    Loads and provides application configuration.
    """

    def __init__(self):
        self.config_path = Path(__file__).parent / "config.yaml"
        self.data = self.load()

    def load(self):
        """
        Load configuration from YAML file.
        """
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    def get(self, *keys, default=None):
        """
        Access nested configuration values.

        Example:
        settings.get("application", "name")
        """
        value = self.data

        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                return default

            if value is None:
                return default

        return value


settings = Settings()