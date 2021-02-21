from os import environ


def load_var(var_name, def_value=None):
    return environ.get(var_name, def_value)


class Config:
    """Config class for variables."""

    LOGGER = True
    TOKEN = load_var("TOKEN")
    APP_ID = int(load_var("APP_ID"))
    API_HASH = load_var("API_HASH")
    OWNER_ID = int(load_var("OWNER_ID"))
    PREFIX_HANDLER = load_var("PREFIX_HANDLER", "/").split()
    WORKERS = int(load_var("WORKERS", 16))


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    TOKEN = "YOUR TOKEN"
    APP_ID = 12345  # Your APP_ID from Telegram
    API_HASH = "YOUR TOKEN"  # Your APP_HASH from Telegram
    OWNER_ID = "YOUR TOKEN"
    PREFIX_HANDLER = ["!", "/"]
    WORKERS = 8
