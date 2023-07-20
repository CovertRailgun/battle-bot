import os

import disnake
from disnake.ext import commands

import settings

"""
There shouldn't be anything in main.py that needs to get changed.

Most of the stuff you might want to do can be done in either the cogs directory or settings.py
"""

class bot(commands.InteractionBot):
    log = settings.logging.getLogger('bot')


    async def on_ready(self) -> None:
        self.log.info(f"User: {self.user} (ID: {self.user.id})")    

if __name__ == '__main__':

    Bot = bot(
        intents=disnake.Intents.all(),
        asyncio_debug=True,
        )
    Bot.load_extensions("cogs")


    Bot.run(settings.DISCORD_BOT_TOKEN)
