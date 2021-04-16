from time import time

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import PREFIX_HANDLER
from ..bot_class import PyroBot

__PLUGIN__ = "Test Plugin"

__help__ = """
Just a simple plugin as an example.
"""


@PyroBot.on_message(filters.command("start", PREFIX_HANDLER))
async def test_bot(_, m: Message):
    await m.reply_text("I'm Alive <3")
    return


@PyroBot.on_message(filters.command("ping", PREFIX_HANDLER))
async def test_bot(_, m: Message):
    start = time()
    replymsg = await m.reply_text("Pinging...")
    await replymsg.edit_text(
        f"<b>Pong!</b>\nTime Taken:{round(time() - start, 2)} seconds",
    )
    return


@PyroBot.on_message(filters.command("repo", PREFIX_HANDLER))
async def test_bot(_, m: Message):
    await m.reply_text(
        "You can find my repo by clicking the button below!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo 📚",
                        url="https://github.com/DivideProjects/PyroBot",
                    ),
                ],
            ],
        ),
    )
    return
