from ast import Or
import inspect

import discord
from discord.ext import commands

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="verify")
    async def verify(self, ctx: commands.Context) -> None:
        """Server Verification"""
        class Verification(discord.ui.View):
            @discord.ui.button(style=discord.ButtonStyle.green, label='Verify')
            async def verify_button(self, button: discord.ui.Button, interaction: discord.Interaction):
                interaction.user.add_roles(903238068910309398)
                interaction.response.send_message("You are now Verified!")
        
        embed = discord.Embed(
            title = "Verification",
            description = inspect.cleandoc(
                f"""
                Click below to verify
                """
            )
        )
        await ctx.send(embed=embed, view=Verification)
        
async def setup(bot):
    await bot.add_cog(Verify(bot))

