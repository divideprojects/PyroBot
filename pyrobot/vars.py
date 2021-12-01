from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    TOKEN = config("TOKEN")
    APP_ID = int(config("APP_ID"))
    API_HASH = config("API_HASH")
    OWNER_ID = int(config("OWNER_ID"))
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/ !").split()
    NO_LOAD = config("NO_LOAD", default=[])
    WORKERS = int(config("WORKERS", default=8))


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    TOKEN = "YOUR TOKEN"
    APP_ID = 12345  # Your APP_ID from Telegram
    API_HASH = "YOUR TOKEN"  # Your APP_HASH from Telegram
    OWNER_ID = "YOUR TOKEN"
    PREFIX_HANDLER = ["!", "/"]
    NO_LOAD = []
    WORKERS = 8
