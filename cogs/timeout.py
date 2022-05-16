import inspect
import asyncio
import datetime
import discord
from discord.ext import commands

class Timeout(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="timeout",
        aliases = ['to']
    )
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx: commands.Context, member: discord.Member, time, *, reason=None) -> None:
        """Timeout a user"""
        #log_channel = discord.utils.get(ctx.guild.channels, id=970211808830967879)
        time_convert = {"s":1, "m":60, "h":3600,"d":86400}
        duration= int(time[0]) * time_convert[time[-1]]
        until = datetime.timedelta(seconds=duration)
        embed = discord.Embed(
            title="Timeout",
            description = inspect.cleandoc(
                f"""
                **Offender:** {member.name}#{member.discriminator}
                **Duration** {time}s
                **Reason:** {reason}
                **Responsible moderator:** {ctx.author.name}#{ctx.author.discriminator}
                """
            ),
            color=0xff8b8b
        )
        embed.set_footer(text=f"ID: {member.id}")
        await member.timeout(until, reason=reason)
        await ctx.send(embed=embed)

        
async def setup(bot):
    await bot.add_cog(Timeout(bot))

