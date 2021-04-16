"""Initialise the directory."""

from datetime import datetime
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger
from os import environ, mkdir, path
from sys import exit as sysexit
from sys import stdout, version_info

LOG_DATETIME = datetime.now().strftime("%d_%m_%Y-%H_%M_%S")
LOGDIR = f"{__name__}/logs"

# Make Logs directory if it does not exixts
if not path.isdir(LOGDIR):
    mkdir(LOGDIR)

LOGFILE = f"{LOGDIR}/{__name__}_{LOG_DATETIME}.txt"

file_handler = FileHandler(filename=LOGFILE)
stdout_handler = StreamHandler(stdout)

basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=INFO,
    handlers=[file_handler, stdout_handler],
)

getLogger("pyrogram").setLevel(WARNING)
LOGGER = getLogger(__name__)

# if version < 3.6, stop bot.
if version_info[0] < 3 or version_info[1] < 7:
    LOGGER.error(
        (
            "You MUST have a Python Version of at least 3.7!\n"
            "Multiple features depend on this. Bot quitting."
        ),
    )
    sysexit(1)  # Quit the Script

# the secret configuration specific things
try:
    if environ.get("ENV"):
        from .vars import Config
    else:
        from .vars import Development as Config
except BaseException as ef:
    LOGGER.error(ef)  # Print Error
    sysexit(1)


TOKEN = Config.TOKEN
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
OWNER_ID = Config.OWNER_ID
PREFIX_HANDLER = Config.PREFIX_HANDLER
NO_LOAD = Config.NO_LOAD
WORKERS = Config.WORKERS
