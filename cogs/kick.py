import inspect

import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="kick"
    )
    @commands. has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None) -> None:
        """Kick a user"""
        log_channel = discord.utils.get(ctx.guild.channels, id=970211808830967879)
        embed = discord.Embed(
            title="Kick",
            description = inspect.cleandoc(
                f"""
                **Offender:** {member.name}#{member.discriminator}
                **Reason:** {reason}
                **Responsible moderator:** {ctx.author.name}#{ctx.author.discriminator}
                """
            )
        )
        embed.set_footer(f"ID: {member.id}")
        if reason==None:
            reason="No reason provided"
            await ctx.guild.kick(member)
            await ctx.send(f"Successfully kicked {member.name}#{member.discriminator}")
            await log_channel.send(embed=embed)
        else:
            await ctx.guild.kick(member, reason=reason)
            await ctx.send(f"Successfully kicked {member.name}#{member.discriminator}")
            await log_channel.send(embed=embed)

        
async def setup(bot):
    await bot.add_cog(Kick(bot))

