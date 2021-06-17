from os import makedirs, path

from pyrogram import Client

from . import API_HASH, APP_ID, LOGGER, MESSAGE_DUMP, NO_LOAD, TOKEN, WORKERS

# Check if MESSAGE_DUMP is correct
if MESSAGE_DUMP == -100 or not str(MESSAGE_DUMP).startswith("-100"):
    raise Exception(
        "Please enter a vaild Supergroup ID, A Supergroup ID starts with -100",
    )


class PyroBot(Client):
    """Starts the Pyrogram Client on the Bot Token when we do 'python3 -m pyrobot'"""

    def __init__(self):
        name = self.__class__.__name__.lower()

        # Make a temporary direcory for storing session file
        SESSION_DIR = f"{name}/SESSION"
        if not path.isdir(SESSION_DIR):
            makedirs(SESSION_DIR)

        super().__init__(
            name,
            plugins=dict(root=f"{name}.plugins", exclude=NO_LOAD),
            workdir=SESSION_DIR,
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TOKEN,
            workers=WORKERS,
        )

    async def start(self):
        """Start the bot."""
        await super().start()
        await self.send_message(MESSAGE_DUMP, "Bot Started!")
        LOGGER.info("Bot Started Successfully!")

    async def stop(self):
        """Stop the bot and send a message to MESSAGE_DUMP telling that the bot has stopped."""
        LOGGER.info("Uploading logs before stopping...!")
        await self.send_message(MESSAGE_DUMP, "Bot Stopped!")
        await super().stop()
        LOGGER.info("Bot Stopped.\nkthxbye!")
