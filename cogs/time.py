import inspect
import asyncio
import datetime
import calendar
import discord
from discord.ext import commands

class Time(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="time"
    )
    async def timeout(self, ctx: commands.Context) -> None:
        """Check the time"""
        
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        
        epoch = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second).timestamp()
        await ctx.send(f"<t:{round(epoch)}>\n{day}-{month}-{year} {hour}:{minute}:{second}")

        
async def setup(bot):
    await bot.add_cog(Time(bot))

