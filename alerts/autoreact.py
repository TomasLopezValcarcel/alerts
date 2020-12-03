import discord
import asyncio
from redbot.core import commands

class autoreact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 743840218750255164:
            await message.add_reaction('\U0001f1f9')
            await asyncio.sleep(0.1)
            await message.add_reaction('\U0001f1ed')
            await asyncio.sleep(0.1)
            await message.add_reaction('\U0001f1e6')
            await asyncio.sleep(0.1)
            await message.add_reaction('\U0001f1f3')
            await asyncio.sleep(0.1)
            await message.add_reaction('\U0001f1f0')
            await asyncio.sleep(0.1)
            await message.add_reaction('\U0001f1f8')
