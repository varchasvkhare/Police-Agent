import inspect

import discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="poll"
    )
    @commands.has_any_role(commands.has_permissions(administrator=True), 917120712840462416)
    async def poll(self, ctx: commands.Context, *, message) -> None:
        """Allows you to make a poll"""
        
        embed = discord.Embed(
            title=f'{ctx.message.author.name} asks',
            description=f'{message}', color=0x797EF6
        )
        embed.set_footer(text='react with any one option')
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Poll(bot))

