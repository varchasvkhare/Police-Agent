import random
import os
import traceback
import sys
import asyncio
import inspect

import discord
from discord.ext import commands, tasks
import asyncpg

my_secret = os.environ['TOKEN']

class Client(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=_"-",
            intents=discord.Intents.all(),
            case_insensitive=True,
            strip_after_prefix=True,
            owner_ids=[
                868465221373665351, #khare
                748552378504052878  #pandey
            ]
        )
    
    @tasks.loop(minutes=1)
    async def change_status(self):
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=f'-help in Detective Hub'
            )
        )

    @change_status.before_loop
    async def _before_change_status(self):
        await self.wait_until_ready()

    async def _startup_task(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

        extensions = [
            'jishaku',
            *[
                f'cogs.{extension[:-3]}'
                for extension in os.listdir('./cogs')
                if extension.endswith('.py')
            ]
        ]

        for item in extensions:
            try:
                await self.load_extension(item)
            except Exception as exc:
                print(f"Failed to load extension {item}")
                traceback.print_exc()

        self.change_status.start()
        
    async def start(self):
        await super().start(
            token=os.getenv("TOKEN"),
            reconnect=True
        )

if __name__ == '__main__':
    bot = Client()
    bot.run()

