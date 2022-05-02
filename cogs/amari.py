import inspect
from amari import AmariClient
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
        amari = AmariClient("e5e71cc6daa28c3d9bc848ee.435561.0813a19d4b9746eacf0d4e68857")
        lb = await amari.fetch_leaderboard(760134264242700320, weekly=True, limit=3)
        top_users_ids = [data[1] for data in list(lb.users.items())]
        
        embed = discord.Embed(
            title=f"Top Users",
            description = inspect.cleandoc(
                f"""
                {top_users_ids}
                """
            ),
            color=0x9C84EF
        )
        
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Amari(bot))

