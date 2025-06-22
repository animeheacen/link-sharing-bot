from bot import Bot
from pyrogram import filters
from pyrogram.types import Message
from config import OWNER_ID, BOT_STATS_TEXT
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    uptime = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=uptime))
