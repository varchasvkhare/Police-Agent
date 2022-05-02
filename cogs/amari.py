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
        id = ctx.author.id
        user = await amari.fetch_user(760134264242700320, id)
        
        embed = discord.Embed(
            title=f"Top Users",
            description = inspect.cleandoc(
                f"""
                {user.level}
                """
            ),
            color=0x9C84EF
        )
        
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Amari(bot))

