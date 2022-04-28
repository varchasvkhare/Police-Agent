import random
import os
import traceback
import sys
import asyncio
import inspect

import discord
from discord.ext import commands, tasks
import asyncpg

BOT_TOKEN = 'OTE5MTQ5MDMzODIwNDE4MDU5.YbRmPg.rJRCJeOAicRK6vtvbs2jq43tmZA'
POSTGRES_DSN = 'postgres://lhjqkocefjmnmu:92530a413343e2a308556d0b2c76a72596a44640b3767c72cd53cc4eef8df956@ec2-3-224-125-117.compute-1.amazonaws.com:5432/d4teouam269f5t'

async def _prefix_callable(bot: commands.AutoShardedBot, message: discord.Message):
    if not hasattr(bot, 'db'): # hasnt connected
        return

    prefix = await bot.db.fetchval('SELECT prefix FROM prefixes WHERE guild_id = $1', message.guild.id) or '-' # default pre
    
    base = [
        f'<@{bot.user.id}>',
        f'<@!{bot.user.id}>',
        prefix
    ]
    
    return base

os.environ['JISHAKU_HIDE'] = 'True'
os.environ['JISHAKU_NO_UNDERSCORE'] = 'True'
os.environ['JISHAKU_FORCE_PAGINATOR'] = 'True'
os.environ['JISHAKU_NO_DM_TRACEBACK'] = 'True'

class Bot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix=_prefix_callable,
            shard_count=1, 
            intents=discord.Intents.all(),
            case_insensitive=True,
            strip_after_prefix=True,
            owner_ids=[
                868465221373665351,
                714731543309844561 # invalid
            ]
        )

        self.add_check(self.blacklisted_check)
    
    async def blacklisted_check(self, ctx: commands.Context):
        # bot owners bypass this
        if await bot.is_owner(ctx.author):
            return True

        res = await bot.db.fetchval('SELECT user_id FROM blacklist WHERE user_id = $1', ctx.author.id)
        if res: # db contains an entry - blacklisted so return False (cant use bot)
            delete_after: int = 7
            
            embed = discord.Embed(
                description='Unfortunately, you have been blacklisted from the bot. If you wish to know why or appeal, please join **[this server](https://discord.gg/xRquATkezz)**.'
            )
            await ctx.reply(
                embed=embed,
                delete_after=delete_after
            )
            await ctx.message.delete(delay=delete_after)

            return False
        else: # everything is normal, not blacklisted
            return True
    
    @tasks.loop(minutes=1)
    async def change_status(self):
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.playing,
                name=f'd/help | {str(len(self.guilds))} servers'
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
    
    async def _create_pool(self):
        try:
            self.db = await asyncpg.create_pool(dsn=POSTGRES_DSN)
        except Exception as exc:
            print('Failed to connect to database.')
            traceback.print_exc()
        else:
            print('Database connected.')

        await self.db.execute('CREATE TABLE IF NOT EXISTS prefixes (guild_id BIGINT, prefix TEXT)')

    async def setup_hook(self):
        asyncio.create_task(self._startup_task())
        await self._create_pool()
    
    async def start(self):
        await super().start(
            token=BOT_TOKEN,
            reconnect=True
        )

if __name__ == '__main__':
    bot = Bot()
    bot.run()