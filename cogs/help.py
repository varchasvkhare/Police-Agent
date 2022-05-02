from ast import Or
import inspect

import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="help"
    )
    async def help(self, ctx: commands.Context) -> None:
        """Help cmd you know"""
        
        embed = discord.Embed(
            title=f'Police Agent Services -',
            description=inspect.cleandoc(
            """
            **・Kick** - Kick a user from this server
            
            **・Poll** - Create a poll with 'yes' & 'no'
            
            **・Rules** - Get a list of all server rules
            
            **・Ping** - Get the latency
            """
            ),color=0xffdd93
        )
        await ctx.channel.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Help(bot))

