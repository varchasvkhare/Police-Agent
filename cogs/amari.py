import inspect
import amari.py
import discord
from discord.ext import commands

class Amari(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="amari", aliases = ["level"]
    )
    async def amari(self, ctx: commands.Context, membed: discord.Member) -> None:
        """Check your amari level"""
        
        embed = discord.Embed(
            title=f"",
            description = inspect.cleandoc(
                f"""
                working
                """
            ),
            color=0x9C84EF
        )
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Amari(bot))

